from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from SeleniumAutomation.browser_utils.browser_utils import BrowserUtils


class DeletedAccount(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.account_deleted_text = (By.XPATH, "//h2[@data-qa='account-deleted']")
        self.continue_btn_after_deleted_account = (By.XPATH, "//a[@data-qa='continue-button']")

    def verify_deleted_account_text_and_click_continue_button(self):
        element \
            = self.wait.until(expected_conditions.visibility_of_element_located(self.account_deleted_text))

        actual_text = element.text
        expected_text = "ACCOUNT DELETED!"

        assert actual_text == expected_text, \
            f"Expected '{expected_text}', but got '{actual_text}'"

        self.aggressive_safe_click(*self.continue_btn_after_deleted_account)