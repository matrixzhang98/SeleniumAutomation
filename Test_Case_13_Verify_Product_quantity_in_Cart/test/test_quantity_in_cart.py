import allure


@allure.feature("products quantity in cart")
@allure.story("End to End add products quantity in cart")
@allure.title("Test E2E products quantity in cart")
def test_products_quantity_in_cart(pages):
    added_products = []

    with allure.step("Step 1 ~ 3: Verify home page URL"):
        pages.home_page.verify_home_page_by_url()
        pages.home_page.click_products_button()

    with allure.step("Step 4: Click 'View Product' for any product on home page"):
        pages.products_page.click_view_product_of_nth_product(7)

    with allure.step("Step 5: Verify product detail is opened"):
        pages.product_detail_page.verify_product_detail_page_by_url()

    with allure.step("Step 6: Increase quantity to 4"):
        pages.product_detail_page.increase_quantity(4)

    with allure.step("Step 7: Click 'Add to cart' button"):
        product = pages.product_detail_page.click_add_to_cart_and_return_product_info()
        expected = pages.products_page.get_expected_cart_summary()
        added_products.append(product)

    with allure.step("Step 8: Click 'View Cart' button"):
        pages.products_page.click_view_cart_button()

    with allure.step("Step 9: Verify that product is displayed in cart page with exact quantity"):
        pages.cart_page.verify_products_added_correctly_in_cart(added_products)
        pages.cart_page.verify_carts_details_info(expected)