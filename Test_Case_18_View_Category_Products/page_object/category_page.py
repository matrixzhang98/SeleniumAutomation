from selenium.webdriver.common.by import By
from SeleniumAutomation.browser_utils.browser_utils import BrowserUtils


class CategoryPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.title_text = (By.XPATH, "//h2[@class='title text-center']")

    def verify_title_text(self, data: dict):
        title = self.driver.find_element(*self.title_text).text
        assert data["category"].upper() in title and data["subcategory"].upper() in title

    def verify_category_page_by_url(self):
        cur_url = self.driver.current_url
        assert "category_products" in cur_url
