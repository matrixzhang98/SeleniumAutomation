import json
import pytest
import allure
import os.path
from SeleniumAutomation.config import config


test_data_path = os.path.abspath(config.TEST_CASE_16_LOGIN_BEFORE_CHECKOUT_DATA)

with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

@allure.feature("place order login before checkout")
@allure.story("End to End place order login before checkout")
@allure.title("Test E2E place order login before checkout")
@pytest.mark.parametrize("test_data_list", test_list)
def test_place_order_login_before_checkout(pages, test_data_list):
    with allure.step("Step 1 ~ 3: Verify home page URL"):
        pages.home_page.verify_home_page_by_url()

    with allure.step("Step 4: Click 'Signup / Login' button"):
        pages.home_page.click_signup_login_button()

    with allure.step("Step 5: Fill email, password and click 'Login' button"):
        pages.signup_login.full_login_process(test_data_list)

    with allure.step("Step 6: Verify 'Logged in as username' at top"):
        pages.created_account_logged.verify_logged_in_as(test_data_list)

    with allure.step("Step 7: Add products to cart"):
        added_products, expected = \
            pages.products_page.add_multiple_products_to_cart_by_index(test_data_list["indexes"])

    with allure.step("Step 8: Click 'Cart' button"):
        pages.home_page.click_cart_button()

    with allure.step("Step 9: Verify that cart page is displayed"):
        pages.cart_page.verify_cart_page_by_url()

    with allure.step("Step 10: Click Proceed To Checkout"):
        pages.cart_page.click_proceed_to_checkout_button()

    with allure.step("Step 11: Verify Address Details and Review Your Order"):
        pages.checkout.verify_all_addresses(test_data_list)
        pages.cart_page.verify_cart(added_products, expected)

    with allure.step("Step 12: Enter description in comment text area and click 'Place Order'"):
        pages.checkout.enter_comment_and_click_place_order_button(test_data_list)

    with allure.step("Step 13: Enter payment details: Name on Card, Card Number, CVC, Expiration date"):
        pages.payment.enter_payment_details(test_data_list)

    with allure.step("Step 14: Click 'Pay and Confirm Order' button"):
        pages.payment.click_pay_and_confirm_order_button()

    with allure.step("Step 15: Verify success message 'Your order has been placed successfully!'"):
        pages.payment.verify_place_order_and_contact_success_message()

    with allure.step("Step 16: Click 'Delete Account' button"):
        pages.created_account_logged.click_delete_account_button()

    with allure.step("Step 17: Verify 'ACCOUNT DELETED!' and click 'Continue' button"):
        pages.deleted_account.verify_deleted_account_text_and_click_continue_button()