import json
import pytest
import allure
import os.path
from SeleniumAutomation.config import config


test_data_path = os.path.abspath(config.TEST_CASE_10_SUBSCRIPTION_HOME_PAGE_EMAIL)

with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

@allure.feature("subscription in home page")
@allure.story("End to End subscription in home page")
@allure.title("Test E2E subscription in home page")
@pytest.mark.parametrize("test_data_list", test_list)
def test_subscription_in_home_page(pages, test_data_list):
    with allure.step("Step 1 ~ 3: Verify home page URL"):
        pages.home_page.verify_home_page_by_url()

    with allure.step("Step 4: Scroll down to footer"):
        pages.home_page.scroll_down_to_footer()

    with allure.step("Step 5: Verify text 'SUBSCRIPTION'"):
        pages.home_page.verify_text_subscription()

    with allure.step("Step 6: Enter email address in input and click arrow button"):
        pages.home_page.enter_subscribe_email_and_submit(test_data_list)

    with allure.step("Step 7: Verify success message 'You have been successfully subscribed!' is visible"):
        pages.home_page.verify_success_subscribe_message()