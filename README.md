# 🚀 Selenium Automation Testing Framework

[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-4.31.0-green.svg)](https://www.selenium.dev/)
[![Pytest](https://img.shields.io/badge/Pytest-8.4.0-9cf.svg)](https://docs.pytest.org/)

🌐 **Test Website**: [Automation Exercise](https://www.automationexercise.com/)

## 📋 Project Overview

A full-featured web automation testing framework built with **Python + Selenium + Pytest**, focused on automating e-commerce workflows.
Covers end-to-end scenarios like user registration, login, product search, add-to-cart, and checkout.
Test scripts are written based on actual test cases provided by the website.

## 🏗️ Project Structure

```
SeleniumAutomation/
├── API_*_*/        # API automation test cases
│   ├── report
│   │     └──allure-results
│   └── test
│         └──__init__.py
│         └──test_*.py
│
├── page_object/    # Page Object Model (POM)
│        └──__init__.py
│        └──page_factory.py 
│        └── ...    
│
├── config/         # Configuration files
│        └──__init__.py
│        └──config.py  
│
├── browser_utils/  # Browser interaction utilities
│        └──__init__.py
│        └──browser_utils.py 
│
├── Test_Case_*/    # Web automation test cases
│   ├── page_object
│   │    └──test_data_folder
│   │       └──test_data.json
│   │
│   ├── screenshots
│   ├── report
│   │     └──allure-results
│   └── test
│         └──__init__.py
│         └──test_*.py  
│   
├── conftest.py     # Pytest configuration
├── .gitignore
├── __init__.py
├── Jenkinsfile
├── requirements.txt
├── setup.py
├── .pytest.ini 
├── README_CN.md     
└── README.md
```
## 🏗️ Design Highlights:
* Based on the **Page Object Model (POM)** design pattern.
* Each test case includes its own *page_object*, *report*, *screenshots*, and *test* folders.
* *page_object* encapsulates UI elements and operations into reusable classes.
* JSON test data is stored under *test_data_folder* for relevant test cases.
* Failed test screenshots are saved in *screenshots/*.
* Allure test results are stored in *report/*.
* Test scripts follow step-by-step definitions based on official test scenarios.
* *browser_utils* contains shared browser utility functions across tests.

## 🌟 Key Features:
* Easy to maintain and scale using **POM**.
* Centralized *page_factory* to manage and initialize all page objects via fixtures.
* Custom *safe_click()* and *aggressive_safe_click()* to handle loading delays and ad overlays.
* Remove full/partial iframe ads via JavaScript.
* Capture critical screenshots upon test failure.
* Supports both headless and headed modes.
* Cross-browser support for **Brave**, **Chrome**, **Edge**, and **Firefox**.
* Standalone test scripts that load data dynamically via config.py — non-devs can also run tests.
* Allure reports use *@feature*, *@story*, *@title*, and *allure.step* to reflect each test case clearly.
* Allure steps match the real test cases exactly — helpful for debugging.
* Invoice verification is automated after adding products to cart.
* CI-ready: integrated with Jenkins to allow selective test execution based on UI input.


## 🛠️ Tech Stack

### Core Technologies
- **Language**: Python 3.13
- **Automation Framework**: Selenium 4.31.0
- **Testing**: Pytest 8.4.0
- **Reporting**: Allure 2.15.0
- **CI/CD**: Jenkins 2.479.1 (Java 17)

### Browser Support
- Brave (Recommended)
- Chrome
- Edge
- Firefox

### Development Tools
- **IDE**: PyCharm Professional 2025.2.1.1
- **API Testing**: Postman 11.61.10
- **CI/CD**: Jenkins 2.479.1

### Environment
- Windows 11
- openjdk version "21.0.2" 2024-01-16
- Jenkins allure plugin

### Version Control
- Git

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Brave/Chrome/Edge/Firefox browser
- ChromeDriver/EdgeDriver/GeckoDriver

### Installation

1. Clone the repo
```bash
git clone [your-repository-url]
cd SeleniumAutomation
```

2. Create virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# Or
.\venv\Scripts\activate  # Windows
```

3. Install dependencies
```bash
pip install -r requirements.txt
```