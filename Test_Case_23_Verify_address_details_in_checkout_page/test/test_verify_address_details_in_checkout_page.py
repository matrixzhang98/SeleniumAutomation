import json
import os.path
import pytest
import allure
from SeleniumAutomation.config import config


test_data_path = os.path.abspath(config.TEST_CASE_23_ADDRESS_DETAILS_DATA)

with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

@allure.feature("Verify address details in checkout page")
@allure.story("End to End verify address details in checkout page")
@allure.title("Test E2E verify address details in checkout page")
@pytest.mark.parametrize("test_data_list", test_list)
def test_verify_address_details_in_checkout_page(pages, test_data_list):
    with allure.step("Step 1 ~ 3: Verify home page URL"):
        pages.home_page.verify_home_page_by_url()

    with allure.step("Step 4: Click 'Signup / Login' button"):
        pages.home_page.click_signup_login_button()

    with allure.step("Step 5: Fill all details in Signup and create account"):
        pages.signup_login.full_register_process(test_data_list)

    with allure.step("Step 6: Verify 'ACCOUNT CREATED!' and click 'Continue' button"):
        pages.account_created.verify_account_created_text_and_click_continue_button()

    with allure.step("Step 7: Verify ' Logged in as username' at top"):
        pages.created_account_logged.verify_logged_in_as(test_data_list)

    with allure.step("Step 8: Add products to cart"):
        pages.products_page.add_multiple_products_to_cart_by_index(test_data_list["indexes"])

    with allure.step("Step 9: Click 'Cart' button"):
        pages.home_page.click_cart_button()

    with allure.step("Step 10: Verify that cart page is displayed"):
        pages.cart_page.verify_cart_page_by_url()

    with allure.step("Step 11: Click Proceed To Checkout"):
        pages.cart_page.click_proceed_to_checkout_button()

    with allure.step("Step 12: Verify that the delivery address is same address filled at the time registration of account"):
        pages.checkout.verify_delivery_address(test_data_list)

    with allure.step("Step 13: Verify that the billing address is same address filled at the time registration of account"):
        pages.checkout.verify_billing_address(test_data_list)

    with allure.step("Step 14: Click 'Delete Account' button"):
        pages.created_account_logged.click_delete_account_button()

    with allure.step("Step 15: Verify 'ACCOUNT DELETED!' and click 'Continue' button"):
        pages.deleted_account.verify_deleted_account_text_and_click_continue_button()