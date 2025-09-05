from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from SeleniumAutomation.browser_utils.browser_utils import BrowserUtils


class ContactUs(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.get_in_touch_text = (By.XPATH, "//h2[text()='Get In Touch']")
        self.form_name = (By.XPATH, "//input[@data-qa='name']")
        self.form_email = (By.XPATH, "//input[@data-qa='email']")
        self.form_subject = (By.XPATH, "//input[@data-qa='subject']")
        self.form_message = (By.XPATH, "//textarea[@data-qa='message']")
        self.form_file = (By.XPATH, "//input[@name='upload_file']")
        self.form_submit = (By.XPATH, "//input[@data-qa='submit-button']")

    def verify_contact_us_info(self):
        element = (
            self.wait.until(expected_conditions.visibility_of_element_located(self.get_in_touch_text)))

        actual_text = element.text
        expected_text = "GET IN TOUCH"
        assert actual_text == expected_text, \
            f"Expected '{expected_text}', but got '{actual_text}'"

    def fill_contact_us_form(self, data: dict):
        self.driver.find_element(*self.form_name).send_keys(data["name"])
        self.driver.find_element(*self.form_email).send_keys(data["email"])
        self.driver.find_element(*self.form_subject).send_keys(data["subject"])
        self.driver.find_element(*self.form_message).send_keys(data["message"])

    def upload_file(self, data: dict):
        self.driver.find_element(*self.form_file).send_keys(data["file"])

    def click_submit_button(self):
        self.driver.find_element(*self.form_submit).click()

    def click_popup_accept(self):
        self.wait.until(expected_conditions.alert_is_present())
        self.driver.switch_to.alert.accept()