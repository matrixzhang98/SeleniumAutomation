import json
import os.path
import pytest
import allure
from SeleniumAutomation.config import config


test_data_path = os.path.abspath(config.TEST_CASE_2_USER_DATA_PATH)

with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

@allure.feature("Login User with correct email and password")
@allure.story("End to End Login with correct info Flow")
@allure.title("Test E2E Login with correct info for {test_data_list[name]}")
@pytest.mark.parametrize("test_data_list", test_list)
def test_login_with_correct_info(pages, test_data_list):
    with allure.step("Step 1 ~ 3: Verify home page URL"):
        pages.home_page.verify_home_page_by_url()

    with allure.step("Step 4: Click on 'Signup / Login' button"):
        pages.home_page.click_signup_login_button()

    with allure.step("Step 5: Verify 'Login to your account' is visible"):
        pages.signup_login.verify_login_page_text()

    with allure.step("Step 6: Enter correct email address and password"):
        pages.signup_login.fill_login_page(test_data_list)

    with allure.step("Step 7: Click 'login' button"):
        pages.signup_login.click_login_button()

    with allure.step("Step 8: Verify that 'Logged in as username' is visible"):
        pages.created_account_logged.verify_logged_in_as(test_data_list)

    with allure.step("Step 9: Click 'Delete Account' button"):
        pages.created_account_logged.click_delete_account_button()

    with allure.step("Step 10: Verify that 'ACCOUNT DELETED!' is visible"):
        pages.deleted_account.verify_deleted_account_text_and_click_continue_button()
