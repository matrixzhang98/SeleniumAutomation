from SeleniumAutomation.browser_utils.browser_utils import BrowserUtils


class GoTestCases(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def verify_test_cases_page_by_url(self):
        expected_url = "https://www.automationexercise.com/test_cases"
        actual_url = self.driver.current_url

        assert "test_cases" in actual_url.lower(), \
            f"Unexpected URL: {actual_url}"

        assert actual_url == expected_url, \
            f"Expected URL '{expected_url}', but got '{actual_url}'"