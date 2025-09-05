import time
import json
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from SeleniumAutomation.page_object.cart_page import CartPage
from SeleniumAutomation.page_object.home_page import HomePage
from SeleniumAutomation.browser_utils.browser_utils import BrowserUtils
from SeleniumAutomation.page_object.product_detail_page import ProductDetailPage


class ProductsPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        self.home_page = HomePage(driver)
        self.cart_page = CartPage(driver)
        self.product_detail_page = ProductDetailPage(driver)
        self.all_products_text = (By.XPATH, "//h2[text()='All Products']")
        self.products_card = (By.XPATH, "//div[@class='product-image-wrapper']")
        # 有加.是相對 XPath，必須配合一個元素使用
        self.view_product_button = (By.XPATH, ".//a[text()='View Product']")
        self.search_product = (By.XPATH, "//input[@id='search_product']")
        self.search_product_button = (By.XPATH, "//button[@id='submit_search']")
        self.search_product_page_text = (By.XPATH, "//h2[text()='Searched Products']")
        self.product_name = (By.XPATH, ".//div[@class='productinfo text-center']/p")
        self.product_price = (By.XPATH, ".//div[@class='productinfo text-center']/h2")
        self.view_the_product = (By.XPATH, ".//a[text()='View Product']")
        self.continue_button = (By.XPATH, "//button[text()='Continue Shopping']")
        self.view_cart_button = (By.XPATH, "//u[text()='View Cart']")
        self.searched_product_hovered_id = (By.XPATH, ".//div[@class='product-overlay']//a[@data-product-id]")
        self.add_to_cart_button = (By.XPATH, ".//a[@class='btn btn-default add-to-cart']")
        # carousel
        self.recommended_items_text = (By.XPATH, "//h2[text()='recommended items']")
        self.recommended_items = (By.XPATH, "//div[@class='recommended_items']")
        self.carousel_product_card = (By.XPATH, "//div[@class='carousel-inner']//div[@class='product-image-wrapper']")
        self.carousel_right_arrow = (By.XPATH, "//a[@class='right recommended-item-control' and @data-slide='next']")
        self.carousel_active = (By.CSS_SELECTOR, ".carousel-inner .item.active")
        self.added_products = []

    # 根據ID取得目標商品的加入按鈕
    @staticmethod
    def get_add_to_cart_button_by_pid(pid: int):
        return By.XPATH, f".//a[@class='btn btn-default add-to-cart' and @data-product-id='{pid}']"

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

    def verify_all_products_page_url_and_text(self):
        self.verify_all_products_page_by_url()
        self.verify_all_products_page_text()

    def check_product_list_is_visible(self):
        products_list = self.driver.find_elements(*self.products_card)
        print("products list of len: ", len(products_list))

        assert len(products_list) > 0, \
            f"Expected at least one product list to be visible"

    def click_view_product_of_first_product(self):
        product_cards = self.driver.find_elements(*self.products_card)

        assert product_cards, "No product cards found."

        first_card = product_cards[0]
        self.safe_click(*self.view_product_button, context=first_card)

    # 點擊第n個商品的view product
    def click_view_product_of_nth_product(self, index: int):
        product_cards = self.driver.find_elements(*self.products_card)

        assert product_cards, "No product cards found."

        nth_card = product_cards[index - 1]
        self.safe_click(*self.view_product_button, context=nth_card)

    def enter_product_name_in_search_box_and_submit(self, data: dict):
        self.driver.find_element(*self.search_product).send_keys(data["product_name"])
        self.driver.find_element(*self.search_product_button).click()

    def verify_search_product_page_text(self):
        element = self.wait.until(expected_conditions.visibility_of_element_located(self.search_product_page_text))
        expected_text = "SEARCHED PRODUCTS"
        actual_text = element.text

        assert actual_text == expected_text, \
            f"Expected '{expected_text}', but got '{actual_text}'"

    # 檢查查詢結果是否符合查詢的關鍵字
    def verify_product_list_is_related_to_search(self, keywords: str):
        self.verify_search_product_page_text()
        self.check_product_list_is_visible()

        total_product = len(self.driver.find_elements(*self.products_card))

        for i in range(total_product):
            current_list_card = self.driver.find_elements(*self.products_card)
            product = current_list_card[i]
            product_name = product.find_element(*self.product_name).text

            # 如果關鍵字不在商品名稱中，就進去詳細頁面找
            if keywords.lower() not in product_name.lower():
                self.safe_click(*self.view_the_product, context=product)
                self.product_detail_page.verify_category_is_related_to_keywords(keywords)
                self.driver.back()
                self.wait.until(expected_conditions.visibility_of_element_located(self.search_product_page_text))

    # 獲取所查詢商品的id
    def get_all_searched_product_id_in_page(self):
        elements = self.driver.find_elements(*self.searched_product_hovered_id)
        return [int(el.get_attribute("data-product-id")) for el in elements]

    # 將根據所查詢商品ID加入購物車
    def add_all_searched_products_to_cart(self):
        product_ids = self.get_all_searched_product_id_in_page()
        return self.add_multiple_products_to_cart_by_id(product_ids)

    def click_cart_button_and_verify_products_are_visible(self, added_products: list, expected_products: list[dict]):
        cart_element = self.driver.find_element(*self.home_page.cart_button)
        self.scroll_element_into_view(cart_element)
        self.home_page.click_cart_button()
        self.cart_page.verify_cart(added_products, expected_products)

    def verify_recommended_items_text(self):
        expected_text = "RECOMMENDED ITEMS"
        actual_text = self.driver.find_element(*self.recommended_items_text).text

        assert actual_text.lower().strip() == expected_text.lower().strip(), \
            f"Expected '{expected_text}', but got '{actual_text}'"

    def click_carousel_right_arrow(self):
        self.safe_click(*self.carousel_right_arrow)

    def click_continue_shopping_button(self):
        self.safe_click(*self.continue_button)

    def click_view_cart_button(self):
        self.safe_click(*self.view_cart_button)

    # By product index
    def hover_the_nth_product_and_click_add_to_cart(self, index: int):
        product_card_in_page = self.driver.find_elements(*self.products_card)

        self.check_product_list_is_visible()

        assert len(product_card_in_page) > index, \
            f"Only '{len(product_card_in_page)}' products found, but index '{index}' requested."

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

        add_to_cart = self.wait.until(
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

    def add_nth_product_and_click_add_to_cart(self, p_id: int):
        self.remove_ads_iframe()

        # 這是list[WebElement]
        searched_products = self.driver.find_elements(*self.products_card)

        # 取得所有商品的id
        product_ids = self.get_all_searched_product_id_in_page()

        assert len(product_ids) > 0, "No product cards found."

        # 找出搜出商品的index，從1開始編排
        indexes = list(range(1, len(searched_products) + 1))

        target_product = None
        for i in indexes:
            # list的index從0開始
            product = searched_products[i - 1]
            try:
                # 找到此商品的非hover的加入購物車按鈕
                add_to_cart_btn = product.find_element(*self.add_to_cart_button)
                # 抓取此商品物件的data-product-id屬性
                product_id = int(add_to_cart_btn.get_attribute("data-product-id"))
                # 如果此商品的id和要加入購物車的id相同
                if product_id == p_id:
                    # 就將其賦值給target_product
                    target_product = product
                    break
            except NoSuchElementException:
                continue

        assert target_product is not None, f"Product with id '{p_id}' not found."

        product_name = target_product.find_element(*self.product_name).text
        product_price = target_product.find_element(*self.product_price).text

        self.scroll_element_into_view(target_product)

        locator = (
            By.XPATH,
            f"//div[@class='productinfo text-center']//a[@class='btn btn-default add-to-cart' and @data-product-id='{p_id}']"
        )

        add_to_cart_btn = target_product.find_element(*locator)
        add_to_cart_btn.click()

        product_info =  {
            "p_id": p_id,
            "name": product_name,
            "price": product_price
        }
        self.added_products.append(product_info)
        return product_info

    # 輪播區域的推薦商品
    def recommended_item(self, pid: int):
        target_product = None
        max_pages = 5

        for page in range(max_pages):
            self.wait.until(expected_conditions.presence_of_all_elements_located(self.carousel_product_card))
            product_cards = self.driver.find_elements(*self.carousel_product_card)
            print(f"Found '{len(product_cards)}' product cards on page '{page + 1}'")

            for index, product in enumerate(product_cards):
                try:
                    # Scroll the product into view
                    self.scroll_element_into_view(product)
                    time.sleep(0.5)  # Small delay for the scroll to complete

                    add_btn = product.find_element(*self.add_to_cart_button)
                    product_id = int(add_btn.get_attribute("data-product-id"))
                    print(f"Checking product ID: '{product_id}'")

                    if product_id == pid:
                        target_product = product
                        name_element = WebDriverWait(product, 5).until(
                            lambda el: el.find_element(*self.product_name)
                        )
                        product_name = name_element.get_attribute("textContent").strip()
                        print(f"Target product name: '{product_name}'")

                        '''
                            等同def find_product_name(el):
                                return el.find_element(*self.product_name)
                        '''

                        price_element = WebDriverWait(product, 5).until(
                            lambda el: el.find_element(*self.product_price)
                        )
                        product_price = price_element.get_attribute("textContent").strip()
                        print(f"Target product name: '{product_price}'")

                        self.click_element_by_js(add_btn)
                        print(f"Clicked add to cart for product ID: '{product_id}'")

                        carousel_product_info = {
                            "pid": pid,
                            "name": product_name,
                            "price": product_price
                        }

                        self.added_products.append(carousel_product_info)
                        return carousel_product_info

                except Exception as e:
                    print(f"Error processing product '{index}': {str(e)}")
                    continue

            if target_product:
                break

            # Click next page
            try:
                is_active = self.driver.find_element(*self.carousel_active)
                original_class = is_active.get_attribute("class")
                self.click_carousel_right_arrow()

                WebDriverWait(self.driver, 5).until(
                    lambda d: is_active.get_attribute("class") != original_class
                )
            except Exception as e:
                print(f"Error navigating carousel: {str(e)}")
                break
        assert False, f"Product with id {pid} not found."

    def get_expected_cart_summary(self) -> list[dict]:
        # 一個用來統整加入購物車商品的字典，用途是幫你處理「相同商品被加入多次」
        summary = {}

        try:
            print(f"[DEBUG] self.added_products = \n{json.dumps(self.added_products, indent=2, ensure_ascii=False)}")
        except TypeError:
            print(f"[DEBUG] self.added_products = {self.added_products}")

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

    def add_multiple_products_to_cart_by_id(self, ids: list[int]) -> tuple[list[dict], list[dict]]:
        products_id = []
        for pid in ids:
            product = self.add_nth_product_and_click_add_to_cart(pid)
            products_id.append(product)
            self.click_continue_shopping_button()

        expected_summary = self.get_expected_cart_summary()
        return products_id, expected_summary

    def add_multiple_products_to_cart_by_index(self, indexes: list[int]) -> tuple[list[dict], list[dict]]:
        is_added = []
        for idx in indexes:
            # 使用hover方法加入
            product = self.hover_the_nth_product_and_click_add_to_cart(idx)
            is_added.append(product)
            self.click_continue_shopping_button()

        expected_summary = self.get_expected_cart_summary()
        return is_added, expected_summary

    def add_carousel_product_to_cart_by_id(self, ids: list[int]):
        recommended_elem = self.driver.find_element(*self.recommended_items)
        self.scroll_element_into_view(recommended_elem)

        added_ids = []
        for pid in ids:
            product = self.recommended_item(pid)
            added_ids.append(product)  # 收集加到 cart 的項目
            self.click_continue_shopping_button()

        expected_summary = self.get_expected_cart_summary()
        print(f"[DEBUG] added_ids:\n{json.dumps(added_ids, indent=2, ensure_ascii=False)}")
        print(f"[DEBUG] expected_summary:\n{json.dumps(expected_summary, indent=2, ensure_ascii=False)}")

        return added_ids, expected_summary