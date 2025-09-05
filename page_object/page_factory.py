from SeleniumAutomation.page_objects.home_page import HomePage
from SeleniumAutomation.page_objects.cart_page import CartPage
from SeleniumAutomation.page_objects.signup_login import SignupLogin
from SeleniumAutomation.page_objects.products_page import ProductsPage
from SeleniumAutomation.browser_utils.browser_utils import BrowserUtils
from SeleniumAutomation.page_objects.deleted_account import DeletedAccount
from SeleniumAutomation.page_objects.product_detail_page import ProductDetailPage
from SeleniumAutomation.Test_Case_1_Register_User.page_object.register import Register
from SeleniumAutomation.page_objects.created_account_logged import CreatedAccountLogged
from SeleniumAutomation.Test_Case_6_Contact_Us_Form.page_object.contact_us import ContactUs
from SeleniumAutomation.Test_Case_1_Register_User.page_object.account_created import AccountCreated
from SeleniumAutomation.Test_Case_7_Verify_Test_Cases_Page.page_object.go_test_cases import GoTestCases
from SeleniumAutomation.Test_Case_6_Contact_Us_Form.page_object.submit_contact_form import SubmitContactForm
from SeleniumAutomation.Test_Case_3_Login_User_with_incorrect_email_and_password.page_object.login_incorrect_info import LoginIncorrectInfo

class PageFactory(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.home_page = HomePage(driver)
        self.cart_page = CartPage(driver)
        self.signup_login = SignupLogin(driver)
        self.products_page = ProductsPage(driver)
        self.browser_utils = BrowserUtils(driver)
        self.deleted_account = DeletedAccount(driver)
        self.product_detail_page = ProductDetailPage(driver)
        self.register = Register(driver)
        self.created_account_logged = CreatedAccountLogged(driver)
        self.contact_us = ContactUs(driver)
        self.account_created = AccountCreated(driver)
        self.go_test_cases = GoTestCases(driver)
        self.submit_contact_form = SubmitContactForm(driver)
        self.login_incorrect_info = LoginIncorrectInfo(driver)
