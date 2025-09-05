from selenium.webdriver.common.by import By
from SeleniumAutomation.browser_utils.browser_utils import BrowserUtils


class LoginIncorrectInfo(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.incorrect_info = (By.XPATH, "//p[text()='Your email or password is incorrect!']")

    def verify_incorrect_info(self):
        element = self.driver.find_element(*self.incorrect_info)
        actual_info = element.text
        expected_info = "Your email or password is incorrect!"
        assert actual_info == expected_info, \
            f"Expected: '{expected_info}', but got '{actual_info}'"