import json
import pytest
import allure
import os.path
from SeleniumAutomation.config import config


test_data_path = os.path.abspath(config.TEST_CASE_3_INCORRECT_USER_DATA)

with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

@allure.feature("Login User with incorrect email and password")
@allure.story("End to End Login with incorrect info Flow")
@allure.title("Test E2E Login with incorrect info for {test_data_list[name]}")
@pytest.mark.parametrize("test_data_list", test_list)
def test_incorrect_user_info(pages, test_data_list):
    # 改成一行呼叫封裝方法
    pages.home_page.navigate_to_login_page_and_verify_text()

    with allure.step("Step 6: Enter incorrect email address and password"):
        pages.signup_login.fill_incorrect_login_info(test_data_list)

    with allure.step("Step 7: Click 'login' button"):
        pages.signup_login.click_login_button()

    with allure.step("Step 8: Verify error 'Your email or password is incorrect!' is visible"):
        pages.login_incorrect_info.verify_incorrect_info()