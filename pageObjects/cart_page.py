from selenium.webdriver.common.by import By
from pageObjects.base_page import BasePage
from utilities.text_formatter import extract_digits


class CartPage(BasePage):
    PRODUCT_ROW_1 = (By.XPATH, "//tr[contains(@id, 'product-1')][1]")
    PRICE_1 = (By.XPATH, "(//tr[contains(@id, 'product')])[1]//td[@class='cart_price']")
    QUANTITY_1 = (By.XPATH, "(//tr[contains(@id, 'product')])[1]//button[@class='disabled']")
    TOTAL_1 = (By.XPATH, "(//tr[contains(@id, 'product')])[1]//td[@class='cart_total']")

    PRODUCT_ROW_2 = (By.XPATH, "//tr[contains(@id, 'product-2')][1]")
    PRICE_2 = (By.XPATH, "(//tr[contains(@id, 'product')])[2]//td[@class='cart_price']")
    QUANTITY_2 = (By.XPATH, "(//tr[contains(@id, 'product')])[2]//button[@class='disabled']")
    TOTAL_2 = (By.XPATH, "(//tr[contains(@id, 'product')])[2]//td[@class='cart_total']")

    def is_product_in_cart(self, product_index):
        locator = self.PRODUCT_ROW_1 if product_index == 1 else self.PRODUCT_ROW_2
        return self.is_visible(locator)

    # def verify_product_details(self, product_index):
    #     if product_index == 1:
    #         return (
    #             self.is_visible(self.PRICE_1) and
    #             self.is_visible(self.QUANTITY_1) and
    #             self.is_visible(self.TOTAL_1)
    #         )
    #     elif product_index == 2:
    #         return (
    #             self.is_visible(self.PRICE_2) and
    #             self.is_visible(self.QUANTITY_2) and
    #             self.is_visible(self.TOTAL_2)
    #         )

    def verify_product_details(self, product_index, expected_price):
        if product_index == 1:
            actual_price = self.get_element_text(self.PRICE_1).strip()
            quantity = self.get_element_text(self.QUANTITY_1).strip()
            total = self.get_element_text(self.TOTAL_1).strip()
        elif product_index == 2:
            actual_price = self.get_element_text(self.PRICE_2).strip()
            quantity = self.get_element_text(self.QUANTITY_2).strip()
            total = self.get_element_text(self.TOTAL_2).strip()
        else:
            return False

        # Clean the price string and convert to number
        actual_price_val = extract_digits(actual_price)  # Removes $ by removing non digit value
        total_val = extract_digits(total)  # Same for total

        # For expected price, check if it's a string like "RS. 500" or already a number like 500
        if isinstance(expected_price, str):
            expected_price_val = extract_digits(expected_price)
        else:
            expected_price_val = expected_price  # Already an int

        # Since only 1 quantity is added, total should equal price
        return (
                actual_price_val == expected_price_val and
                total_val == expected_price_val and
                quantity == "1"
        )

