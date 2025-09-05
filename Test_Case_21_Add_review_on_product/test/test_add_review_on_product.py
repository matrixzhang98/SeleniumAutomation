import json
import pytest
import allure
import os.path
from SeleniumAutomation.config import config


test_data_path = os.path.abspath(config.TEST_CASE_21_ADD_REVIEW_ON_PRODUCT_DATA)

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

    with allure.step("Step 3: Click on 'Products' button"):
        pages.home_page.click_products_button()

    with allure.step("Step 4: Verify user is navigated to ALL PRODUCTS page successfully"):
        pages.products_page.verify_all_products_page_url_and_text()

    with allure.step("Step 5: Click on 'View Product' button"):
        pages.products_page.click_view_product_of_nth_product(test_data_list["product_index"])

    with allure.step("Step 6: Verify 'Write Your Review' is visible"):
        pages.product_detail_page.verify_write_your_review_text_is_visible()

    with allure.step("Step 7: Enter name, email and review"):
        pages.product_detail_page.enter_review_info(test_data_list)

    with allure.step("Step 8: Click 'Submit' button"):
        pages.product_detail_page.click_review_submit_button()

    with allure.step("Step 9: Verify success message 'Thank you for your review.'"):
        pages.product_detail_page.verify_success_message_is_visible()