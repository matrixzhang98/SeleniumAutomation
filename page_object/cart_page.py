from selenium.webdriver.common.by import By
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from SeleniumAutomation.browser_utils.browser_utils import BrowserUtils


class CartPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        self.description = (By.XPATH, ".//td[@class='cart_description']//h4/a")
        self.description_category = (By.XPATH, ".//td[@class='cart_description']//p")
        self.price = (By.XPATH, ".//td[@class='cart_price']//p")
        self.quantity = (By.XPATH, ".//td[@class='cart_quantity']/button")
        self.total_price = (By.XPATH, ".//td[@class='cart_total']/p")
        self.delete_button = (By.XPATH, ".//td[@class='cart_delete']/a")
        self.proceed_to_checkout_button = (By.XPATH, "//a[text()='Proceed To Checkout']")
        self.register_login_button = (By.XPATH, "//u[text()='Register / Login']")


    # verify product name is visible
    def verify_products_added_correctly_in_cart(self, expected_products: list[dict]):
        product_ele \
            = self.wait.until(expected_conditions.visibility_of_all_elements_located(self.description))

        assert len(product_ele) == len(expected_products), \
            f"Expected '{len(expected_products)}' products but got '{len(product_ele)}'"

        for i, expected in enumerate(expected_products):
            product_name = product_ele[i].text.strip()
            assert product_name == expected["name"], \
                f"Expected '{expected['name']}', but got '{product_name}'"

    def verify_carousel_products_added_correctly_in_cart(self, expected_products: list[dict]):
        # 定位所有商品的<tr>標籤
        product_rows = self.wait.until(
            expected_conditions.visibility_of_all_elements_located((By.CSS_SELECTOR, "#cart_info_table tbody tr"))
        )

        # 建立 dict，key 是商品名稱，value 是商品價格
        cart_products = {}
        for row in product_rows:
            # 商品名稱在 cart_description > h4 > a
            name = row.find_element(By.CSS_SELECTOR, "td.cart_description h4 a").text.strip()
            # 價格在 cart_price > p
            price = row.find_element(By.CSS_SELECTOR, "td.cart_price p").text.strip()
            cart_products[name] = price

        # 逐一驗證 expected_products 是否存在，且價格符合
        for expected in expected_products:
            name = expected["name"]
            price = expected["price"]

            assert name in cart_products, f"Product '{name}' not found in cart"
            assert cart_products[name] == price, f"Product '{name}' price expected '{price}' but got '{cart_products[name]}'"

    # verify price、quantity、total_price are visible
    def verify_carts_details_info(self, expected_products: list[dict]):
        price_ele \
            = self.wait.until(expected_conditions.visibility_of_all_elements_located(self.price))

        quantity_ele \
            = self.wait.until(expected_conditions.visibility_of_all_elements_located(self.quantity))

        total_price_ele \
            = self.wait.until(expected_conditions.visibility_of_all_elements_located(self.total_price))

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
                f"Expected '{expected_price}', but got '{actual_price}'"

            assert actual_quantity == expected_quantity, \
                f"Expected '{expected_quantity}', but got '{actual_quantity}'"

            assert actual_total_price == expected_total_price, \
                f"Expected '{expected_total_price}', but got '{actual_total_price}'"

    def verify_carousel_cart(self, added_products: list, expected_products: list[dict]):
        self.verify_carousel_products_added_correctly_in_cart(added_products)
        self.verify_carts_details_info(expected_products)

    def verify_cart(self, added_products: list, expected_products: list[dict]):
        self.verify_products_added_correctly_in_cart(added_products)
        self.verify_carts_details_info(expected_products)

    def verify_cart_page_by_url(self):
        actual_url = self.driver.current_url

        assert "view_cart" in actual_url.lower(), \
            f"Unexpected URL: '{actual_url}'"

    def click_proceed_to_checkout_button(self):
        self.driver.find_element(*self.proceed_to_checkout_button).click()

    def click_register_login_button(self):
        current_url = self.driver.current_url
        ele = self.wait.until(expected_conditions.visibility_of_element_located(self.register_login_button))
        ele.click()

        self.wait.until(expected_conditions.url_changes(current_url))
        new_url = self.driver.current_url

        assert "login" in new_url.lower(), \
            f"Unexpected URL: '{new_url}'"

    def verify_cart_and_click_remove_button_corresponding_to_particular_product(self, added_products: list, expected_products: list[dict], data: dict):
        self.verify_cart(added_products, expected_products)
        self.delete_all_or_nth_product(data)

    def click_cart_delete_button(self, idx: int):
        product_index_delete_button = (By.XPATH, f"//tr[@id='product-{idx}']//td[@class='cart_delete']/a")
        self.aggressive_safe_click(*product_index_delete_button)

    def delete_all_or_nth_product(self, data: dict):
        assert set(data["remove_indexes"]).issubset(set(data["indexes"])), \
            f"Expected '{data['remove_indexes']}' to be a subset of '{data['indexes']}'"

        for rmv_idx in data["remove_indexes"]:
            print(f"🗑️ Deleting product-{rmv_idx} from cart...")
            self.click_cart_delete_button(rmv_idx)

    def verify_particular_product_is_removed(self, data: dict):
        failed_indexes = []

        for rmv_idx in data["remove_indexes"]:
            try:
                self.wait.until(expected_conditions.invisibility_of_element_located((By.XPATH, f"//tr[@id='product-{rmv_idx}']")))
                print(f"✅ Product-{rmv_idx} is removed from cart successfully.")
            except TimeoutException:
                print(f"❌ Product-{rmv_idx} is not removed from cart.")
                failed_indexes.append(rmv_idx)
        if failed_indexes:
            raise Exception(f"❌ Unable to remove the product: '{failed_indexes}', multiple retries failed.\n無法刪除商品: '{failed_indexes}'，多次重試失敗")