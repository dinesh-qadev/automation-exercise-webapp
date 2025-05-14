# pages/payment_page.py

from pageObjects.base_page import BasePage
from selenium.webdriver.common.by import By


class PaymentPage(BasePage):

    NAME_ON_CARD = (By.NAME, "name_on_card")
    CARD_NUMBER = (By.NAME, "card_number")
    CVC = (By.NAME, "cvc")
    EXPIRY_MONTH = (By.NAME, "expiry_month")
    EXPIRY_YEAR = (By.NAME, "expiry_year")
    PAY_AND_CONFIRM_BUTTON = (By.ID, "submit")
    ORDER_SUCCESS_MESSAGE = (By.XPATH, "//p[normalize-space(text())='Congratulations! Your order has been confirmed!']")

    def fill_payment_form(self, payment_data):
        self.enter_text(self.NAME_ON_CARD, payment_data['name_on_card'])
        self.enter_text(self.CARD_NUMBER, payment_data['card_number'])
        self.enter_text(self.CVC, payment_data['cvc'])
        self.enter_text(self.EXPIRY_MONTH, payment_data['expiry_month'])
        self.enter_text(self.EXPIRY_YEAR, payment_data['expiry_year'])

    def click_pay_and_confirm(self):
        self.click(self.PAY_AND_CONFIRM_BUTTON)

    def verify_order_success_message(self):
        success_message = self.get_element_text(self.ORDER_SUCCESS_MESSAGE).strip()
        assert success_message == "Congratulations! Your order has been confirmed!", \
            f"Expected success message not found. Got: '{success_message}'"