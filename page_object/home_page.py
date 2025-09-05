import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from SeleniumAutomation.page_object.signup_login import SignupLogin
from SeleniumAutomation.browser_utils.browser_utils import BrowserUtils


class HomePage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.signup_login = SignupLogin(driver)
        self.wait = WebDriverWait(driver, 10)
        self.homepage_logo = (By.XPATH, "//img[@alt='Website for automation practice']")
        self.signup_login_button = (By.XPATH, "//a[contains(text(), 'Signup / Login')]")
        self.home_button = (By.XPATH, "//a[text()=' Home']")
        self.cart_button = (By.XPATH, "//a[text()=' Cart']")
        self.contact_us = (By.XPATH, "//a[text()=' Contact us']")
        self.test_cases_button = (By.XPATH, "//a[text()=' Test Cases']")
        self.products_button = (By.XPATH, "//a[text()=' Products']")
        self.brands_text = (By.XPATH, "//div[@class='brands_products']//h2[text()='Brands']")
        self.scroll_up_button = (By.XPATH, "//a[@id='scrollUp']")
        self.carousel_text = (By.XPATH, "//h2[text()='Full-Fledged practice website for Automation Engineers']")

    @allure.step("Step 1 ~ 5: Navigate to login page and verify login prompt")
    def navigate_to_login_page_and_verify_text(self):
        self.verify_home_page_by_url()
        self.click_signup_login_button()
        self.signup_login.verify_new_user_signup_text()
        self.signup_login.verify_login_page_text()

    def verify_home_page_by_url(self):
        expected_url = "https://automationexercise.com/"
        actual_url = self.driver.current_url

        print("Step 3: ", actual_url)

        assert "automationexercise" in actual_url.lower(), \
            f"Unexpected URL: {actual_url}"

        assert actual_url == expected_url, \
            f"Expected URL '{expected_url}', but got '{actual_url}'"

        homepage_logo \
            = self.wait.until(expected_conditions.visibility_of_element_located(self.homepage_logo))

        # 只有WebElement才可以用is_displayed()
        assert homepage_logo.is_displayed(), \
            f"Home page logo is not visible — page may not have loaded correctly"

    def verify_brands_text(self):
        expected_text = "BRANDS"
        actual_text = self.driver.find_element(*self.brands_text).text

        assert actual_text.lower().strip() == expected_text.lower().strip(), \
            f"Expected '{expected_text}', but got '{actual_text}'"

    def verify_pages_is_scrolled_up_and_carousel_text_is_visible(self):
        self.wait.until(expected_conditions.invisibility_of_element_located(self.scroll_up_button))

        element = self.driver.find_element(*self.carousel_text)
        assert element.is_displayed(), "Text element is not visible"

        expected_text = "Full-Fledged practice website for Automation Engineers"
        actual_text = self.driver.find_element(*self.carousel_text).text

        assert actual_text.lower().strip() == expected_text.lower().strip(), \
            f"Expected '{expected_text}', but got '{actual_text}'"

    def click_signup_login_button(self):
        self.driver.find_element(*self.signup_login_button).click()

    def click_home_button(self):
        self.driver.find_element(*self.home_button).click()

    def click_contact_us(self):
        self.driver.find_element(*self.contact_us).click()

    def click_test_cases_button(self):
        self.driver.find_element(*self.test_cases_button).click()

    def click_products_button(self):
        self.driver.find_element(*self.products_button).click()

    def click_cart_button(self):
        self.driver.find_element(*self.cart_button).click()

    def click_category_link(self, data: dict):
        category = data["category"].capitalize()
        category_link = (By.XPATH, f"//a[@data-toggle='collapse' and contains(., '{category}')]")
        self.driver.find_element(*category_link).click()

    def click_subcategory_link(self, data: dict):
        category = data["category"].capitalize()
        subcategory = data["subcategory"].capitalize()
        subcategory_link = (By.XPATH, f"//div[@id='{category}']//a[contains(., '{subcategory}')]")
        self.wait.until(expected_conditions.visibility_of_element_located(subcategory_link))
        self.driver.find_element(*subcategory_link).click()

    def click_category_and_subcategory_link(self, data: dict):
        self.click_category_link(data)
        self.click_subcategory_link(data)

    def click_any_brand_name(self, brand: str) -> str:
        locator  = (By.XPATH, f"//li//a[text()='{brand}']")
        self.driver.find_element(*locator).click()
        return brand

    def click_scroll_up_button(self):
        self.driver.find_element(*self.scroll_up_button).click()
