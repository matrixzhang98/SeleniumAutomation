import json
import pytest
import allure
import os.path
from SeleniumAutomation.config import config


test_data_path = os.path.abspath(config.TEST_CASE_6_CONTACT_US_DATA)

with open(test_data_path, encoding="utf-8") as f:
    test_data = json.load(f)
    test_list = test_data["data"]

@allure.feature("Contact Us Form")
@allure.story("End to End Contact us")
@allure.title("Test E2E Contact us {test_data_list[name]}")
@pytest.mark.parametrize("test_data_list", test_list)
def test_contact_us(pages, test_data_list):
    with allure.step("Step 1 ~ 3: Verify home page URL"):
        pages.home_page.verify_home_page_by_url()

    with allure.step("Step 4: Click on 'Contact Us' button"):
        pages.home_page.click_contact_us()

    with allure.step("Step 5: Verify 'GET IN TOUCH' is visible"):
        pages.contact_us.verify_contact_us_info()

    with allure.step("Step 6: Enter name, email, subject and message"):
        pages.contact_us.fill_contact_us_form(test_data_list)

    with allure.step("Step 7: Upload file"):
        pages.contact_us.upload_file(test_data_list)

    with allure.step("Step 8: Click 'Submit' button"):
        pages.contact_us.click_submit_button()

    with allure.step("Step 9: Click OK button"):
        pages.contact_us.click_popup_accept()

    with allure.step("Step 10: Verify success message 'Success! Your details have been submitted successfully.' is visible"):
        pages.submit_contact_form.verify_submit_contact_success_message()

    with allure.step("Step 11: Click 'Home' button and verify that landed to home page successfully"):
        pages.home_page.click_home_button()
        pages.home_page.verify_home_page_by_url()