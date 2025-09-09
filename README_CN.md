# 🚀 Selenium 自動化測試框架

[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-4.31.0-green.svg)](https://www.selenium.dev/)
[![Pytest](https://img.shields.io/badge/Pytest-8.4.0-9cf.svg)](https://docs.pytest.org/)

🌐 **測試網站**: [Automation Exercise](https://www.automationexercise.com/)

## 📋 專案概述

這是一個完整的 Web 自動化測試框架，使用 Python + Selenium + Pytest 實現，專注於電子商務網站的自動化測試。
專案涵蓋了從使用者註冊、登入、商品搜索到結帳流程的完整測試場景。
根據網站的測試案例編寫測試代碼。

## 🏗️ 專案結構

```
SeleniumAutomation/
├── API_*_*/        # API 自動化測試案例
│   ├── report
│   │     └──allure-results
│   └── test
│         └──__init__.py
│         └──test_*.py   # 測試腳本
│
├── page_object/    # 頁面對象模型
│        └──__init__.py
│        └──page_factory.py # 頁面模型的工廠
│        └── ...    # 其他常用的page_object
│
├── config/         # 配置文件
│        └──__init__.py
│        └──config.py   # 設定檔
│
├── browser_utils/  # 瀏覽器相關工具
│        └──__init__.py
│        └──browser_utils.py  
│
├── Test_Case_*/    # Web 自動化測試案例
│   ├── page_object
│   │    └──test_data_folder
│   │       └──test_data.json
│   │
│   ├── screenshots
│   ├── report
│   │     └──allure-results
│   └── test
│         └──__init__.py
│         └──test_*.py   # 測試腳本
│   
├── conftest.py     # Pytest 配置
├── .gitignore
├── __init__.py
├── Jenkinsfile
├── requirements.txt
├── setup.py
├── .pytest.ini 
├── README_CN.md   # README中文文檔
└── README.md
```
## 🏗️ 專案設計:
Page Object Model (POM) design pattern  
Web測試:  
* 每個Test Case都有page_object、report、screenshots、test四個資料夾。
其中page_object負責封裝網頁上的操作與元素成一個class物件，並根據每個測案撰寫相關的方法。
* 某些page_object底下會有個放json檔的資料夾，裡面放該測案的測試資料。
* screenshots為測試失敗截圖
* report為allure-report的放置處
* test為測試檔案，根據網頁的測試案例+步驟寫測試檔
* browser_utils負責放置與瀏覽器交互的工具，部分所有畫面共用的方法也放置於此。

## 🏗️ 專案特色:
* POM模式開發，方便後續維護和擴展。
* 建立page_factory來管理所有的page_object，並在fixture中初始化，減少每次在test檔案中重複性的實例化。
* 撰寫safe_click()和aggressive_safe_click()加強對容易被畫面loading或廣告遮擋的按鈕做點擊。
* 透過javascript撰寫移除部分或全部的iframe廣告。
* 測試失敗時可於關鍵畫面截圖。
* head模式跟headless模式切換。
* 支援brave、chrome、edge跟firefox瀏覽器的測試並可在未來擴展其他瀏覽器。
* 獨立測試檔案，在測試中讀檔並透過config文件做路徑管理，使非開發者也能測試系統。
* allure報告展示成果，透過feature、story、title説明該test case的主旨，並用allure.step的方式一步步的根據測案來測試。
* allure.step的内容跟測案完全一樣，方便對照debug。
* 加入購物車後下載發票可自動比對金額。
* 使用Jenkins部署測試代碼，並且根據畫面的test case自由選擇測試内容。


## 🛠️ 技術棧

### 核心技術
- **程式語言**: Python 3.13
- **自動化框架**: Selenium 4.31.0
- **測試框架**: Pytest 8.4.0
- **測試報告**: Allure 2.15.0
- **CI/CD**: Jenkins 2.479.1 (Java 17)

### 瀏覽器支援
- Brave (推薦)
- Chrome 
- Edge
- Firefox

### 開發工具
- **IDE**: PyCharm Professional 2025.2.1.1
- **API 測試**: Postman 11.61.10
- **CI/CD**: Jenkins 2.479.1

### 環境
- Windows 11
- openjdk version "21.0.2" 2024-01-16
- Jenkins allure plugin

### 版本控制
- git


--- 
## 🚀 快速開始（Local 開發者使用）

### 環境需求
- Python 3.8+
- Brave/Chrome/Edge/Firefox 瀏覽器
- ChromeDriver/EdgeDriver/GeckoDriver

### Installation

1. **克隆專案**
```bash
git clone https://github.com/matrixzhang98/SeleniumAutomation.git
cd SeleniumAutomation
```

2. **建立虛擬環境** (強烈建議)
```bash
python -m venv venv

# Windows
.\venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. **安裝依賴套件**
```bash
# 升級 pip
pip install --upgrade pip

# 安裝專案依賴
pip install -r requirements.txt

# 安裝專案套件
pip install .
```

### 🎯 執行測試

#### 方法一：執行單一測試案例
```bash
# 基本語法
pytest <TEST_FILE>.py --browser_name=<瀏覽器> [--headless]

# 範例：使用 Chrome 執行用戶註冊測試
pytest Test_Case_1_Register_User/test/test_end_to_end_register.py --browser_name=chrome

# 範例：使用 Brave 無頭模式執行登入測試
pytest Test_Case_2_Login_User_with_correct_email_and_password/test/test_login_with_correct_info.py --browser_name=brave --headless
```

#### 方法二：執行 API 測試
```bash
# 範例：執行產品列表 API 測試
pytest API_1_Get_All_Products_List/test/test_get_all_products_list.py --browser_name=chrome
```

#### 方法三：產生 Allure 測試報告
```bash
# 執行測試並產生 Allure 結果
pytest Test_Case_1_Register_User/test/test_end_to_end_register.py --browser_name=chrome --alluredir=Test_Case_1_Register_User/report/allure-results

# 查看測試報告 (需要先安裝 allure)
allure serve Test_Case_1_Register_User/report/allure-results
```

#### 方法四：執行 API 測試，產生 Allure 測試報告
```bash
pytest API_1_Get_All_Products_List/test/test_get_all_products_list.py --alluredir=API_1_Get_All_Products_List/report/allure-results

allure serve Test_Case_1_Register_User/report/allure-results
```

### 🔧 可用參數

| 參數               | 選項                                   | 說明                |
|------------------|--------------------------------------|-------------------|
| `--browser_name` | `brave`, `chrome`, `edge`, `firefox` | 指定測試瀏覽器           |
| `--headless`     | `normal`, `headless`                 | 啟用無頭模式 (不顯示瀏覽器視窗) |

### 📁 測試案例清單

#### TEST_FILE - Web 自動化測試 (26 個案例)
- `Test_Case_1_Register_User/test/test_end_to_end_register` - 用戶註冊
- `Test_Case_2_Login_User_with_correct_email_and_password/test/test_login_with_correct_info` - 正確登入
- `Test_Case_3_Login_User_with_incorrect_email_and_password/test/test_incorrect_user_info` - 錯誤登入
- `Test_Case_4_Logout_User/test/test_logout` - 用戶登出
- `Test_Case_5_Register_User_with_existing_email/test/test_exist_user` - 重複註冊
- `Test_Case_6_Contact_Us_Form/test/test_contact_us` - 聯絡表單
- `Test_Case_7_Verify_Test_Cases_Page/test/test_go_test_cases` - 測試案例頁面
- `Test_Case_8_Verify_All_Products_and_product_detail_page/test/test_verify_all_products` - 產品頁面
- `Test_Case_9_Search_Product/test/test_search_product` - 產品搜尋
- `Test_Case_10_Verify_Subscription_in_home_page/test/test_subscription_in_home_page` - 首頁訂閱
- `Test_Case_11_Verify_Subscription_in_Cart_page/test/test_subscription_in_cart_page` - 購物車訂閱
- `Test_Case_12_Add_Products_in_Cart/test/test_add_products_in_cart` - 加入購物車
- `Test_Case_13_Verify_Product_quantity_in_Cart/test/test_quantity_in_cart` - 購物車數量
- `Test_Case_14_Place_Order_Register_while_Checkout/test/test_place_order_register_while_checkout` - 結帳時註冊
- `Test_Case_15_Place_Order_Register_before_Checkout/test/test_place_order_register_before_checkout` - 結帳前註冊
- `Test_Case_16_Place_Order_Login_before_Checkout/test/test_place_order_login_before_checkout` - 結帳前登入
- `Test_Case_17_Remove_Products_From_Cart/test/test_remove_products_from_cart` - 移除購物車商品
- `Test_Case_18_View_Category_Products/test/test_view_category_products` - 查看分類產品
- `Test_Case_19_View_and_Cart_Brand_Products/test/test_view_and_cart_brand_products` - 品牌產品
- `Test_Case_20_Search_Products_and_Verify_Cart_After_Login/test/test_search_products_and_verify_cart_after_login` - 登入後搜尋
- `Test_Case_21_Add_review_on_product/test/test_add_review_on_product` - 產品評論
- `Test_Case_22_Add_to_cart_from_Recommended_items/test/test_add_to_cart_from_recommended_items` - 推薦商品
- `Test_Case_23_Verify_address_details_in_checkout_page/test/test_verify_address_details_in_checkout_page` - 結帳地址
- `Test_Case_24_Download_Invoice_after_purchase_order/test/test_download_invoice_after_purchase_order` - 下載發票
- `Test_Case_25_Verify_Scroll_Up_using_Arrow_button_and_Scroll_Down_functionality/test/test_verify_scroll_up_using_arrow_button_and_scroll_down_functionality` - 按鈕滾動功能
- `Test_Case_26_Verify_Scroll_Up_without_Arrow_button_and_Scroll_Down_functionality/test/test_verify_scroll_up_without_arrow_button_and_scroll_down_functionality` - 滾動功能

#### TEST_FILE - API 自動化測試 (14 個案例)
- `API_1_Get_All_Products_List/test/test_get_all_products_list` - 取得所有產品
- `API_2_POST_To_All_Products_List/test/test_post_to_all_products_list` - 產品列表 POST
- `API_3_Get_All_Brands_List/test/test_get_all_brands_list` - 取得所有品牌
- `API_4_PUT_To_All_Brands_List/test/test_put_to_all_brands_list` - 品牌列表 PUT
- `API_5_POST_To_Search_Product/test/test_post_to_search_product` - 搜尋產品
- `API_6_POST_To_Search_Product_without_search_product_parameter/test/test_post_to_search_product_without_search_product_parameter` - 無參數搜尋
- `API_7_POST_To_Verify_Login_with_valid_details/test/test_post_to_verify_login_with_valid_details` - 有效登入驗證
- `API_8_POST_To_Verify_Login_without_email_parameter/test/test_post_to_verify_login_without_email_parameter` - 無郵件登入
- `API_9_DELETE_To_Verify_Login/test/test_delete_to_verify_login` - 登入驗證 DELETE
- `API_10_POST_To_Verify_Login_with_invalid_details/test/test_post_to_verify_login_with_invalid_details` - 無效登入
- `API_11_POST_To_Create_Register_User_Account/test/test_post_to_create_register_user_account` - 建立用戶帳戶
- `API_12_DELETE_METHOD_To_Delete_User_Account/test/test_delete_method_to_delete_user_account` - 刪除用戶帳戶
- `API_13_PUT_METHOD_To_Update_User_Account/test/test_put_method_to_update_user_account` - 更新用戶帳戶
- `API_14_GET_user_account_detail_by_email/test/test_get_user_account_detail_by_email` - 依郵件取得用戶詳情

### 💡 使用提示

1. **首次執行**: 建議先執行 `Test_Case_1_Register_User` 測試用戶註冊功能
2. **瀏覽器選擇**: Brave 瀏覽器執行效果最佳，Chrome 次之
3. **無頭模式**: 在 CI/CD 環境中建議使用 `--headless` 參數
4. **測試報告**: 每次執行後都會在對應的 `report/allure-results` 目錄產生測試結果
5. **截圖功能**: 測試失敗時會自動截圖並儲存在 `screenshots` 目錄

--- 
## 🧪 使用 Jenkins 執行自動化測試（CI/CD 部署者使用）

此專案已整合 Jenkins Pipeline，clone 後即可直接部署執行。

### 步驟如下：

#### 1️⃣ 確保 Jenkins 已安裝以下插件：
- **Allure Jenkins Plugin**

#### 2️⃣ 建立 Jenkins 任務
1. 登入 Jenkins
2. 點選 **「新建任務」** > 輸入名稱(**SeleniumAutomation**)
3. 選擇 **Pipeline 專案**
4. 在「Pipeline」區塊選擇：
    - **Pipeline script from SCM**
    - SCM: `Git`
    - Repository URL: `https://github.com/matrixzhang98/SeleniumAutomation.git`
    - Branch: `master`
5. 儲存

#### 3️⃣ 設定 Pipeline 參數
執行 Job 時，選擇以下參數來決定測試行為：

- `BROWSER`：測試所使用的瀏覽器（如：brave、chrome 等）
- `HEADLESS`：是否使用 headless 模式（如：normal、headless）
- `TEST_CASE`：選擇測試案例目錄
- `TEST_FILE`：選擇實際執行的測試檔案

> ✅ 所有可選參數已在 `Jenkinsfile` 中定義，執行時會自動顯示選單。  
> ✅ 選擇參數化測試時`TEST_CASE`需與`TEST_FILE`完全一樣


| 測試案例 | TEST\_CASE 參數                                            | TEST\_FILE 參數                                                                              |
|------|----------------------------------------------------------|--------------------------------------------------------------------------------------------|
| 用戶註冊 | `Test_Case_1_Register_User`                              | `Test_Case_1_Register_User/test/test_end_to_end_register`                                  |
| 登入測試 | `Test_Case_2_Login_User_with_correct_email_and_password` | `Test_Case_2_Login_User_with_correct_email_and_password/test/test_login_with_correct_info` |
| ...  | ...                                                      | ...                                                                                        |



### 🚀 Jenkins CI/CD 整合（僅支援 windows 用戶）

本專案已整合 Jenkins 持續整合，支援：
- **參數化建置**: 可選擇瀏覽器、執行模式、測試案例
- **自動化環境設定**: 自動建立虛擬環境並安裝依賴
- **Allure 報告**: 自動產生並發布測試報告
- **多瀏覽器支援**: 支援 Brave、Chrome、Edge、Firefox

#### 4️⃣ 查看 Allure 測試報告
執行完畢後，在 Jenkins 的「建置頁面」中會自動產生並顯示 Allure 報告。

---

### 🛠️ Jenkins Pipeline 做了什麼？
當 Jenkins 執行此專案時，會自動：

1. 建立虛擬環境並啟動
2. 安裝相依套件
3. 執行指定測試檔案
4. 產生 Allure 測試報告
5. 將報告作為建置成果呈現