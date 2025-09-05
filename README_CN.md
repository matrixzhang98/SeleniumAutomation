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
├── __init__.py
├── Jenkinsfile
├── requirements.txt
├── .pytest.ini     
└── README.md       # 專案文檔
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

## 🚀 快速開始

### 環境需求
- Python 3.8+
- Brave/Chrome/Edge/Firefox 瀏覽器
- ChromeDriver/EdgeDriver/GeckoDriver

### 安裝步驟

1. 克隆專案
```bash
git clone [your-repository-url]
cd SeleniumAutomation
```

2. 建立虛擬環境 (建議)
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
.\venv\Scripts\activate  # Windows
```

3. 安裝依賴
```bash
pip install -r requirements.txt
```