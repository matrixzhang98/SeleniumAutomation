import json
import allure
import os.path
from SeleniumAutomation.config import config


test_data_path = os.path.abspath(config.TEST_CASE_18_VIEW_CATEGORY_PRODUCTS_DATA)

with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

@allure.feature("test view category products")
@allure.story("End to End test view category products")
@allure.title("Test E2E view category products")
def test_view_category_products(pages):
    with allure.step("Step 1 ~ 3: Verify home page URL"):
        pages.home_page.verify_home_page_by_url()

    with allure.step("Step 4: Click on 'Women' category"):
        pages.home_page.click_category_link(test_list[1])

    with allure.step("Step 5: Click on any category link under 'Women' category, for example: Dress"):
        pages.home_page.click_subcategory_link(test_list[1])

    with allure.step("Step 6: Verify that category page is displayed and confirm text 'WOMEN - TOPS PRODUCTS'"):
        pages.category_page.verify_title_text(test_list[1])

    with allure.step("Step 7: On left side bar, click on any sub-category link of 'Men' category"):
        pages.home_page.click_category_and_subcategory_link(test_list[3])

    with allure.step("Step 8: Verify that user is navigated to that category page"):
        pages.category_page.verify_category_page_by_url()