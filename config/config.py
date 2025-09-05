import os

# 專案根目錄（SeleniumAutomation）
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 測試資料 JSON 路徑
REGISTER_DATA_PATH = os.path.join(BASE_DIR, "page_object", "register_data", "register_test_data.json")

# Allure 測試結果儲存資料夾
ALLURE_RESULTS_DIR = os.path.join(BASE_DIR, "report", "allure-results")

# Screenshots 資料夾路徑（放在 Test_Case_1_Register_User 裡）
SCREENSHOTS_DIR = os.path.join(BASE_DIR, "screenshots")

# Brave 瀏覽器執行檔路徑
BRAVE_PATH = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"