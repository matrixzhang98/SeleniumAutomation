from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from SeleniumAutomation.browser_utils.browser_utils import BrowserUtils
from SeleniumAutomation.Test_Case_1_Register_User.page_object.register import Register


class SignupLogin(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.new_user_sign_up_text = (By.XPATH, "//h2[text()='New User Signup!']")
        self.sign_up_name = (By.XPATH, "//input[@data-qa='signup-name']")
        self.sign_up_email = (By.XPATH, "//input[@data-qa='signup-email']")
        self.sign_up_submit = (By.XPATH, "//button[@data-qa='signup-button']")

        self.login_page_text = (By.XPATH, "//h2[text()='Login to your account']")
        self.login_email = (By.XPATH, "//input[@data-qa='login-email']")
        self.login_password = (By.XPATH, "//input[@data-qa='login-password']")
        self.login_button = (By.XPATH, "//button[@data-qa='login-button']")
        self.logout_button = (By.XPATH, "//a[text()=' Logout']")

        self.account_exist_info = (By.XPATH, "//p[text()='Email Address already exist!']")

    def verify_new_user_signup_text(self):
        wait = WebDriverWait(self.driver, 10)
        element \
            = wait.until(expected_conditions.visibility_of_element_located(self.new_user_sign_up_text))
        print("Step 5: " , element.text)

        actual_text = element.text
        expected_text = "New User Signup!"

        assert actual_text == expected_text, \
            f"Expected '{expected_text}', but got '{actual_text}'"

    def verify_login_page_text(self):
        wait = WebDriverWait(self.driver, 10)
        login_page_element \
            = wait.until(expected_conditions.visibility_of_element_located(self.login_page_text))

        actual_text = login_page_element.text
        expected_text = "Login to your account"

        assert actual_text == expected_text, \
            f"Expected '{expected_text}', but got '{actual_text}'"

    def fill_signup_page(self, data: dict):
        self.driver.find_element(*self.sign_up_name).send_keys(data["name"])
        self.driver.find_element(*self.sign_up_email).send_keys(data["email"])

    def click_signup_button(self):
        self.driver.find_element(*self.sign_up_submit).click()

    def fill_login_page(self, data: dict):
        self.driver.find_element(*self.login_email).send_keys(data["email"])
        self.driver.find_element(*self.login_password).send_keys(data["password"])

    def fill_incorrect_login_info(self, data: dict):
        self.driver.find_element(*self.login_email).send_keys(data["incorrect_login_email"])
        self.driver.find_element(*self.login_password).send_keys(data["incorrect_login_password"])

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()

    def click_logout_button(self):
        self.driver.find_element(*self.logout_button).click()

    def account_exist_text(self):
        wait = WebDriverWait(self.driver, 10)
        info = wait.until(expected_conditions.visibility_of_element_located(self.account_exist_info))

        actual_text = info.text
        expected_text = "Email Address already exist!"

        assert actual_text == expected_text, \
            f"Expected '{expected_text}', but got '{actual_text}'"

    def full_register_process(self, data: dict):
        register = Register(self.driver)
        self.fill_signup_page(data)
        self.click_signup_button()
        register.fill_account_information(data)
        register.fill_address_information(data)
        register.click_create_account_button()