from selenium.webdriver.common.by import By
from pageObjects.base_page import BasePage

class CheckoutPage(BasePage):
    ADDRESS_DELIVERY_BOX = (By.ID, "address_delivery")
    REVIEW_ORDER_SECTION = (By.XPATH, "//h2[normalize-space()='Review Your Order']")
    COMMENT_TEXTAREA = (By.NAME, "message")
    PLACE_ORDER_BUTTON = (By.XPATH, "//a[normalize-space()='Place Order']")

    def is_address_delivery_box_visible(self):
        return self.is_visible(self.ADDRESS_DELIVERY_BOX)

    def get_address_delivery_box_text(self):
        return self.get_element_text(self.ADDRESS_DELIVERY_BOX)

    def is_review_order_section_visible(self):
        return self.is_visible(self.REVIEW_ORDER_SECTION)

    def enter_order_comment(self, comment):
        self.enter_text(self.COMMENT_TEXTAREA, comment)

    def click_place_order_button(self):
        self.click(self.PLACE_ORDER_BUTTON)
