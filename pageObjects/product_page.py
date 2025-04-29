from selenium.webdriver.common.by import By
from .base_page import BasePage


class ProductsPage(BasePage):
    PRODUCTS_HEADER = (By.XPATH, "//h2[normalize-space()='All Products']")
    FIRST_PRODUCT = (By.XPATH, "//div[@class='features_items']//div[@class='productinfo text-center']")
    FIRST_VIEW_PRODUCT = (By.XPATH, "(//a[contains(text(),'View Product')])[1]")

    def __init__(self, driver):
        super().__init__(driver)

    def is_all_products_page_displayed(self):
        return self.is_visible(self.PRODUCTS_HEADER)

    def is_product_list_visible(self):
        return self.is_visible(self.FIRST_PRODUCT)

    def click_first_view_product(self):
        self.click(self.FIRST_VIEW_PRODUCT)
