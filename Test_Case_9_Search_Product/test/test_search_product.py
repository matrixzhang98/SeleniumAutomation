import json
import allure
import pytest
import os.path
from SeleniumAutomation.config import config


test_data_path = os.path.abspath(config.TEST_CASE_9_SEARCH_PRODUCT_DATA)

with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

@allure.feature("search product")
@allure.story("End to End search product")
@allure.title("Test E2E search product")
@pytest.mark.parametrize("test_data_list", test_list)
def test_search_product(pages, test_data_list):
    with allure.step("Step 1 ~ 3: Verify home page URL"):
        pages.home_page.verify_home_page_by_url()

    with allure.step("Step 4: Click on 'Products' button"):
        pages.home_page.click_products_button()

    with allure.step("Step 5: Verify user is navigated to ALL PRODUCTS page successfully"):
        pages.products_page.verify_all_products_page_url_and_text()

    with allure.step("Step 6: Enter product name in search input and click search button"):
        pages.products_page.enter_product_name_in_search_box_and_submit(test_data_list)

    with allure.step("Step 7: Verify 'SEARCHED PRODUCTS' is visible"):
        pages.products_page.verify_search_product_page_text()

    with allure.step("Step 8: Verify all the products related to search are visible"):
        pages.products_page.verify_product_list_is_related_to_search(test_data_list["product_name"])