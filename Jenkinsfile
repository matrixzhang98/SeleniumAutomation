pipeline {
    agent any

    parameters {
        choice(name: 'BROWSER', choices: ['brave', 'chrome', 'edge', 'firefox'], description: 'Choose the browser(指定測試瀏覽器)')
        choice(name: 'HEADLESS', choices: ['normal', 'headless'], description: 'Choose the head mode(是否使用 headless 模式)')
        choice(name: 'TEST_CASE', choices: [
            'Test_Case_1_Register_User',
            'Test_Case_2_Login_User_with_correct_email_and_password',
            'Test_Case_3_Login_User_with_incorrect_email_and_password',
            'Test_Case_4_Logout_User',
            'Test_Case_5_Register_User_with_existing_email',
            'Test_Case_6_Contact_Us_Form',
            'Test_Case_7_Verify_Test_Cases_Page',
            'Test_Case_8_Verify_All_Products_and_product_detail_page',
            'Test_Case_9_Search_Product',
            'Test_Case_10_Verify_Subscription_in_home_page',
            'Test_Case_11_Verify_Subscription_in_Cart_page',
            'Test_Case_12_Add_Products_in_Cart',
            'Test_Case_13_Verify_Product_quantity_in_Cart',
            'Test_Case_14_Place_Order_Register_while_Checkout',
            'Test_Case_15_Place_Order_Register_before_Checkout',
            'Test_Case_16_Place_Order_Login_before_Checkout',
            'Test_Case_17_Remove_Products_From_Cart',
            'Test_Case_18_View_Category_Products',
            'Test_Case_19_View_and_Cart_Brand_Products',
            'Test_Case_20_Search_Products_and_Verify_Cart_After_Login',
            'Test_Case_21_Add_review_on_product',
            'Test_Case_22_Add_to_cart_from_Recommended_items',
            'Test_Case_23_Verify_address_details_in_checkout_page',
            'Test_Case_24_Download_Invoice_after_purchase_order',
            'Test_Case_25_Verify_Scroll_Up_using_Arrow_button_and_Scroll_Down_functionality',
            'Test_Case_26_Verify_Scroll_Up_without_Arrow_button_and_Scroll_Down_functionality',
            'API_1_Get_All_Products_List',
            'API_2_POST_To_All_Products_List',
            'API_3_Get_All_Brands_List',
            'API_4_PUT_To_All_Brands_List',
            'API_5_POST_To_Search_Product',
            'API_6_POST_To_Search_Product_without_search_product_parameter',
            'API_7_POST_To_Verify_Login_with_valid_details',
            'API_8_POST_To_Verify_Login_without_email_parameter',
            'API_9_DELETE_To_Verify_Login',
            'API_10_POST_To_Verify_Login_with_invalid_details',
            'API_11_POST_To_Create_Register_User_Account',
            'API_12_DELETE_METHOD_To_Delete_User_Account',
            'API_13_PUT_METHOD_To_Update_User_Account',
            'API_14_GET_user_account_detail_by_email'
        ], description: 'Select the corresponding test case(選擇要執行的測試案例)')
        choice(name: 'TEST_FILE', choices: [
            'Test_Case_1_Register_User/test/test_end_to_end_register',
            'Test_Case_2_Login_User_with_correct_email_and_password/test/test_login_with_correct_info',
            'Test_Case_3_Login_User_with_incorrect_email_and_password/test/test_incorrect_user_info',
            'Test_Case_4_Logout_User/test/test_logout',
            'Test_Case_5_Register_User_with_existing_email/test/test_exist_user',
            'Test_Case_6_Contact_Us_Form/test/test_contact_us',
            'Test_Case_7_Verify_Test_Cases_Page/test/test_go_test_cases',
            'Test_Case_8_Verify_All_Products_and_product_detail_page/test/test_verify_all_products',
            'Test_Case_9_Search_Product/test/test_search_product',
            'Test_Case_10_Verify_Subscription_in_home_page/test/test_subscription_in_home_page',
            'Test_Case_11_Verify_Subscription_in_Cart_page/test/test_subscription_in_cart_page',
            'Test_Case_12_Add_Products_in_Cart/test/test_add_products_in_cart',
            'Test_Case_13_Verify_Product_quantity_in_Cart/test/test_quantity_in_cart',
            'Test_Case_14_Place_Order_Register_while_Checkout/test/test_place_order_register_while_checkout',
            'Test_Case_15_Place_Order_Register_before_Checkout/test/test_place_order_register_before_checkout',
            'Test_Case_16_Place_Order_Login_before_Checkout/test/test_place_order_login_before_checkout',
            'Test_Case_17_Remove_Products_From_Cart/test/test_remove_products_from_cart',
            'Test_Case_18_View_Category_Products/test/test_view_category_products',
            'Test_Case_19_View_and_Cart_Brand_Products/test/test_view_and_cart_brand_products',
            'Test_Case_20_Search_Products_and_Verify_Cart_After_Login/test/test_search_products_and_verify_cart_after_login',
            'Test_Case_21_Add_review_on_product/test/test_add_review_on_product',
            'Test_Case_22_Add_to_cart_from_Recommended_items/test/test_add_to_cart_from_recommended_items',
            'Test_Case_23_Verify_address_details_in_checkout_page/test/test_verify_address_details_in_checkout_page',
            'Test_Case_24_Download_Invoice_after_purchase_order/test/test_download_invoice_after_purchase_order',
            'Test_Case_25_Verify_Scroll_Up_using_Arrow_button_and_Scroll_Down_functionality/test/test_verify_scroll_up_using_arrow_button_and_scroll_down_functionality',
            'Test_Case_26_Verify_Scroll_Up_without_Arrow_button_and_Scroll_Down_functionality/test/test_verify_scroll_up_without_arrow_button_and_scroll_down_functionality',
            'API_1_Get_All_Products_List/test/test_get_all_products_list',
            'API_2_POST_To_All_Products_List/test/test_post_to_all_products_list',
            'API_3_Get_All_Brands_List/test/test_get_all_brands_list',
            'API_4_PUT_To_All_Brands_List/test/test_put_to_all_brands_list',
            'API_5_POST_To_Search_Product/test/test_post_to_search_product',
            'API_6_POST_To_Search_Product_without_search_product_parameter/test/test_post_to_search_product_without_search_product_parameter',
            'API_7_POST_To_Verify_Login_with_valid_details/test/test_post_to_verify_login_with_valid_details',
            'API_8_POST_To_Verify_Login_without_email_parameter/test/test_post_to_verify_login_without_email_parameter',
            'API_9_DELETE_To_Verify_Login/test/test_delete_to_verify_login',
            'API_10_POST_To_Verify_Login_with_invalid_details/test/test_post_to_verify_login_with_invalid_details',
            'API_11_POST_To_Create_Register_User_Account/test/test_post_to_create_register_user_account',
            'API_12_DELETE_METHOD_To_Delete_User_Account/test/test_delete_method_to_delete_user_account',
            'API_13_PUT_METHOD_To_Update_User_Account/test/test_put_method_to_update_user_account',
            'API_14_GET_user_account_detail_by_email/test/test_get_user_account_detail_by_email'
        ], description: 'Select the corresponding test file(選擇要執行的測試檔)')
    }

    stages {
        stage('Echo Parameters') {
            steps {
                bat '''
                echo BROWSER: %BROWSER%
                echo HEADLESS: %HEADLESS%
                echo TEST_FILE: %TEST_FILE%
                echo TEST_CASE: %TEST_CASE%
                '''
            }
        }

        stage('Setup Python Environment') {
            steps {
                bat '''
                cd SeleniumAutomation
                call venv\\Scripts\\activate
                python --version
                pip install --upgrade pip
                pip install -r requirements.txt
                pip install .
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                cd SeleniumAutomation
                call venv\\Scripts\\activate
                setlocal EnableDelayedExpansion

                set HEADLESS_OPTION=
                if "%HEADLESS%"=="headless" (
                    set HEADLESS_OPTION=--headless
                ) else (
					set HEADLESS_OPTION=
				)

                REM 清除舊的 Allure 結果
                del /Q %TEST_CASE%\\report\\allure-results\\*

                pytest %TEST_FILE%.py ^
                  --browser_name=%BROWSER% ^
                  !HEADLESS_OPTION! ^
                  --alluredir=%TEST_CASE%\\report\\allure-results

                dir /s /b %TEST_CASE%\\report\\allure-results
                '''
            }
        }

        stage('Debug Allure Results Path') {
            steps {
                bat "dir /s /b ${params.TEST_CASE}\\report\\allure-results"
            }
        }

        stage('Allure Report') {
            steps {
                allure([
                    includeProperties: true,
                    results: [[path: "${params.TEST_CASE}\\report\\allure-results"]]
                ])
            }
        }
    }
}
