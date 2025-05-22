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

    #Locator for TestCase_013
    PRODUCT_QUANTITIES = (By.XPATH, "//table[@id='cart_info_table']//td[@class='cart_quantity']")

    #Locators for TestCase14
    PROCEED_TO_CHECKOUT_BUTTON = (By.XPATH, "//a[normalize-space()='Proceed To Checkout']")
    REGISTER_LOGIN_BUTTON = (By.XPATH, "//u[normalize-space()='Register / Login']")

    PRODUCT_NAME_1 = (By.XPATH, "(//div[@class='productinfo text-center'])[1]//p")
    PRODUCT_NAME_2 = (By.XPATH, "(//div[@class='productinfo text-center'])[2]//p")

    #Testcase_017
    DELETE_PRODUCT_BUTTON = (By.XPATH, "//a[@class='cart_quantity_delete']")
    PRODUCT_IN_CART = (By.XPATH, "//tr[@id='product-1']")

    # Dynamic locator for a product row by name
    PRODUCT_ROW_BY_NAME = (By.XPATH, "//tr[@id][.//a[contains(text(), '{}')]]")

    # PRODUCT_PRICE = (By.XPATH, "(//td[@class='cart_price']//p)[{}]")
    # PRODUCT_QUANTITY = (By.XPATH, "(//td[@class='cart_quantity']//button)[{}]")
    # PRODUCT_TOTAL = (By.XPATH, "(//td[@class='cart_total']//p)[{}]")

    def is_cart_page_visible(self):
        return "/view_cart" in self.driver.current_url

    # def are_products_in_cart(self, product_index):
    #     locator = self.PRODUCT_ROW_1 if product_index == 1 else self.PRODUCT_ROW_2
    #     return self.is_visible(locator)

    def are_products_in_cart(self, product_names: list):
        """
                Verifies that all given product names are present in the cart.
                Returns True if all are found, False if any is missing.
                """
        for name in product_names:
            locator = (
                self.PRODUCT_ROW_BY_NAME[0],
                self.PRODUCT_ROW_BY_NAME[1].format(name.strip())
            )
            self.wait_for_element(locator)
            if not self.is_visible(locator):
                print(f"Product not found in cart: {name}")
                return False
        return True

    def verify_product_details(self, product_index, expected_price):
        if product_index == 1:
            actual_price = self.get_element_text(self.PRICE_1).strip()
            quantity = self.get_element_text(self.QUANTITY_1).strip()
            total = self.get_element_text(self.TOTAL_1).strip()
            # product = self.get_element_text(self.PRODUCT_NAME_1).strip()
        elif product_index == 2:
            actual_price = self.get_element_text(self.PRICE_2).strip()
            quantity = self.get_element_text(self.QUANTITY_2).strip()
            total = self.get_element_text(self.TOTAL_2).strip()
            # product = self.get_element_text(self.PRODUCT_NAME_2).strip()
        else:
            return False

        # Clean the price string and convert to number
        actual_price_val = extract_digits(actual_price)  # Removes RS by removing non digit value
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

    # Methods for TestCase_013
    def get_product_quantity(self):
        quantity_text = self.get_element_text(self.PRODUCT_QUANTITIES).strip()
        return int(quantity_text)

    #Methods for Testcase_14
    def click_proceed_to_checkout(self):
        self.click(self.PROCEED_TO_CHECKOUT_BUTTON)

    def click_register_login_button(self):
        self.click(self.REGISTER_LOGIN_BUTTON)

    #Methods for Testcase_017
    def delete_product_from_cart(self):
        self.click(self.DELETE_PRODUCT_BUTTON)

    def is_product_removed(self):
        return self.wait_for_element_to_disappear(self.PRODUCT_IN_CART)
