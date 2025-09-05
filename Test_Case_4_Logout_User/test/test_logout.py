import json
import pytest
import allure
import os.path
from SeleniumAutomation.config import config


test_data_path = os.path.abspath(config.TEST_CASE_4_CORRECT_USER_DATA)

with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

@allure.feature("Logout with correct email and password")
@allure.story("End to End Logout user")
@allure.title("Test E2E Logout user {test_data_list[name]}")
@pytest.mark.parametrize("test_data_list", test_list)
def test_logout(pages, test_data_list):
    pages.home_page.navigate_to_login_page_and_verify_text()

    with allure.step("Step 6: Enter correct email address and password"):
        pages.signup_login.fill_login_page(test_data_list)

    with allure.step("Step 7: Click 'login' button"):
        pages.signup_login.click_login_button()

    with allure.step("Step 8: Verify that 'Logged in as username' is visible"):
        pages.created_account_logged.verify_logged_in_as(test_data_list)

    with allure.step("Step 9: Click 'Logout' button"):
        pages.signup_login.click_logout_button()

    with allure.step("Step 10: Verify that user is navigated to login page"):
        pages.home_page.click_home_button()
        pages.home_page.verify_home_page_by_url()