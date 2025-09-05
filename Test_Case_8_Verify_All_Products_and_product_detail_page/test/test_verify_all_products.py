import allure


@allure.feature("verify all products")
@allure.story("End to End Go to test verify all products page")
@allure.title("Test E2E Go to test verify all products page")
def test_verify_all_products_and_product_detail(pages):
    with allure.step("Step 1 ~ 3: Verify home page URL"):
        pages.home_page.verify_home_page_by_url()

    with allure.step("Step 4: Click on 'Products' button"):
        pages.home_page.click_products_button()

    with allure.step("Step 5: Verify user is navigated to ALL PRODUCTS page successfully"):
        pages.products_page.verify_all_products_page_url_and_text()

    with allure.step("Step 6: The products list is visible"):
        pages.products_page.check_product_list_is_visible()

    with allure.step("Step 7: Click on 'View Product' of first product"):
        pages.products_page.click_view_product_of_first_product()

    with allure.step("Step 8: User is landed to product detail page"):
        pages.product_detail_page.verify_product_detail_page_by_url()

    with allure.step("Step 9: Verify that detail detail is visible: product name, category, price, availability, condition, brand"):
        pages.product_detail_page.verify_product_details_are_visible()