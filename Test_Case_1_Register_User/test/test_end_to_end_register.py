import json
import os.path
import pytest
import allure
from SeleniumAutomation.config import config


test_data_path = os.path.abspath(config.TEST_CASE_1_REGISTER_DATA_PATH)

with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

@allure.feature("User Registration")
@allure.story("End to End Registration Flow")
@allure.title("Test E2E Registration for {test_data_list[name]}")
@pytest.mark.parametrize("test_data_list", test_list)
def test_end_to_end_register(pages, test_data_list):
    with allure.step("Step 1 ~ 3: Verify home page URL"):
        pages.home_page.verify_home_page_by_url()

    with allure.step("Step 4: Click on 'SignupLogin / Login' button"):
        pages.home_page.click_signup_login_button()

    with allure.step("Step 5: Verify 'New User SignupLogin!' is visible"):
        pages.signup_login.verify_new_user_signup_text()

    with allure.step("Step 6: Enter name and email address"):
        pages.signup_login.fill_signup_page(test_data_list)

    with allure.step("Step 7: Click 'SignupLogin' button"):
        pages.signup_login.click_signup_button()

    with allure.step("Step 8: Verify 'ENTER ACCOUNT INFORMATION' is visible"):
        pages.register.verify_enter_text()

    with allure.step("Step 9: Fill account information"):
        pages.register.fill_account_information(test_data_list)

    with allure.step("Step 10: Select newsletter checkbox"):
        pages.register.select_account_newsletter(test_data_list)

    with allure.step("Step 11: Select special offers checkbox"):
        pages.register.select_account_special_offers(test_data_list)

    with allure.step("Step 12: Fill address information"):
        pages.register.fill_address_information(test_data_list)

    with allure.step("Step 13: Click 'Create Account' button"):
        pages.register.click_create_account_button()

    with allure.step("Step 14: Verify that 'ACCOUNT CREATED!' is visible"):
        pages.account_created.verify_account_created_text()

    with allure.step("Step 15: Click 'Continue' button"):
        pages.account_created.click_create_account_continue_button()

    with allure.step("Step 16: Verify that 'Logged in as username' is visible"):
        pages.created_account_logged.verify_logged_in_as(test_data_list)

    with allure.step("Step 17: Click 'Delete Account' button"):
        pages.created_account_logged.click_delete_account_button()

    with allure.step("Step 18: Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button"):
        pages.deleted_account.verify_deleted_account_text_and_click_continue_button()