from selenium.webdriver.common.by import By
from .base_page import BasePage

class ProductDetailPage(BasePage):
    PRODUCT_NAME = (By.XPATH, "//div[@class='product-information']/h2")
    CATEGORY = (By.XPATH, "//div[@class='product-information']/p[1]")
    PRICE = (By.XPATH, "//div[@class='product-information']//span/span")
    AVAILABILITY = (By.XPATH, "// b[normalize-space()='Availability:']")
    CONDITION = (By.XPATH, "//div[@class='product-information']/p/b[contains(text(),'Condition:')]")
    BRAND = (By.XPATH, "//div[@class='product-information']/p/b[contains(text(),'Brand:')]")

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
