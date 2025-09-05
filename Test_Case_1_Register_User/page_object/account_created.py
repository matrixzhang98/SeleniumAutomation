from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from SeleniumAutomation.browser_utils.browser_utils import BrowserUtils


class AccountCreated(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.account_created = (By.XPATH, "//h2[@data-qa='account-created']")
        self.create_account_continue = (By.XPATH, "//a[@data-qa='continue-button']")

    def verify_account_created_text(self):
        element = self.wait.until(expected_conditions.visibility_of_element_located(self.account_created))
        actual_text_for_created_acc = element.text
        expected_text_for_created_acc = "ACCOUNT CREATED!"

        assert actual_text_for_created_acc == expected_text_for_created_acc, \
            f"Expected '{expected_text_for_created_acc}', but got '{actual_text_for_created_acc}'"

    def click_create_account_continue_button(self):
        self.aggressive_safe_click(*self.create_account_continue)

    def verify_account_created_text_and_click_continue_button(self):
        self.verify_account_created_text()
        self.click_create_account_continue_button()