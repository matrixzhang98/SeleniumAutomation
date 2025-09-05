from selenium.webdriver.common.by import By
from SeleniumAutomation.browser_utils.browser_utils import BrowserUtils


class Checkout(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.address_details_text = (By.XPATH, "//h2[text()='Address Details']")
        # delivery address
        self.delivery_address_text = (By.XPATH, "//h3[text()='Your delivery address']")
        self.da_firstname_lastname = (By.XPATH, "//ul[@id='address_delivery']//li[contains(@class, 'address_firstname address_lastname')]")
        self.da_company = (By.XPATH, "//ul[@id='address_delivery']/li[contains(@class, 'address_address1 address_address2')][1]")
        self.da_address = (By.XPATH, "//ul[@id='address_delivery']/li[contains(@class, 'address_address1 address_address2')][2]")
        self.da_address2 = (By.XPATH, "//ul[@id='address_delivery']/li[contains(@class, 'address_address1 address_address2')][3]")
        self.da_city_state_zip = (By.XPATH, "//ul[@id='address_delivery']/li[contains(@class, 'address_city address_state_name address_postcode')]")
        self.da_country = (By.XPATH, "//ul[@id='address_delivery']/li[contains(@class, 'address_country_name')]")
        self.da_mobile = (By.XPATH, "//ul[@id='address_delivery']/li[contains(@class, 'address_phone')]")
        # billing address
        self.billing_address_text = (By.XPATH, "//h3[text()='Your billing address']")
        self.ba_firstname_lastname = (By.XPATH, "//ul[@id='address_invoice']//li[contains(@class, 'address_firstname address_lastname')]")
        self.ba_company = (By.XPATH, "//ul[@id='address_invoice']/li[contains(@class, 'address_address1 address_address2')][1]")
        self.ba_address = (By.XPATH, "//ul[@id='address_invoice']/li[contains(@class, 'address_address1 address_address2')][2]")
        self.ba_address2 = (By.XPATH, "//ul[@id='address_invoice']/li[contains(@class, 'address_address1 address_address2')][3]")
        self.ba_city_state_zip = (By.XPATH, "//ul[@id='address_invoice']/li[contains(@class, 'address_city address_state_name address_postcode')]")
        self.ba_country = (By.XPATH, "//ul[@id='address_invoice']/li[contains(@class, 'address_country_name')]")
        self.ba_mobile = (By.XPATH, "//ul[@id='address_invoice']/li[contains(@class, 'address_phone')]")
        # review order
        self.review_order_text = (By.XPATH, "//h2[text()='Review Your Order']")
        self.total_price = (By.XPATH, "(//p[contains(@class, 'cart_total_price')])[last()]")
        # place order
        self.comment = (By.XPATH, "//textarea[@name='message']")
        self.place_order_button = (By.XPATH, "//a[text()='Place Order']")


    def verify_address_details_text(self):
        expected_text = "Address Details"
        actual_text = self.driver.find_element(*self.address_details_text).text

        assert actual_text.lower().strip() == expected_text.lower().strip(), \
            f"Expected '{expected_text}', but got '{actual_text}'"

    def verify_delivery_address_text(self):
        expected_text = "YOUR DELIVERY ADDRESS"
        actual_text = self.driver.find_element(*self.delivery_address_text).text

        assert actual_text.lower().strip() == expected_text.lower().strip(), \
            f"Expected '{expected_text}', but got '{actual_text}'"

    def verify_billing_address_text(self):
        expected_text = "YOUR BILLING ADDRESS"
        actual_text = self.driver.find_element(*self.billing_address_text).text

        assert actual_text.lower().strip() == expected_text.lower().strip(), \
            f"Expected '{expected_text}', but got '{actual_text}'"

    def verify_delivery_address(self, data: dict):
        locators = {
            "name": self.da_firstname_lastname,
            "company": self.da_company,
            "address": self.da_address,
            "address2": self.da_address2,
            "city_state_zip": self.da_city_state_zip,
            "country": self.da_country,
            "mobile_number": self.da_mobile,
        }
        self._verify_address(data, locators)

    def verify_billing_address(self, data: dict):
        locators = {
            "name": self.ba_firstname_lastname,
            "company": self.ba_company,
            "address": self.ba_address,
            "address2": self.ba_address2,
            "city_state_zip": self.ba_city_state_zip,
            "country": self.ba_country,
            "mobile_number": self.ba_mobile,
        }
        self._verify_address(data, locators)

    def _verify_address(self, data: dict, locators: dict):
        name = self.driver.find_element(*locators["name"]).text
        company = self.driver.find_element(*locators["company"]).text
        address = self.driver.find_element(*locators["address"]).text
        address2 = self.driver.find_element(*locators["address2"]).text
        city_state_zip = self.driver.find_element(*locators["city_state_zip"]).text
        country = self.driver.find_element(*locators["country"]).text
        mobile_number = self.driver.find_element(*locators["mobile_number"]).text

        new_name = self.concat_firstname_lastname(data)
        new_city_state_zip = self.concat_city_state_zip(data)

        assert new_name == name, \
            f"Expected '{new_name}', but got '{name}'"

        excepted_company = data.get("company", "")
        assert excepted_company == company, \
            f"Expected '{excepted_company}', but got '{company}'"

        assert data['address'] == address, \
            f"Expected '{data['address']}', but got '{address}'"

        excepted_address2 = data.get("address2", "")
        assert excepted_address2 == address2, \
            f"Expected '{excepted_address2}', but got '{address2}'"

        assert new_city_state_zip == city_state_zip, \
            f"Expected '{new_city_state_zip}', but got '{city_state_zip}'"

        assert data['country'] == country, \
            f"Expected '{data['country']}', but got '{country}'"

        assert data['mobile_number'] == mobile_number, \
            f"Expected '{data['mobile_number']}', but got '{mobile_number}'"

    @staticmethod
    def concat_firstname_lastname(data: dict):
        gender = data["gender"]
        first_name = data["first_name"]
        last_name = data["last_name"]

        if gender == "male":
            new_concat_name = f"Mr. {first_name} {last_name}"
        else:
            new_concat_name = f"Mrs. {first_name} {last_name}"
        return new_concat_name

    @staticmethod
    def concat_city_state_zip(data: dict):
        city = data["city"]
        state = data["state"]
        zipcode = data["zipcode"]
        return f"{city} {state} {zipcode}"

    def verify_all_addresses(self, data: dict):
        self.verify_delivery_address(data)
        self.verify_billing_address(data)

    def enter_comment_and_click_place_order_button(self, data: dict):
        self.driver.find_element(*self.comment).send_keys(data["comment"])
        self.driver.find_element(*self.place_order_button).click()

    def get_total_price(self):
        price = self.driver.find_element(*self.total_price).text
        new_price = price.split()
        print("[DEBUG] new_price: ", new_price)
        return new_price[1]