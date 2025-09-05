import pytest
from pathlib import Path
from datetime import datetime
from selenium import webdriver
from SeleniumAutomation.config import config
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options as EdgeOptions
from SeleniumAutomation.page_object.page_factory import PageFactory
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def get_brave_options(headless):
    options = ChromeOptions()
    # ✅ 停用 BraveShields 提示與干擾
    options.add_argument("--disable-features=BraveShields,TrackingProtection")
    options.add_argument("--disable-brave-extension")  # Brave 有些功能是以 extension 實現的
    options.add_argument("--incognito")
    options.add_experimental_option("prefs", get_common_prefs())
    add_common_arguments(options, headless)

    return options

def get_chrome_options(headless):
    options = ChromeOptions()
    options.add_argument("--incognito")
    options.add_experimental_option("prefs", get_common_prefs())
    add_common_arguments(options, headless)
    return options

def get_edge_options(headless):
    options = EdgeOptions()
    options.add_experimental_option("prefs", get_common_prefs())
    add_common_arguments(options, headless)
    return options

def get_firefox_options(headless):
    options = FirefoxOptions()
    prefs = get_common_prefs()
    for key, value in prefs.items():
        options.set_preference(key, value)

    options.set_preference("dom.disable_open_during_load", True)
    options.set_preference("dom.popup_maximum", 0)
    options.set_preference("permissions.default.image", 2)  # 不載入圖片（若允許）
    options.set_preference("media.autoplay.default", 1)     # 禁止自動播放影片
    options.set_preference("privacy.trackingprotection.enabled", True)  # 啟用追蹤防護 # noqa

    if headless:
        options.headless = True

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

def get_common_prefs():
    # ✅ 關閉密碼儲存提示、關閉自動填寫、關閉通知
    return {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.default_content_setting_values.notifications": 2,
        "autofill.credit_card_enabled": False,
        "profile.autofill_credit_card_enabled": False,
        # ✅ 關閉自動填寫地址的提示
        "autofill.profile_enabled": False,
        "profile.autofill_profile_enabled": False,

        "download.default_directory": config.DOWNLOAD_PATH,  # ✅ 改成你測試用下載資料夾
        "download.prompt_for_download": False,               # ✅ 關閉「儲存」視窗
        "plugins.always_open_pdf_externally": True,
        "safebrowsing.enabled": True # noqa
    }

def add_common_arguments(options, headless=False):
    flags = [
        "--disable-save-password-bubble",
        "--disable-infobars", # noqa
        "--disable-popup-blocking",
        "--disable-notifications",
        "--disable-extensions",
        "--disable-features=PasswordManagerLeakDetection,AutofillServerCommunication,AutofillKeyMetrics",
        "--no-default-browser-check",
        "--disable-component-update",
        "--disable-background-networking",
        "--disable-client-side-phishing-detection",
        "--disable-domain-reliability",
        "--ignore-certificate-errors"
    ]
    for flag in flags:
        options.add_argument(flag)

    if headless:
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        # 取得測試檔案完整路徑
        test_file_path = Path(item.fspath).resolve()
        print("Call: ", call)
        # 假設你的資料夾命名皆以 Test_Case_ 開頭，我們往上找符合的資料夾
        test_case_dir = next((parent for parent in test_file_path.parents if parent.name.startswith("Test_Case_")), None)

        if test_case_dir:
            screenshots_dir = test_case_dir / "screenshots"
            screenshots_dir.mkdir(parents=True, exist_ok=True)

            # 檔案命名：test_func_name[param].png
            test_name =  f"{item.name}.png"
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_file = screenshots_dir / f"{test_name}_{timestamp}.png"

            # 從 fixture 取 driver 並截圖
            browser_instance = item.funcargs.get("browser_instance", None)
            if isinstance(browser_instance, webdriver.Chrome):  # or other browser
                browser_instance.save_screenshot(str(screenshot_file))
                print(f"\nScreenshot saved to {screenshot_file}")

@pytest.fixture(scope="function")
def browser_instance(request, web_base_url):
    browser_name = request.config.getoption("browser_name")
    headless = request.config.getoption("headless")

    if browser_name == "brave":
        options = get_brave_options(headless=headless)
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    elif browser_name == "chrome":
        options = get_chrome_options(headless=headless)
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    elif browser_name == "edge":
        options = get_edge_options(headless=headless)
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=options)
    elif browser_name == "firefox":
        options = get_firefox_options(headless=headless)
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
    else:
        raise Exception("browser_name should be chrome, edge, brave")

    driver.maximize_window()
    driver.implicitly_wait(4)
    driver.get(web_base_url)

    driver.execute_script("""
    const ads = document.querySelectorAll('iframe, #aswift_1_host, #aswift_2_host, .adsbygoogle, .ad-container, [id^="google_ads"], [id^="aswift_"]');
    ads.forEach(ad => ad.remove());
    """) # noqa

    # ✅ 移除 Google 密碼彈窗 + 持續監控避免再次出現（防止遮擋測試元素）
    driver.execute_script("""
    const pwDialogs = document.querySelectorAll('div[aria-label="Save password?"], div[role="dialog"]');
    pwDialogs.forEach(d => d.remove());
    
    const observer = new MutationObserver(() => {
        const dialogs = document.querySelectorAll('div[aria-label="Save password?"], div[role="dialog"]');
        dialogs.forEach(d => d.remove());
    });
    observer.observe(document.body, { childList: true, subtree: true });
    """)

    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def pages(browser_instance):
    return PageFactory(browser_instance)

@pytest.fixture(scope="session")
def api_base_url():
    return "https://automationexercise.com/api"

@pytest.fixture(scope="session")
def web_base_url():
    return "https://automationexercise.com/"