import allure


@allure.feature("add products in cart")
@allure.story("End to End add products in cart")
@allure.title("Test E2E add products in cart")
def test_add_products_in_cart(pages):
    added_products = []

    with allure.step("Step 1 ~ 3: Verify home page URL"):
        pages.home_page.verify_home_page_by_url()

    with allure.step("Step 4: Click 'Products' button"):
        pages.home_page.click_products_button()

    with allure.step("Step 5: Hover over first product and click 'Add to cart'"):
        product_1 = pages.products_page.hover_the_nth_product_and_click_add_to_cart(1)
        added_products.append(product_1)

    with allure.step("Step 6: Click 'Continue Shopping' button"):
        pages.products_page.click_continue_shopping_button()

    with allure.step("Step 7: Hover over second product and click 'Add to cart'"):
        product_2 = pages.products_page.hover_the_nth_product_and_click_add_to_cart(2)
        added_products.append(product_2)

    with allure.step("Step 8: Click 'View Cart' button"):
        pages.products_page.click_view_cart_button()

    with allure.step("Step 9: Verify both products are added to Cart"):
        # 預期會加入購物車的商品
        expected = pages.products_page.get_expected_cart_summary()
        # 驗證預期商品是否被正確加入
        pages.cart_page.verify_products_added_correctly_in_cart(added_products)

    with allure.step("Step 10: Verify their prices, quantity and total price"):
        # 驗證預期商品的價格、數量和總價
        pages.cart_page.verify_carts_details_info(expected)