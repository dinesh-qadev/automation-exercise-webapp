from selenium.webdriver.common.by import By
from .base_page import BasePage


class ProductDetailPage(BasePage):
    PRODUCT_NAME = (By.XPATH, "//div[@class='product-information']/h2")
    CATEGORY = (By.XPATH, "//div[@class='product-information']/p[1]")
    PRICE = (By.XPATH, "//div[@class='product-information']//span/span")
    AVAILABILITY = (By.XPATH, "// b[normalize-space()='Availability:']")
    CONDITION = (By.XPATH, "//div[@class='product-information']/p/b[contains(text(),'Condition:')]")
    BRAND = (By.XPATH, "//div[@class='product-information']/p/b[contains(text(),'Brand:')]")

    #Locators for TestCase_013
    PRODUCT_INFO = (By.XPATH, "//div[@class='product-information']")
    QUANTITY_INPUT = (By.ID, "quantity")
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[normalize-space()='Add to cart']")
    VIEW_CART_LINK = (By.XPATH, "//u[normalize-space()='View Cart']")

    def __init__(self, driver):
        super().__init__(driver)

    def is_product_detail_page_displayed(self):
        # Check if the current URL contains 'product_details'
        current_url = self.driver.current_url
        return "product_details" in current_url
        #return self.is_visible(self.PRODUCT_NAME)

    def is_product_name_visible(self):
        return self.is_visible(self.PRODUCT_NAME)

    def is_category_visible(self):
        return self.is_visible(self.CATEGORY)

    def is_price_visible(self):
        # text = self.get_element_text(self.PRICE)
        # print(text)
        return self.is_visible(self.PRICE)

    def is_availability_visible(self):
        return self.is_visible(self.AVAILABILITY)

    def is_condition_visible(self):
        return self.is_visible(self.CONDITION)

    def is_brand_visible(self):
        return self.is_visible(self.BRAND)

    #Methods for TestCase_013
    def is_product_detail_visible(self):
        return self.is_visible(self.PRODUCT_INFO)

    def set_quantity(self, quantity):
        self.clear_input(self.QUANTITY_INPUT)
        self.enter_text(self.QUANTITY_INPUT, text=quantity)

    def click_add_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)

    def click_view_cart(self):
        self.click(self.VIEW_CART_LINK)
