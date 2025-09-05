from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from SeleniumAutomation.browser_utils.browser_utils import BrowserUtils


class CreatedAccountLogged(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logged_text = (By.XPATH, "//a[contains(., 'Logged in as')]")
        self.delete_account_btn = (By.XPATH, "//a[contains(.,'Delete Account')]")

    def verify_logged_in_as(self, data: dict):
        element = self.wait.until(expected_conditions.visibility_of_element_located(self.logged_text))
        actual_text = element.text.strip()
        expected_text = f"Logged in as {data["name"]}"

        assert actual_text == expected_text, \
            f"Expected '{expected_text}', but got '{actual_text}'"

    def click_delete_account_button(self):
        self.aggressive_safe_click(*self.delete_account_btn)