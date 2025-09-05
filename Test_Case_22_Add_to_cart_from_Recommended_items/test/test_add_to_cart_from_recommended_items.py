import json
import pytest
import allure
import os.path
from SeleniumAutomation.config import config


test_data_path = os.path.abspath(config.TEST_CASE_22_CAROUSEL_PRODUCT_DATA)

with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

@allure.feature("test add review on product")
@allure.story("End to End add review on product")
@allure.title("Test E2E add review on product")
@pytest.mark.parametrize("test_data_list", test_list)
def test_add_review_on_product(pages, test_data_list):
    with allure.step("Step 1 ~ 2: Verify home page URL"):
        pages.home_page.verify_home_page_by_url()

    with allure.step("Step 3: Scroll to bottom of page"):
        pages.home_page.scroll_down_to_footer()

    with allure.step("Step 4: Verify 'RECOMMENDED ITEMS' are visible"):
        pages.products_page.verify_recommended_items_text()

    with allure.step("Step 5: Click on 'Add To Cart' on Recommended product"):
        added_products, expected = pages.products_page.add_carousel_product_to_cart_by_id(test_data_list["carousel_id"])

    with allure.step("Step 6: Click on 'View Cart' button"):
        pages.home_page.click_cart_button()

    with allure.step("Step 7: Verify that product is displayed in cart page"):
        pages.cart_page.verify_carousel_cart(added_products, expected)