from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from SeleniumAutomation.browser_utils.browser_utils import BrowserUtils


class ProductDetailPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.product_name = (By.XPATH, "//div[@class='product-information']/h2")
        self.category = (By.XPATH, "//div[@class='product-information']/p[1]")
        self.price = (By.XPATH, "//div[@class='product-information']//span/span")
        self.availability = (By.XPATH, "//p/b[text()='Availability:']/parent::p")
        self.condition = (By.XPATH, "//p/b[text()='Condition:']/parent::p")
        self.brand = (By.XPATH, "//p/b[text()='Brand:']/parent::p")
        self.quantity_input = (By.XPATH, "//input[@id='quantity']")
        self.add_to_cart_button = (By.XPATH, "//button[@type='button']")
        self.write_your_review_text = (By.XPATH, "//a[text()='Write Your Review']")

        self.review_name = (By.XPATH, "//input[@id='name']")
        self.review_email = (By.XPATH, "//input[@id='email']")
        self.review_text = (By.XPATH, "//textarea[@id='review']")
        self.submit_review_button = (By.XPATH, "//button[@id='button-review']")
        self.review_success_message = (By.XPATH, "//span[text()='Thank you for your review.']")
        self.added_products = []

    def verify_product_detail_page_by_url(self):
        actual_url = self.driver.current_url
        assert "product_details" in actual_url.lower(), \
            f"Unexpected URL: {actual_url}"

    def verify_write_your_review_text_is_visible(self):
        write_your_review_text = self.wait.until(expected_conditions.visibility_of_element_located(self.write_your_review_text))
        assert write_your_review_text.is_displayed(), "Write Your Review text is not visible"

    def verify_success_message_is_visible(self):
        success_message = self.wait.until(expected_conditions.visibility_of_element_located(self.review_success_message))
        assert success_message.is_displayed(), "Success message is not visible"

    def verify_product_details_are_visible(self):
        element = {
            "product_name": self.product_name,
            "category": self.category,
            "price": self.price,
            "availability": self.availability,
            "condition": self.condition,
            "brand": self.brand
        }

        for label, locator in element.items():
            el = self.wait.until(expected_conditions.visibility_of_element_located(locator))
            text = el.text.strip()
            assert text != "", f"{label} text is empty"
            print(f"{label} verified: {text}")

    def verify_category_is_related_to_keywords(self, keywords: str):
        category_element = self.driver.find_element(*self.category)
        category = category_element.text
        assert keywords.lower() in category.lower(), \
            f"expected '{keywords}', but got '{category}'"

    def increase_quantity(self, quantity: int):
        quantity_input = self.driver.find_element(*self.quantity_input)
        quantity_input.clear()
        quantity_input.send_keys(str(quantity))

        '''
            .clear() + .send_keys("4") 是常見在 Selenium 裡操作輸入框的做法，原因是：

            send_keys() 是模擬鍵盤輸入，傳入的參數必須是字串（string），因為它本質上是把字串「打」進去輸入框。
            
            即使你想輸入數字 4，也必須轉成字串 "4"，不能直接傳入整數 4，否則會報錯。
            
            所以用字串 "4" 是 Selenium 規定的用法，才能正常模擬輸入這個數字。這很正常，也符合 Selenium API 的設計
        '''

    def click_add_to_cart(self):
        self.driver.find_element(*self.add_to_cart_button).click()

    def click_add_to_cart_and_return_product_info(self) -> dict:
        name = self.driver.find_element(*self.product_name).text
        category = self.driver.find_element(*self.category).text
        price = self.driver.find_element(*self.price).text
        availability = self.driver.find_element(*self.availability).text
        condition = self.driver.find_element(*self.condition).text
        brand = self.driver.find_element(*self.brand).text
        quantity = self.driver.find_element(*self.quantity_input).get_attribute("value")

        product_info = {
            "name": name,
            "category": category,
            "price": price,
            "availability": availability,
            "condition": condition,
            "brand": brand,
            "quantity": quantity,
        }

        self.driver.find_element(*self.add_to_cart_button).click()
        return product_info

    def enter_review_info(self, data: dict):
        self.driver.find_element(*self.review_name).send_keys(data["name"])
        self.driver.find_element(*self.review_email).send_keys(data["email"])
        self.driver.find_element(*self.review_text).send_keys(data["review_text"])

    def click_review_submit_button(self):
        self.safe_click(*self.submit_review_button)