import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from SeleniumAutomation.browser_utils.browser_utils import BrowserUtils
from SeleniumAutomation.page_objects.signup_login import SignupLogin


class HomePage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.homepage_logo = (By.XPATH, "//img[@alt='Website for automation practice']")
        self.sign_up_button = (By.XPATH, "//a[contains(text(), 'Signup / Login')]")
        self.home_button = (By.XPATH, "//a[text()=' Home']")
        self.cart_button = (By.XPATH, "//a[text()=' Cart']")
        self.contact_us = (By.XPATH, "//a[text()=' Contact us']")
        self.test_cases_button = (By.XPATH, "//a[text()=' Test Cases']")
        self.products_button = (By.XPATH, "//a[text()=' Products']")

    def verify_home_page_by_url(self):
        expected_url = "https://automationexercise.com/"
        actual_url = self.driver.current_url

        print("Step 3: ", actual_url)

        assert "automationexercise" in actual_url.lower(), \
            f"Unexpected URL: {actual_url}"

        assert actual_url == expected_url, \
            f"Expected URL '{expected_url}', but got '{actual_url}'"

        wait = WebDriverWait(self.driver, 10)
        homepage_logo \
            = wait.until(expected_conditions.visibility_of_element_located(self.homepage_logo))

        assert homepage_logo.is_displayed(), \
            f"Home page logo is not visible — page may not have loaded correctly"

    @allure.step("Step 1 ~ 5: Navigate to login page and verify login prompt")
    def navigate_to_login_page_and_verify_text(self):
        self.verify_home_page_by_url()
        self.click_signup_link()
        sign_up_login_page = SignupLogin(self.driver)
        sign_up_login_page.verify_new_user_signup_text()
        sign_up_login_page.verify_login_page_text()

    def click_signup_link(self):
        self.driver.find_element(*self.sign_up_button).click()

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
