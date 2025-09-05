import allure


@allure.feature("test view and cart brand products")
@allure.story("End to End view and cart brand products")
@allure.title("Test E2E view and cart brand products")
def test_view_and_cart_brand_products(pages):
    with allure.step("Step 1 ~ 3: Verify home page URL"):
        pages.home_page.verify_home_page_by_url()

    with allure.step("Step 4: Verify that Brands are visible on left side bar"):
        pages.home_page.verify_brands_text()

    with allure.step("Step 5: Click on any brand name"):
        brand1 = pages.home_page.click_any_brand_name("Polo")

    with allure.step("Step 6: Verify that user is navigated to brand page and brand products are displayed"):
        pages.brand_products.verify_brand_page_and_products(brand1)

    with allure.step("Step 7: On left side bar, click on any other brand link"):
        brand2 = pages.home_page.click_any_brand_name("H&M")

    with allure.step("Step 8: Verify that user is navigated to that brand page and can see products"):
        pages.brand_products.verify_brand_page_and_products(brand2)