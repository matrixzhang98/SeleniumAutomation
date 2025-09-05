from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from SeleniumAutomation.browser_utils.browser_utils import BrowserUtils
from SeleniumAutomation.page_objects.product_detail_page import ProductDetailPage


class ProductsPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.all_products_text = (By.XPATH, "//h2[text()='All Products']")
        self.products_card = (By.XPATH, "//div[@class='product-image-wrapper']")
        # 有加.是相對 XPath，必須配合一個元素使用
        self.view_product_button = (By.XPATH, ".//a[text()='View Product']")
        self.search_product = (By.XPATH, "//input[@id='search_product']")
        self.search_product_button = (By.XPATH, "//button[@id='submit_search']")
        self.search_product_page_text = (By.XPATH, "//h2[text()='Searched Products']")
        self.search_result_list = (By.XPATH, "//div[@class='product-image-wrapper']")

        self.product_name = (By.XPATH, ".//div[@class='productinfo text-center']/p")
        self.product_price = (By.XPATH, ".//div[@class='productinfo text-center']/h2")
        self.view_the_product = (By.XPATH, ".//a[text()='View Product']")

        self.continue_button = (By.XPATH, "//button[text()='Continue Shopping']")
        self.view_cart_button = (By.XPATH, "//u[text()='View Cart']")
        self.added_products = []

    def verify_all_products_page_by_url(self):
        actual_url = self.driver.current_url

        assert "products" in actual_url.lower(), \
            f"Unexpected URL: {actual_url}"

    def verify_all_products_page_text(self):
        expected_text = "ALL PRODUCTS"
        element = self.driver.find_element(*self.all_products_text)
        actual_text = element.text

        assert actual_text == expected_text, \
            f"Expected '{expected_text}', but got '{actual_text}'"

    def check_product_list_is_visible(self):
        products_list = self.driver.find_elements(*self.products_card)
        print(len(products_list))
        assert len(products_list) > 0, \
            f"Expected at least one product list to be visible"

    def click_view_product_of_first_product(self):
        product_cards = self.driver.find_elements(*self.products_card)
        assert product_cards, "No product cards found."

        self.remove_ads_iframe()
        first_card = product_cards[0]
        view_button = first_card.find_element(*self.view_product_button)
        view_button.click()

    def click_view_product_of_nth_product(self, index: int):
        product_cards = self.driver.find_elements(*self.products_card)
        assert product_cards, "No product cards found."

        self.remove_ads_iframe()
        nth_card = product_cards[index - 1]

        # 先讓元素滑動到可視範圍內
        self.scroll_element_into_view(nth_card)
        view_button = nth_card.find_element(*self.view_product_button)
        view_button.click()

    def enter_product_name_in_search_box_and_submit(self, data: dict):
        self.driver.find_element(*self.search_product).send_keys(data["product_name"])
        self.driver.find_element(*self.search_product_button).click()

    def verify_search_product_page_text(self):
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(expected_conditions.visibility_of_element_located(self.search_product_page_text))

        expected_text = "SEARCHED PRODUCTS"
        actual_text = element.text
        assert actual_text == expected_text, \
            f"Expected '{expected_text}', but got '{actual_text}'"

    # 檢查查詢結果是否符合查詢的關鍵字
    def verify_product_list_is_related_to_search(self, keywords: str):
        self.verify_search_product_page_text()
        result_list_card = self.driver.find_elements(*self.search_result_list)
        total_product = len(self.driver.find_elements(*self.search_result_list))

        assert len(result_list_card) > 0, f"Expected at least one product list to be visible"

        pdp = ProductDetailPage(self.driver)
        for i in range(total_product):
            current_list_card = self.driver.find_elements(*self.search_result_list)
            product = current_list_card[i]
            product_name = product.find_element(*self.product_name).text

            if keywords.lower() not in product_name.lower():
                self.remove_ads_iframe()

                product.find_element(*self.view_the_product).click()
                pdp.verify_category_is_related_to_keywords(keywords)

                self.driver.back()
                wait = WebDriverWait(self.driver, 3)
                wait.until(expected_conditions.visibility_of_element_located(self.search_product_page_text))

    def hover_the_nth_product_and_click_add_to_cart(self, index: int):
        product_card_in_page = self.driver.find_elements(*self.search_result_list)

        assert len(product_card_in_page) > index, \
            f"Only {len(product_card_in_page)} products found, but index {index} requested."

        product_to_hover = product_card_in_page[index - 1]
        self.remove_ads_iframe()
        self.scroll_element_into_view(product_to_hover)

        actions = ActionChains(self.driver)
        actions.move_to_element(product_to_hover).perform()

        product_name = product_to_hover.find_element(*self.product_name).text
        product_price = product_to_hover.find_element(*self.product_price).text

        # hover後才會渲染的html結構，必須選取他
        overlay_button_locator = (
            By.XPATH,
            f".//div[@class='product-overlay']//a[@data-product-id='{index}']"
        )

        wait = WebDriverWait(product_to_hover, 3)
        add_to_cart = wait.until(
            expected_conditions.visibility_of_element_located(overlay_button_locator)
        )

        self.remove_ads_iframe()
        add_to_cart.click()

        product_info =  {
            "index": index,
            "name": product_name,
            "price": product_price
        }

        self.added_products.append(product_info)
        return product_info

    def get_expected_cart_summary(self) -> list[dict]:
        # 一個用來統整加入購物車商品的字典，用途是幫你處理「相同商品被加入多次」
        summary = {}
        for product in self.added_products:
            key = (product["name"], product["price"])
            if key in summary:
                summary[key]["quantity"] += 1
            else:
                summary[key] = {
                    "name": product["name"],
                    "price": product["price"],
                    "quantity": 1
                }
        return list(summary.values())

    def click_continue_shopping_button(self):
        wait = WebDriverWait(self.driver, 3)
        button = wait.until(expected_conditions.element_to_be_clickable(self.continue_button))
        button.click()

    def click_view_cart_button(self):
        wait = WebDriverWait(self.driver, 3)
        button = wait.until(expected_conditions.element_to_be_clickable(self.view_cart_button))
        button.click()

    def add_multiple_products_to_cart(self, indexes: list[int]) -> tuple[list[dict], list[dict]]:
        added = []
        for idx in indexes:
            product = self.hover_the_nth_product_and_click_add_to_cart(idx)
            added.append(product)
            self.click_continue_shopping_button()
        # 雖然根據test case 14的要求要按下"Cart"的按鈕但是其實點擊view cart導覽到的還是同一個畫面
        # self.click_view_cart_button()
        expected_summary = self.get_expected_cart_summary()
        return added, expected_summary