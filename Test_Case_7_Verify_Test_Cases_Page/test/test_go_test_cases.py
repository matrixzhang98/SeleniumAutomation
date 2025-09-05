import allure

@allure.feature("Go to test cases page")
@allure.story("End to End Go to test cases page")
@allure.title("Test E2E Go to test cases page")
def test_go_to_test_cases(pages):
    with allure.step("Step 1 ~ 3: Verify home page URL"):
        pages.home_page.verify_home_page_by_url()

    with allure.step("Step 4: Click on 'Test Cases' button"):
        pages.home_page.click_test_cases_button()

    with allure.step("Step 5: Verify user is navigated to test cases page successfully"):
        pages.go_test_cases.verify_test_cases_page_by_url()