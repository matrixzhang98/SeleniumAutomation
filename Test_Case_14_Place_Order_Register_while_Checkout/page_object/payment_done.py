import os
import time
from selenium.webdriver.common.by import By
from SeleniumAutomation.config import config
from SeleniumAutomation.browser_utils.browser_utils import BrowserUtils
from SeleniumAutomation.Test_Case_14_Place_Order_Register_while_Checkout.page_object.checkout import Checkout


class PaymentDone(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.checkout = Checkout(driver)
        self.download_invoice = (By.XPATH, "//a[contains(., 'Download Invoice')]")
        self.continue_button = (By.XPATH, "//a[contains(., 'Continue')]")
        self.title = (By.XPATH, "//h2[@data-qa='order-placed']")
        self.success_message = (By.XPATH, "//p[contains(text(), 'order has been confirmed')]")
        self.download_dir = config.DOWNLOAD_PATH

    def verify_payment_done_title(self):
        expected_title = "ORDER PLACED!"
        actual_title = self.driver.find_element(*self.title).text
        assert expected_title.lower() == actual_title.lower(), \
            f"Expected {expected_title}, but got {actual_title}"

    def verify_payment_done_page_by_url(self):
        url = self.driver.current_url
        assert "payment_done" in url, f"Unexpected URL: {url}"

    def verify_order_placed_success_message(self):
        # Congratulations! Your order has been confirmed!
        success_message = self.driver.find_element(*self.success_message).text
        assert "Congratulations" in success_message, \
            f"Expected 'Congratulations in success message', but got '{success_message}'"

    def click_continue_button_after_payment_done(self):
        self.safe_click(*self.continue_button)

    def click_download_invoice(self):
        self.aggressive_safe_click(*self.download_invoice)

    def wait_for_download(self, timeout=15, extension=".txt"):
        start_time = time.time()
        while time.time() - start_time < timeout:
            last_file = self.get_last_downloaded_file()
            if last_file:
                if last_file.endswith(extension) and not last_file.endswith((".crdownload", ".tmp")):
                    return last_file
            time.sleep(1)
        raise TimeoutError(f"No .txt file downloaded within {timeout} seconds.")

    def get_last_downloaded_file(self):
        files = os.listdir(self.download_dir)
        files = [f for f in files if not f.endswith(".crdownload")]  # ✅ 避免尚未完成的檔案
        if not files:
            return None

        full_paths = []
        for f in files:
            full_path = os.path.join(self.download_dir, f)
            try:
                # 嘗試取得建立時間，若檔案不存在跳過
                _ = os.path.getctime(full_path)
                full_paths.append(full_path)
            except FileNotFoundError:
                continue
        if not full_paths:
            return None
        return max(full_paths, key=os.path.getctime)

    def download_invoice_and_verify_content(self):
        self.click_download_invoice()
        download_file = self.wait_for_download(extension=".txt")

        assert download_file.endswith(".txt"), f"Download file is not .txt file: {download_file}"
        assert os.path.getsize(download_file) > 0, f"Download file is empty: {download_file}"

        with open(download_file, 'r', encoding='utf-8') as f:
            content = f.read()
            print("[DEBUG] file content: ", content)
        return content

    def check_the_download_invoice_content(self, price: str):
        file = self.download_invoice_and_verify_content()
        assert price in file, f"Price {price} not found in download file"