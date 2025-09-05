from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from SeleniumAutomation.browser_utils.browser_utils import BrowserUtils


class Register(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.select_gender_male = (By.XPATH, "//div[@id='uniform-id_gender1']")
        self.select_gender_female = (By.XPATH, "//div[@id='uniform-id_gender2']")
        self.sign_up_password = (By.XPATH, "//input[@data-qa='password']")
        self.days_dropdown = (By.XPATH, "//select[@data-qa='days']")
        self.months_dropdown = (By.XPATH, "//select[@data-qa='months']")
        self.years_dropdown = (By.XPATH, "//select[@data-qa='years']")
        self.newsletter_checkbox = (By.XPATH, "//input[@name='newsletter']")
        self.special_offers_checkbox = (By.XPATH, "//input[@name='optin']")
        self.enter_account_info = (By.XPATH, "//b[text()='Enter Account Information']")
        self.first_name = (By.XPATH, "//input[@id='first_name']")
        self.last_name = (By.XPATH, "//input[@id='last_name']")
        self.company = (By.XPATH, "//input[@data-qa='company']")
        self.address = (By.XPATH, "//input[@data-qa='address']")
        self.address2 = (By.XPATH, "//input[@data-qa='address2']")
        self.country = (By.XPATH, "//select[@id='country']")
        self.state = (By.XPATH, "//input[@id='state']")
        self.city = (By.XPATH, "//input[@id='city']")
        self.zipcode = (By.XPATH, "//input[@id='zipcode']")
        self.mobile_number = (By.XPATH, "//input[@id='mobile_number']")
        self.create_account = (By.XPATH, "//button[@data-qa='create-account']")

    def select_gender(self, gender: str):
        gender = gender.lower()

        if gender in ("mr.", "male"):
            element = self.driver.find_element(*self.select_gender_male)
        elif gender in ("mrs.", "female"):
            element = self.driver.find_element(*self.select_gender_female)
        else:
            raise ValueError(f"Unknown gender value: {gender}")
        element.click()

    def select_day(self, days: str):
        element = self.driver.find_element(*self.days_dropdown)
        Select(element).select_by_visible_text(days)

    def select_month(self, months: str):
        element = self.driver.find_element(*self.months_dropdown)
        Select(element).select_by_visible_text(months)

    def select_year(self, years: str):
        element = self.driver.find_element(*self.years_dropdown)
        Select(element).select_by_visible_text(years)

    def select_country(self, country: str):
        element = self.driver.find_element(*self.country)
        Select(element).select_by_visible_text(country)

    def _send_if_exist(self, locater, value):
        if value:
            self.driver.find_element(*locater).send_keys(value)

    def verify_enter_text(self):
        element = self.wait.until(expected_conditions.visibility_of_element_located(self.enter_account_info))
        actual_text = element.text
        expected_text = "ENTER ACCOUNT INFORMATION"
        assert actual_text == expected_text, \
            f"Expected '{expected_text}', but got '{actual_text}'"

    def fill_account_information(self, data: dict):
        self.select_gender(data["gender"])
        self.driver.find_element(*self.sign_up_password).send_keys(data["password"])
        self.select_day(data["day"])
        self.select_month(data["month"])
        self.select_year(data["year"])

    def select_account_newsletter(self, data: dict):
        if data.get("newsletter"):
            self.safe_click(*self.newsletter_checkbox)

    def select_account_special_offers(self, data: dict):
        if data.get("special_offers"):
            self.safe_click(*self.special_offers_checkbox)

    def fill_address_information(self, data: dict):
        self.driver.find_element(*self.first_name).send_keys(data["first_name"])
        self.driver.find_element(*self.last_name).send_keys(data["last_name"])

        self._send_if_exist(self.company, data.get("company"))
        self.driver.find_element(*self.address).send_keys(data["address"])

        self._send_if_exist(self.address2, data.get("address2"))
        self.select_country(data["country"])

        self.driver.find_element(*self.state).send_keys(data["state"])
        self.driver.find_element(*self.city).send_keys(data["city"])
        self.driver.find_element(*self.zipcode).send_keys(data["zipcode"])
        self.driver.find_element(*self.mobile_number).send_keys(data["mobile_number"])

    def click_create_account_button(self):
        self.aggressive_safe_click(*self.create_account)
