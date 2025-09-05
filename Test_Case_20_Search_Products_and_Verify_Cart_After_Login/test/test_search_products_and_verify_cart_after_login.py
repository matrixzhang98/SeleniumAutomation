import json
import pytest
import allure
import os.path
from SeleniumAutomation.config import config


test_data_path = os.path.abspath(config.TEST_CASE_20_SEARCH_PRODUCTS_AND_VERIFY_CART_AFTER_LOGIN_DATA)

with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

@allure.feature("search products and verify cart after login")
@allure.story("End to End search products and verify cart after login")
@allure.title("Test E2E search products and verify cart after login")
@pytest.mark.parametrize("test_data_list", test_list)
def test_search_products_and_verify_cart_after_login(pages, test_data_list):
    with allure.step("Step 1 ~ 2: Verify home page URL"):
        pages.home_page.verify_home_page_by_url()

    with allure.step("Step 3: Click on 'Products' button"):
        pages.home_page.click_products_button()

    with allure.step("Step 4: Verify user is navigated to ALL PRODUCTS page successfully"):
        pages.products_page.verify_all_products_page_url_and_text()

    with allure.step("Step 5: Enter product name in search input and click search button"):
        pages.products_page.enter_product_name_in_search_box_and_submit(test_data_list)

    with allure.step("Step 6: Verify 'SEARCHED PRODUCTS' is visible"):
        pages.products_page.verify_search_product_page_text()

    with allure.step("Step 7: Verify all the products related to search are visible"):
        pages.products_page.verify_product_list_is_related_to_search(test_data_list["product_name"])

    with allure.step("Step 8: Add those products to cart"):
        added_products, expected = pages.products_page.add_all_searched_products_to_cart()

    with allure.step("Step 9: Click 'Cart' button and verify that products are visible in cart"):
        pages.products_page.click_cart_button_and_verify_products_are_visible(added_products, expected)

    with allure.step("Step 10: Click 'Signup / Login' button and submit login details"):
        pages.home_page.click_signup_login_button()
        pages.signup_login.full_login_process(test_data_list)

    with allure.step("Step 11: Again, go to Cart page"):
        pages.home_page.click_cart_button()

    with allure.step("Step 12: Verify that those products are visible in cart after login as well"):
        pages.cart_page.verify_cart(added_products, expected)