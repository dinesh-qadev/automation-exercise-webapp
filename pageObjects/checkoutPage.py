from selenium.webdriver.common.by import By
from pageObjects.base_page import BasePage
from utilities.text_formatter import extract_digits

class CheckoutPage(BasePage):

    # Locators
    ADDRESS_DELIVERY_BOX = (By.XPATH, "//ul[@id='address_delivery']")
    PRODUCT_NAME_1 = (By.XPATH, "(//td[@class='cart_description']/h4/a)[1]")
    PRODUCT_PRICE_1 = (By.XPATH, "(//td[@class='cart_price']/p)[1]")
    PRODUCT_QUANTITY_1 = (By.XPATH, "(//td[@class='cart_quantity']/button)[1]")
    PRODUCT_TOTAL_1 = (By.XPATH, "(//td[@class='cart_total']/p)[1]")
    COMMENT_TEXTAREA = (By.NAME, "message")
    PLACE_ORDER_BUTTON = (By.XPATH, "//a[text()='Place Order']")

    def is_address_and_review_visible(self):
        return self.is_visible(self.ADDRESS_DELIVERY_BOX)

    def get_delivery_address_text(self):
        return self.get_element_text(self.ADDRESS_DELIVERY_BOX).strip()

    def verify_product_review_details(self, expected_name, expected_price, expected_quantity):
        actual_name = self.get_element_text(self.PRODUCT_NAME_1).strip()
        actual_price = self.get_element_text(self.PRODUCT_PRICE_1).strip()
        actual_quantity = self.get_element_text(self.PRODUCT_QUANTITY_1).strip()

        assert expected_name in actual_name, f"Expected name '{expected_name}', got '{actual_name}'"
        assert extract_digits(actual_price) == extract_digits(expected_price), f"Expected price {expected_price}, got {actual_price}"
        assert int(actual_quantity) == int(expected_quantity), f"Expected quantity {expected_quantity}, got {actual_quantity}"

    def enter_comment(self, comment):
        self.enter_text(self.COMMENT_TEXTAREA, comment)

    def click_place_order(self):
        self.click(self.PLACE_ORDER_BUTTON)
