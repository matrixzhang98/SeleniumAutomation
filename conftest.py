import pytest
import os
import sys
from config import config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

def get_chromium_options(browser_name, headless):
    options = ChromeOptions()

    if browser_name == "brave":
        # ✅ Brave 執行檔路徑
        brave_path = config.BRAVE_PATH
        options.binary_location = brave_path

    # ✅ 關閉密碼儲存提示、關閉自動填寫、關閉通知
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.default_content_setting_values.notifications": 2,

        # ✅ 關閉自動填寫地址的提示
        "autofill.profile_enabled": False,
        "profile.autofill_profile_enabled": False
    }
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--disable-autofill-keyboard-accessory-view[8]")

    if headless:
        options.add_argument("--headless=new")  # 🆕 這是新版 headless 模式
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")

    return options


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="brave",
        help="Choose browser: chrome, edge, brave"
    )
    parser.addoption(
        "--headless",
        action="store_true",
        help="Run browser in headless mode"
    )

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    resp = outcome.get_result()
    print("Call: ", call)
    if resp.when == "call" and resp.failed:
        driver = item.funcargs.get("browser_instance")

        if driver:
            screenshots_dir = config.TEST_CASE_1_SCREENSHOTS_DIR
            os.makedirs(screenshots_dir, exist_ok=True)

            file_name = f"{item.name}.png"
            file_path = os.path.join(screenshots_dir, file_name)

            driver.save_screenshot(file_path)
            print(f"Screenshot saved to {file_path}")


@pytest.fixture(scope="function")
def browser_instance(request):
    browser_name = request.config.getoption("browser_name")
    headless = request.config.getoption("headless")
    if browser_name in ["chrome", "brave"]:
        options = get_chromium_options(browser_name, headless=headless)
        driver = webdriver.Chrome(options=options)
    elif browser_name == "edge":
        driver = webdriver.Edge()
    else:
        raise Exception("browser_name should be chrome, edge, brave")

    driver.implicitly_wait(4)
    driver.get("https://automationexercise.com/")

    # ✅ 移除 iframe 廣告（防止點擊被遮住）
    driver.execute_script("""
            const ads = document.querySelectorAll('iframe');
            ads.forEach(ad => ad.remove());
    """)

    yield driver
    driver.quit()
