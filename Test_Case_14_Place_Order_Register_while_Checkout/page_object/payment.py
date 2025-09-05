import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from SeleniumAutomation.browser_utils.browser_utils import BrowserUtils
from selenium.common import TimeoutException, StaleElementReferenceException


class Payment(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.payment_text = (By.XPATH, "//h2[text()='Payment']")
        self.name_on_card = (By.XPATH, "//input[@data-qa='name-on-card']")
        self.card_number = (By.XPATH, "//input[@data-qa='card-number']")
        self.cvc = (By.XPATH, "//input[@data-qa='cvc']")
        self.expiration_month = (By.XPATH, "//input[@data-qa='expiry-month']")
        self.expiration_year = (By.XPATH, "//input[@data-qa='expiry-year']")
        self.pay_and_confirm_order_button = (By.XPATH, "//button[@data-qa='pay-button']")
        self.success_message = (By.XPATH, "//div[contains(@class, 'alert-success') and contains(text(), 'Your order has been placed successfully!')]")
        self.delete_account_button = (By.XPATH, "//a[contains(text(), 'Delete Account')]")

    def verify_payment_text(self):
        expected_text = "Payment"
        actual_text = self.driver.find_element(*self.payment_text).text

        assert actual_text.lower().strip() == expected_text.lower().strip(), \
            f"Expected '{expected_text}', but got '{actual_text}'"

    def verify_payment_page_by_url(self):
        actual_url = self.driver.current_url

        assert "payment" in actual_url, \
            f"Unexpected URL: {actual_url}"

    def verify_payment_page_by_text_and_url(self):
        self.verify_payment_text()
        self.verify_payment_page_by_url()

    def click_pay_and_confirm_order_button(self):
        self.driver.find_element(*self.pay_and_confirm_order_button).click()

    def enter_payment_details(self, data: dict):
        self.driver.find_element(*self.name_on_card).send_keys(data["name_on_card"])
        self.driver.find_element(*self.card_number).send_keys(data["card_number"])
        self.driver.find_element(*self.cvc).send_keys(data["cvc"])
        self.driver.find_element(*self.expiration_month).send_keys(data["expiration_month"])
        self.driver.find_element(*self.expiration_year).send_keys(data["expiration_year"])

    def verify_place_order_and_contact_success_message(self):
        expected_text = "Your order has been placed successfully!"
        retries = 3

        for attempt in range(1, retries + 1):
            try:
                print(f"🧪 嘗試取得成功訊息，第 {attempt} 次")
                element = self.wait.until(expected_conditions.presence_of_element_located(self.success_message))
                actual_text = element.text.strip()

                if not actual_text:
                    raise AssertionError("⚠️The success message element appears but has no text \n 成功訊息元素出現但沒有文字")

                assert actual_text.lower() == expected_text.lower(), \
                    f"Expected '{expected_text}', but got '{actual_text}'"
                print("✅ Success message verification passed \n成功訊息驗證通過")
                return
            except StaleElementReferenceException:
                print(f"⚠️ Success message element stale, retrying {attempt}th time...\n成功訊息元素 stale，第 {attempt} 次重試中...")
                time.sleep(1)
            except TimeoutException:
                print("⏰ 成功訊息等待逾時，準備檢查是否已跳轉")
                break  # 跳出 retry 迴圈，往後檢查跳轉

        # 若進入這邊，表示成功訊息沒有成功取得或驗證，檢查是否有跳轉頁面
        try:
            self.wait.until(expected_conditions.presence_of_element_located(self.delete_account_button))
            print("⚠️ The waiting time for the success message has expired. Check if the redirect has been completed.\n成功訊息抓不到，但頁面已成功跳轉，視為成功")
        except TimeoutException:
            raise AssertionError("❌ The success message did not appear, the page did not jump, and the process was abnormal.\n成功訊息沒出現，頁面也沒跳轉，流程異常")
