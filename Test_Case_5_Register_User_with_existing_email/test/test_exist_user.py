import json
import pytest
import allure
import os.path
from SeleniumAutomation.config import config


test_data_path = os.path.abspath(config.TEST_CASE_5_EXIST_USER_DATA)

with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

@allure.feature("Logout with exist email and password")
@allure.story("End to End Login exist user")
@allure.title("Test E2E Login exist user {test_data_list[name]}")
@pytest.mark.parametrize("test_data_list", test_list)
def test_exist_user(pages, test_data_list):
    pages.home_page.navigate_to_login_page_and_verify_text()

    with allure.step("Step 6: Enter name and already registered email address"):
        pages.signup_login.fill_signup_page(test_data_list)

    with allure.step("Step 7: Click 'Signup' button"):
        pages.signup_login.click_signup_button()

    with allure.step("Step 8: Verify error 'Email Address already exist!' is visible"):
        pages.signup_login.account_exist_text()
