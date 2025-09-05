from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException


class BrowserUtils:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.header = (By.XPATH, "//header[@id='header']")
        self.footer = (By.CSS_SELECTOR, ".footer-widget")
        self.subscription_text = (By.XPATH, "//h2[text()='Subscription']")
        # 前端的html就是把id拼錯
        self.subscription_input_box = (By.XPATH, "//input[@id='susbscribe_email']") # noqa
        self.subscription_arrow_button = (By.XPATH, "//button[@id='subscribe']")
        self.subscribe_success_message =(By.ID, "success-subscribe")
        self.ads_iframe = (By.XPATH, "//iframe[starts-with(@id, 'aswift')]") # noqa

    def scroll_up_to_header(self):
        header = self.wait.until(
            expected_conditions.presence_of_element_located(self.header)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({ behavior: 'smooth', block: 'start' });",
            header
        )

        assert header.is_displayed(), "Header not visible after scroll"

    def scroll_down_to_footer(self):
        footer = self.wait.until(
            expected_conditions.presence_of_element_located(self.footer)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({ behavior: 'smooth', block: 'end' });",
            footer
        )

        assert footer.is_displayed(), "Footer not visible after scroll"

    def verify_text_subscription(self):
        subscription_element = self.wait.until(expected_conditions.visibility_of_element_located(self.subscription_text))

        expected_text = "SUBSCRIPTION"
        actual_text = subscription_element.text
        assert actual_text == expected_text, \
            f"Expected '{expected_text}', but got '{actual_text}'"

    def enter_subscribe_email_and_submit(self, data: dict):
        self.driver.find_element(*self.subscription_input_box).send_keys(data["email"])
        self.driver.find_element(*self.subscription_arrow_button).click()

    def verify_success_subscribe_message(self):
        message_element = (
            self.wait.until(expected_conditions.visibility_of_element_located(self.subscribe_success_message)))

        expected_text = "You have been successfully subscribed!"
        actual_text = message_element.text
        assert actual_text == expected_text, \
            f"Expected '{expected_text}', but got '{actual_text}'"

    def scroll_element_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def click_element_by_js(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    def remove_ads_iframe(self):
        # 等待 iframe 廣告載入後再移除（最多等 5 秒）
        try:
            self.wait.until(
                expected_conditions.presence_of_element_located(self.ads_iframe)
            )
            self.driver.execute_script("""
                var ads = document.querySelectorAll('iframe[id^="aswift"]');
                ads.forEach(ad => ad.remove());
            """) # noqa
        except TimeoutException:
            # 若 5 秒內沒出現也繼續執行，不報錯
            pass

    def remove_all_ads_iframe(self):
        # 等待 iframe 廣告載入後再移除（最多等 5 秒）
        try:
            self.wait.until(
                expected_conditions.presence_of_element_located(self.ads_iframe)
            )
            self.driver.execute_script("document.querySelectorAll('iframe').forEach(el => el.remove());")
        except TimeoutException:
            # 若 5 秒內沒出現也繼續執行，不報錯
            pass

    def safe_click(self, by, value, context=None, max_attempts=3):
        """帶重試的安全點擊，避免 iframe 或 DOM 干擾"""
        for attempt in range(max_attempts):
            try:
                self.remove_ads_iframe()
                element = context.find_element(by, value) if context else self.driver.find_element(by, value)
                self.scroll_element_into_view(element)
                element.click()
                return
            except (ElementClickInterceptedException, NoSuchElementException):
                if attempt == max_attempts - 1:
                    raise
                continue

    def aggressive_safe_click(self, by, value, context=None, max_attempts=5):
        for attempt in range(max_attempts):
            try:
                self.remove_all_ads_iframe()
                element = context.find_element(by, value) if context else self.driver.find_element(by, value)
                self.scroll_element_into_view(element)
                element.click()
                return
            except (ElementClickInterceptedException, NoSuchElementException):
                if attempt == max_attempts - 1:
                    raise
                continue
