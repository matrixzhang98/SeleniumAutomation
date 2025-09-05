import json
import pytest
import allure
import os.path
from SeleniumAutomation.config import config


test_data_path = os.path.abspath(config.TEST_CASE_17_REMOVE_PRODUCTS_FROM_CART_DATA)

with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

@allure.feature("test remove products from cart")
@allure.story("End to End test remove products from cart")
@allure.title("Test E2E remove products from cart")
@pytest.mark.parametrize("test_data_list", test_list)
def test_remove_products_from_cart(pages, test_data_list):
    with allure.step("Step 1 ~ 3: Verify home page URL"):
        pages.home_page.verify_home_page_by_url()

    with allure.step("Step 4: Add products to cart"):
        added_products, expected = \
            pages.products_page.add_multiple_products_to_cart_by_index(test_data_list["indexes"])

    with allure.step("Step 5: Click 'Cart' button"):
        pages.home_page.click_cart_button()

    with allure.step("Step 6: Verify that cart page is displayed"):
        pages.cart_page.verify_cart_page_by_url()

    with allure.step("Step 7: Click 'X' button corresponding to particular product"):
        pages.cart_page.verify_cart_and_click_remove_button_corresponding_to_particular_product(added_products, expected, test_data_list)

    with allure.step("Step 8: Verify that product is removed from the cart"):
        pages.cart_page.verify_particular_product_is_removed(test_data_list)