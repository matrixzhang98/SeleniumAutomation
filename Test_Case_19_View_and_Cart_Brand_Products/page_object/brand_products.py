from selenium.webdriver.common.by import By
from SeleniumAutomation.page_object.products_page import ProductsPage
from SeleniumAutomation.browser_utils.browser_utils import BrowserUtils


class BrandProducts(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.products_page = ProductsPage(driver)
        self.products_card = (By.XPATH, "//div[@class='product-image-wrapper']")

    def verify_brand_page_by_url(self):
        url = self.driver.current_url
        assert "brand_products" in url

    def verify_brand_page_by_url_and_brand_name(self, brand_name_str: str):
        url = self.driver.current_url
        assert "brand_products" in url and brand_name_str in url

    def verify_brand_page_products(self):
        self.products_page.check_product_list_is_visible()

    def verify_brand_page_and_products(self, brand_name: str):
        self.verify_brand_page_by_url_and_brand_name(brand_name)
        self.verify_brand_page_products()