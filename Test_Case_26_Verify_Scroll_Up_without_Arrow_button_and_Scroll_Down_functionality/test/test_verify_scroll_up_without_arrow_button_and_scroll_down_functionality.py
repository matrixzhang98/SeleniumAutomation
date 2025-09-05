import allure


@allure.feature("Verify scroll up without arrow button and scroll down functionality")
@allure.story("End to End verify scroll up without arrow button and scroll down functionality")
@allure.title("Test E2E verify scroll up without arrow button and scroll down functionality")
def test_verify_scroll_up_without_arrow_button_and_scroll_down_functionality(pages):
    with allure.step("Step 1 ~ 3: Verify home page URL"):
        pages.home_page.verify_home_page_by_url()

    with allure.step("Step 4: Scroll down page to bottom"):
        pages.home_page.scroll_down_to_footer()

    with allure.step("Step 5: Verify 'SUBSCRIPTION' is visible"):
        pages.home_page.verify_text_subscription()

    with allure.step("Step 6: Scroll up page to top"):
        pages.home_page.scroll_up_to_header()

    with allure.step("Step 7: Verify that page is scrolled up and 'Full-Fledged practice website for Automation Engineers' text is visible on screen"):
        pages.home_page.verify_pages_is_scrolled_up_and_carousel_text_is_visible()