import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# TEST_CASE_1 JSON 路徑
TEST_CASE_1_REGISTER_DATA_PATH = os.path.join(BASE_DIR, "Test_Case_1_Register_User", "page_object", "register_data", "register_test_data.json")

# TEST_CASE_2 JSON 路徑
TEST_CASE_2_USER_DATA_PATH = os.path.join(BASE_DIR, "Test_Case_2_Login_User_with_correct_email_and_password", "page_object", "test_case_2_data", "user_test_data.json")

# TEST_CASE_3 JSON 路徑
TEST_CASE_3_INCORRECT_USER_DATA = os.path.join(BASE_DIR, "Test_Case_3_Login_User_with_incorrect_email_and_password", "page_object", "test_case_3_data", "incorrect_user_test_data.json")

# TEST_CASE_4 JSON 路徑
TEST_CASE_4_CORRECT_USER_DATA = os.path.join(BASE_DIR, "Test_Case_4_Logout_User", "page_object", "test_case_4_data", "correct_user_test_data.json")

# TEST_CASE_5 JSON 路徑
TEST_CASE_5_EXIST_USER_DATA = os.path.join(BASE_DIR, "Test_Case_5_Register_User_with_existing_email", "page_object", "test_case_5_data", "exist_user_test_data.json")

# TEST_CASE_6 JSON 路徑
TEST_CASE_6_CONTACT_US_DATA = os.path.join(BASE_DIR, "Test_Case_6_Contact_Us_Form", "page_object", "test_case_6_data", "contact_us_test_data.json")

# TEST_CASE_9 JSON 路徑
TEST_CASE_9_SEARCH_PRODUCT_DATA = os.path.join(BASE_DIR, "Test_Case_9_Search_Product", "page_object", "search_product_test_data", "search_product_name.json")

# TEST_CASE_10 JSON 路徑
TEST_CASE_10_SUBSCRIPTION_HOME_PAGE_EMAIL = os.path.join(BASE_DIR, "Test_Case_10_Verify_Subscription_in_home_page", "page_object", "subscription_test_data", "subscription_user_email.json")

# TEST_CASE_11 JSON 路徑
TEST_CASE_11_SUBSCRIPTION_IN_CART_PAGE_EMAIL = os.path.join(BASE_DIR, "Test_Case_11_Verify_Subscription_in_Cart_page", "page_object", "subscription_in_cart_test_data", "subscription_in_cart_user_email.json")

# TEST_CASE_14 JSON 路徑
TEST_CASE_14_REGISTER_DATA = os.path.join(BASE_DIR, "Test_Case_14_Place_Order_Register_while_Checkout", "page_object", "register_user_test_data", "register_user_test_data.json")

# TEST_CASE_15 JSON 路徑
TEST_CASE_15_REGISTER_BEFORE_CHECKOUT_DATA = os.path.join(BASE_DIR, "Test_Case_15_Place_Order_Register_before_Checkout", "page_object", "register_before_checkout_test_data", "register_before_checkout_test_data.json")

# TEST_CASE_16 JSON 路徑
TEST_CASE_16_LOGIN_BEFORE_CHECKOUT_DATA = os.path.join(BASE_DIR, "Test_Case_16_Place_Order_Login_before_Checkout", "page_object", "login_before_checkout_test_data", "login_before_checkout_test_data.json")

# TEST_CASE_17 JSON 路徑
TEST_CASE_17_REMOVE_PRODUCTS_FROM_CART_DATA = os.path.join(BASE_DIR, "Test_Case_17_Remove_Products_From_Cart", "page_object", "remove_products_from_cart_test_data", "remove_products_from_cart_test_data.json")

# TEST_CASE_18 JSON 路徑
TEST_CASE_18_VIEW_CATEGORY_PRODUCTS_DATA = os.path.join(BASE_DIR, "Test_Case_18_View_Category_Products", "page_object", "category_list_test_data", "category_list_test_data.json")

# TEST_CASE_20 JSON 路徑
TEST_CASE_20_SEARCH_PRODUCTS_AND_VERIFY_CART_AFTER_LOGIN_DATA = os.path.join(BASE_DIR, "Test_Case_20_Search_Products_and_Verify_Cart_After_Login", "page_object", "search_product_test_data", "search_product_name.json")

# TEST_CASE_21 JSON 路徑
TEST_CASE_21_ADD_REVIEW_ON_PRODUCT_DATA = os.path.join(BASE_DIR, "Test_Case_21_Add_review_on_product", "page_object", "add_review_on_product_test_data", "add_review_on_product.json")

# TEST_CASE_22 JSON 路徑
TEST_CASE_22_CAROUSEL_PRODUCT_DATA = os.path.join(BASE_DIR, "Test_Case_22_Add_to_cart_from_Recommended_items", "page_object", "carousel_product", "carousel_item.json")

# TEST_CASE_23 JSON 路徑
TEST_CASE_23_ADDRESS_DETAILS_DATA = os.path.join(BASE_DIR, "Test_Case_23_Verify_address_details_in_checkout_page", "page_object", "address_details_data", "address_details_data.json")

# TEST_CASE_24 JSON 路徑
TEST_CASE_24_DOWNLOAD_INVOICE_DATA = os.path.join(BASE_DIR, "Test_Case_24_Download_Invoice_after_purchase_order", "page_object", "download_invoice_after_purchase_order", "download_invoice_after_purchase_order.json")

# TEST_CASE_1 Allure 測試結果1資料夾
TEST_CASE_1_ALLURE_RESULTS_DIR = os.path.join(BASE_DIR, "Test_Case_1_Register_User", "report", "allure-results")

# TEST_CASE_2 Allure 測試結果資料夾
TEST_CASE_2_ALLURE_RESULTS_DIR = os.path.join(BASE_DIR, "Test_Case_2_Login_User_with_correct_email_and_password", "report", "allure-results")

# TEST_CASE_3 Allure 測試結果資料夾
TEST_CASE_3_ALLURE_RESULTS_DIR = os.path.join(BASE_DIR, "Test_Case_3_Login_User_with_incorrect_email_and_password", "report", "allure-results")

# TEST_CASE_4 Allure 測試結果資料夾
TEST_CASE_4_ALLURE_RESULTS_DIR = os.path.join(BASE_DIR, "Test_Case_4_Logout_User", "report", "allure-results")

# TEST_CASE_5 Allure 測試結果資料夾
TEST_CASE_5_ALLURE_RESULTS_DIR = os.path.join(BASE_DIR, "Test_Case_5_Register_User_with_existing_email", "report", "allure-results")

# TEST_CASE_6 Allure 測試結果資料夾
TEST_CASE_6_ALLURE_RESULTS_DIR = os.path.join(BASE_DIR, "Test_Case_6_Contact_Us_Form", "report", "allure-results")

# TEST_CASE_7 Allure 測試結果資料夾
TEST_CASE_7_ALLURE_RESULTS_DIR = os.path.join(BASE_DIR, "Test_Case_7_Verify_Test_Cases_Page", "report", "allure-results")

# TEST_CASE_8 Allure 測試結果資料夾
TEST_CASE_8_ALLURE_RESULTS_DIR = os.path.join(BASE_DIR, "Test_Case_8_Verify_All_Products_and_product_detail_page", "report", "allure-results")

# TEST_CASE_9 Allure 測試結果資料夾
TEST_CASE_9_ALLURE_RESULTS_DIR = os.path.join(BASE_DIR, "Test_Case_9_Search_Product", "report", "allure-results")

# TEST_CASE_10 Allure 測試結果資料夾
TEST_CASE_10_ALLURE_RESULTS_DIR = os.path.join(BASE_DIR, "Test_Case_10_Verify_Subscription_in_home_page", "report", "allure-results")

# TEST_CASE_11 Allure 測試結果資料夾
TEST_CASE_11_ALLURE_RESULTS_DIR = os.path.join(BASE_DIR, "Test_Case_11_Verify_Subscription_in_Cart_page", "report", "allure-results")

# TEST_CASE_12 Allure 測試結果資料夾
TEST_CASE_12_ALLURE_RESULTS_DIR = os.path.join(BASE_DIR, "Test_Case_12_Add_Products_in_Cart", "report", "allure-results")

# TEST_CASE_13 Allure 測試結果資料夾
TEST_CASE_13_ALLURE_RESULTS_DIR = os.path.join(BASE_DIR, "Test_Case_13_Verify_Product_quantity_in_Cart", "report", "allure-results")

# TEST_CASE_14 Allure 測試結果資料夾
TEST_CASE_14_ALLURE_RESULTS_DIR = os.path.join(BASE_DIR, "Test_Case_14_Place_Order_Register_while_Checkout", "report", "allure-results")

# TEST_CASE_15 Allure 測試結果資料夾
TEST_CASE_15_ALLURE_RESULTS_DIR = os.path.join(BASE_DIR, "Test_Case_15_Place_Order_Register_before_Checkout", "report", "allure-results")

# TEST_CASE_16 Allure 測試結果資料夾
TEST_CASE_16_ALLURE_RESULTS_DIR = os.path.join(BASE_DIR, "Test_Case_16_Place_Order_Login_before_Checkout", "report", "allure-results")

# TEST_CASE_17 Allure 測試結果資料夾
TEST_CASE_17_ALLURE_RESULTS_DIR = os.path.join(BASE_DIR, "Test_Case_17_Remove_Products_From_Cart", "report", "allure-results")

# TEST_CASE_18 Allure 測試結果資料夾
TEST_CASE_18_ALLURE_RESULTS_DIR = os.path.join(BASE_DIR, "Test_Case_18_View_Category_Products", "report", "allure-results")

# TEST_CASE_19 Allure 測試結果資料夾
TEST_CASE_19_ALLURE_RESULTS_DIR = os.path.join(BASE_DIR, "Test_Case_19_View_and_Cart_Brand_Products", "report", "allure-results")

# TEST_CASE_20 Allure 測試結果資料夾
TEST_CASE_20_ALLURE_RESULTS_DIR = os.path.join(BASE_DIR, "Test_Case_20_Search_Products_and_Verify_Cart_After_Login", "report", "allure-results")

# TEST_CASE_21 Allure 測試結果資料夾
TEST_CASE_21_ALLURE_RESULTS_DIR = os.path.join(BASE_DIR, "Test_Case_21_Add_review_on_product", "report", "allure-results")

# TEST_CASE_22 Allure 測試結果資料夾
TEST_CASE_22_ALLURE_RESULTS_DIR = os.path.join(BASE_DIR, "Test_Case_22_Add_to_cart_from_Recommended_items", "report", "allure-results")

# TEST_CASE_23 Allure 測試結果資料夾
TEST_CASE_23_ALLURE_RESULTS_DIR = os.path.join(BASE_DIR, "Test_Case_23_Verify_address_details_in_checkout_page", "report", "allure-results")

# TEST_CASE_24 Allure 測試結果資料夾
TEST_CASE_24_ALLURE_RESULTS_DIR = os.path.join(BASE_DIR, "Test_Case_24_Download_Invoice_after_purchase_order", "report", "allure-results")

# TEST_CASE_25 Allure 測試結果資料夾
TEST_CASE_25_ALLURE_RESULTS_DIR = os.path.join(BASE_DIR, "Test_Case_25_Verify_Scroll_Up_using_Arrow_button_and_Scroll_Down_functionality", "report", "allure-results")

# TEST_CASE_26 Allure 測試結果資料夾
TEST_CASE_26_ALLURE_RESULTS_DIR = os.path.join(BASE_DIR, "Test_Case_26_Verify_Scroll_Up_without_Arrow_button_and_Scroll_Down_functionality", "report", "allure-results")

# TEST_CASE_1 Screenshots 截圖資料夾
TEST_CASE_1_SCREENSHOTS_DIR = os.path.join(BASE_DIR, "Test_Case_1_Register_User", "screenshots")

# TEST_CASE_2 Screenshots 截圖資料夾
TEST_CASE_2_SCREENSHOTS_DIR = os.path.join(BASE_DIR, "Test_Case_2_Login_User_with_correct_email_and_password", "screenshots")

# TEST_CASE_3 Screenshots 截圖資料夾
TEST_CASE_3_SCREENSHOTS_DIR = os.path.join(BASE_DIR, "Test_Case_3_Login_User_with_incorrect_email_and_password", "screenshots")

# TEST_CASE_4 Screenshots 截圖資料夾
TEST_CASE_4_SCREENSHOTS_DIR = os.path.join(BASE_DIR, "Test_Case_4_Logout_User", "screenshots")

# TEST_CASE_5 Screenshots 截圖資料夾
TEST_CASE_5_SCREENSHOTS_DIR = os.path.join(BASE_DIR, "Test_Case_5_Register_User_with_existing_email", "screenshots")

# TEST_CASE_6 Screenshots 截圖資料夾
TEST_CASE_6_SCREENSHOTS_DIR = os.path.join(BASE_DIR, "Test_Case_6_Contact_Us_Form", "screenshots")

# TEST_CASE_7 Screenshots 截圖資料夾
TEST_CASE_7_SCREENSHOTS_DIR = os.path.join(BASE_DIR, "Test_Case_7_Verify_Test_Cases_Page", "screenshots")

# TEST_CASE_8 Screenshots 截圖資料夾
TEST_CASE_8_SCREENSHOTS_DIR = os.path.join(BASE_DIR, "Test_Case_8_Verify_All_Products_and_product_detail_page", "screenshots")

# TEST_CASE_9 Screenshots 截圖資料夾
TEST_CASE_9_SCREENSHOTS_DIR = os.path.join(BASE_DIR, "Test_Case_9_Search_Product", "screenshots")

# TEST_CASE_10 Screenshots 截圖資料夾
TEST_CASE_10_SCREENSHOTS_DIR = os.path.join(BASE_DIR, "Test_Case_10_Verify_Subscription_in_home_page", "screenshots")

# TEST_CASE_11 Screenshots 截圖資料夾
TEST_CASE_11_SCREENSHOTS_DIR = os.path.join(BASE_DIR, "Test_Case_11_Verify_Subscription_in_Cart_page", "screenshots")

# TEST_CASE_12 Screenshots 截圖資料夾
TEST_CASE_12_SCREENSHOTS_DIR = os.path.join(BASE_DIR, "Test_Case_12_Add_Products_in_Cart", "screenshots")

# TEST_CASE_13 Screenshots 截圖資料夾
TEST_CASE_13_SCREENSHOTS_DIR = os.path.join(BASE_DIR, "Test_Case_13_Verify_Product_quantity_in_Cart", "screenshots")

# TEST_CASE_14 Screenshots 截圖資料夾
TEST_CASE_14_SCREENSHOTS_DIR = os.path.join(BASE_DIR, "Test_Case_14_Place_Order_Register_while_Checkout", "screenshots")

# TEST_CASE_15 Screenshots 截圖資料夾
TEST_CASE_15_SCREENSHOTS_DIR = os.path.join(BASE_DIR, "Test_Case_15_Place_Order_Register_before_Checkout", "screenshots")

# TEST_CASE_16 Screenshots 截圖資料夾
TEST_CASE_16_SCREENSHOTS_DIR = os.path.join(BASE_DIR, "Test_Case_16_Place_Order_Login_before_Checkout", "screenshots")

# TEST_CASE_17 Screenshots 截圖資料夾
TEST_CASE_17_SCREENSHOTS_DIR = os.path.join(BASE_DIR, "Test_Case_17_Remove_Products_From_Cart", "screenshots")

# TEST_CASE_18 Screenshots 截圖資料夾
TEST_CASE_18_SCREENSHOTS_DIR = os.path.join(BASE_DIR, "Test_Case_18_View_Category_Products", "screenshots")

# TEST_CASE_19 Screenshots 截圖資料夾
TEST_CASE_19_SCREENSHOTS_DIR = os.path.join(BASE_DIR, "Test_Case_19_View_and_Cart_Brand_Products", "screenshots")

# TEST_CASE_20 Screenshots 截圖資料夾
TEST_CASE_20_SCREENSHOTS_DIR = os.path.join(BASE_DIR, "Test_Case_20_Search_Products_and_Verify_Cart_After_Login", "screenshots")

# TEST_CASE_21 Screenshots 截圖資料夾
TEST_CASE_21_SCREENSHOTS_DIR = os.path.join(BASE_DIR, "Test_Case_21_Add_review_on_product", "screenshots")

# TEST_CASE_22 Screenshots 截圖資料夾
TEST_CASE_22_SCREENSHOTS_DIR = os.path.join(BASE_DIR, "Test_Case_22_Add_to_cart_from_Recommended_items", "screenshots")

# TEST_CASE_23 Screenshots 截圖資料夾
TEST_CASE_23_SCREENSHOTS_DIR = os.path.join(BASE_DIR, "Test_Case_23_Verify_address_details_in_checkout_page", "screenshots")

# TEST_CASE_24 Screenshots 截圖資料夾
TEST_CASE_24_SCREENSHOTS_DIR = os.path.join(BASE_DIR, "Test_Case_24_Download_Invoice_after_purchase_order", "screenshots")

# TEST_CASE_25 Screenshots 截圖資料夾
TEST_CASE_25_SCREENSHOTS_DIR = os.path.join(BASE_DIR, "Test_Case_25_Verify_Scroll_Up_using_Arrow_button_and_Scroll_Down_functionality", "screenshots")

# TEST_CASE_26 Screenshots 截圖資料夾
TEST_CASE_26_SCREENSHOTS_DIR = os.path.join(BASE_DIR, "Test_Case_26_Verify_Scroll_Up_without_Arrow_button_and_Scroll_Down_functionality", "screenshots")

DOWNLOAD_PATH = os.getenv("DOWNLOAD_PATH", str(Path.home() / "Downloads"))

# 可匯出變數（選擇性）
__all__ = [
    "BASE_DIR",
    "TEST_CASE_1_REGISTER_DATA_PATH",
    "TEST_CASE_2_USER_DATA_PATH",
    "TEST_CASE_3_INCORRECT_USER_DATA",
    "TEST_CASE_4_CORRECT_USER_DATA",
    "TEST_CASE_5_EXIST_USER_DATA",
    "TEST_CASE_6_CONTACT_US_DATA",
    "TEST_CASE_9_SEARCH_PRODUCT_DATA",
    "TEST_CASE_10_SUBSCRIPTION_HOME_PAGE_EMAIL",
    "TEST_CASE_11_SUBSCRIPTION_IN_CART_PAGE_EMAIL",
    "TEST_CASE_14_REGISTER_DATA",
    "TEST_CASE_15_REGISTER_BEFORE_CHECKOUT_DATA",
    "TEST_CASE_16_LOGIN_BEFORE_CHECKOUT_DATA",
    "TEST_CASE_17_REMOVE_PRODUCTS_FROM_CART_DATA",
    "TEST_CASE_18_VIEW_CATEGORY_PRODUCTS_DATA",
    "TEST_CASE_20_SEARCH_PRODUCTS_AND_VERIFY_CART_AFTER_LOGIN_DATA",
    "TEST_CASE_21_ADD_REVIEW_ON_PRODUCT_DATA",
    "TEST_CASE_22_CAROUSEL_PRODUCT_DATA",
    "TEST_CASE_23_ADDRESS_DETAILS_DATA",
    "TEST_CASE_24_DOWNLOAD_INVOICE_DATA",
    "TEST_CASE_1_ALLURE_RESULTS_DIR",
    "TEST_CASE_2_ALLURE_RESULTS_DIR",
    "TEST_CASE_3_ALLURE_RESULTS_DIR",
    "TEST_CASE_4_ALLURE_RESULTS_DIR",
    "TEST_CASE_5_ALLURE_RESULTS_DIR",
    "TEST_CASE_6_ALLURE_RESULTS_DIR",
    "TEST_CASE_7_ALLURE_RESULTS_DIR",
    "TEST_CASE_8_ALLURE_RESULTS_DIR",
    "TEST_CASE_9_ALLURE_RESULTS_DIR",
    "TEST_CASE_10_ALLURE_RESULTS_DIR",
    "TEST_CASE_11_ALLURE_RESULTS_DIR",
    "TEST_CASE_12_ALLURE_RESULTS_DIR",
    "TEST_CASE_13_ALLURE_RESULTS_DIR",
    "TEST_CASE_14_ALLURE_RESULTS_DIR",
    "TEST_CASE_15_ALLURE_RESULTS_DIR",
    "TEST_CASE_16_ALLURE_RESULTS_DIR",
    "TEST_CASE_17_ALLURE_RESULTS_DIR",
    "TEST_CASE_18_ALLURE_RESULTS_DIR",
    "TEST_CASE_19_ALLURE_RESULTS_DIR",
    "TEST_CASE_20_ALLURE_RESULTS_DIR",
    "TEST_CASE_21_ALLURE_RESULTS_DIR",
    "TEST_CASE_22_ALLURE_RESULTS_DIR",
    "TEST_CASE_23_ALLURE_RESULTS_DIR",
    "TEST_CASE_24_ALLURE_RESULTS_DIR",
    "TEST_CASE_25_ALLURE_RESULTS_DIR",
    "TEST_CASE_26_ALLURE_RESULTS_DIR",
    "TEST_CASE_1_SCREENSHOTS_DIR",
    "TEST_CASE_2_SCREENSHOTS_DIR",
    "TEST_CASE_3_SCREENSHOTS_DIR",
    "TEST_CASE_4_SCREENSHOTS_DIR",
    "TEST_CASE_5_SCREENSHOTS_DIR",
    "TEST_CASE_6_SCREENSHOTS_DIR",
    "TEST_CASE_7_SCREENSHOTS_DIR",
    "TEST_CASE_8_SCREENSHOTS_DIR",
    "TEST_CASE_9_SCREENSHOTS_DIR",
    "TEST_CASE_10_SCREENSHOTS_DIR",
    "TEST_CASE_11_SCREENSHOTS_DIR",
    "TEST_CASE_12_SCREENSHOTS_DIR",
    "TEST_CASE_13_SCREENSHOTS_DIR",
    "TEST_CASE_14_SCREENSHOTS_DIR",
    "TEST_CASE_15_SCREENSHOTS_DIR",
    "TEST_CASE_16_SCREENSHOTS_DIR",
    "TEST_CASE_17_SCREENSHOTS_DIR",
    "TEST_CASE_18_SCREENSHOTS_DIR",
    "TEST_CASE_19_SCREENSHOTS_DIR",
    "TEST_CASE_20_SCREENSHOTS_DIR",
    "TEST_CASE_21_SCREENSHOTS_DIR",
    "TEST_CASE_22_SCREENSHOTS_DIR",
    "TEST_CASE_23_SCREENSHOTS_DIR",
    "TEST_CASE_24_SCREENSHOTS_DIR",
    "TEST_CASE_25_SCREENSHOTS_DIR",
    "TEST_CASE_26_SCREENSHOTS_DIR",
    "DOWNLOAD_PATH"
]
