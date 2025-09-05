from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from SeleniumAutomation.browser_utils.browser_utils import BrowserUtils

class CartPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.description = (By.XPATH, ".//td[@class='cart_description']//h4/a")
        self.description_category = (By.XPATH, ".//td[@class='cart_description']//p")
        self.price = (By.XPATH, ".//td[@class='cart_price']//p")
        self.quantity = (By.XPATH, ".//td[@class='cart_quantity']/button")
        self.total_price = (By.XPATH, ".//td[@class='cart_total']/p")
        self.delete_button = (By.XPATH, ".//td[@class='cart_delete']/a")

        self.proceed_to_checkout_button = (By.XPATH, "//a[text()='Proceed To Checkout']")
        self.register_login_button = (By.XPATH, "//u[text()='Register / Login']")

    # verify product name
    def verify_products_added_correctly_in_cart(self, expected_products: list[dict]):
        wait = WebDriverWait(self.driver, 5)

        product_ele \
            = wait.until(expected_conditions.visibility_of_all_elements_located(self.description))

        assert len(product_ele) == len(expected_products), \
            f"Expected {len(expected_products)} products but got {len(product_ele)}"

        for i, expected in enumerate(expected_products):
            product_name = product_ele[i].text.strip()

            assert product_name == expected["name"], \
                f"Expected {expected['name']}, but got {product_name}"


    # verify price、quantity、total_price
    def verify_carts_details_info(self, expected_products: list[dict]):
        wait = WebDriverWait(self.driver, 5)

        price_ele \
            = wait.until(expected_conditions.visibility_of_all_elements_located(self.price))

        quantity_ele \
            = wait.until(expected_conditions.visibility_of_all_elements_located(self.quantity))

        total_price_ele \
            = wait.until(expected_conditions.visibility_of_all_elements_located(self.total_price))

        for i, expected in enumerate(expected_products):
            actual_price = price_ele[i].text.strip()
            actual_quantity = quantity_ele[i].text.strip()
            actual_total_price = total_price_ele[i].text.strip()

            expected_price = expected["price"]
            expected_quantity = str(expected["quantity"])
            '''
                expected_price.split()[-1]
                假設 expected_price = "Rs. 1500"
                
                expected_price.split() → ["Rs.", "1500"]
                expected_price.split()[-1] → "1500"
            '''
            expected_total_price = f"Rs. {int(expected_price.split()[-1]) * int(expected_quantity)}"

            assert actual_price == expected_price, \
                f"Expected {expected_price}, but got {actual_price}"

            assert actual_quantity == expected_quantity, \
                f"Expected {expected_quantity}, but got {actual_quantity}"

            assert actual_total_price == expected_total_price, \
                f"Expected {expected_total_price}, but got {actual_total_price}"

    def verify_cart_page_by_url(self):
        actual_url = self.driver.current_url

        assert "view_cart" in actual_url.lower(), \
            f"Unexpected URL: {actual_url}"

    def click_proceed_to_checkout_button(self):
        self.driver.find_element(*self.proceed_to_checkout_button).click()

    def click_register_login_button(self):
        current_url = self.driver.current_url

        wait = WebDriverWait(self.driver, 5)
        ele =wait.until(expected_conditions.visibility_of_element_located(self.register_login_button))
        ele.click()

        wait.until(expected_conditions.url_changes(current_url))
        new_url = self.driver.current_url

        assert "login" in new_url.lower(), \
            f"Unexpected URL: {new_url}"