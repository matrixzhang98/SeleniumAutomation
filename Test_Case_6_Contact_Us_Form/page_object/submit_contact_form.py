from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from SeleniumAutomation.browser_utils.browser_utils import BrowserUtils


class SubmitContactForm(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.success_message = (By.XPATH, "//div[@class='status alert alert-success']")
        self.home_button = (By.XPATH, "//i[@class='fa fa-angle-double-left']")

    def verify_submit_contact_success_message(self):
        element = (
            self.wait.until(expected_conditions.visibility_of_element_located(self.success_message)))

        actual_text = element.text
        expected_text = "Success! Your details have been submitted successfully."
        assert actual_text == expected_text, \
            f"expected '{expected_text}', but got '{actual_text}'"
