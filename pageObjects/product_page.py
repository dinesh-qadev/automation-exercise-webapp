from selenium.webdriver.common.by import By
from .base_page import BasePage
import re


class ProductsPage(BasePage):
    #Locators
    PRODUCTS_HEADER = (By.XPATH, "//h2[normalize-space()='All Products']")
    FIRST_PRODUCT = (By.XPATH, "//div[@class='features_items']//div[@class='productinfo text-center']")
    FIRST_VIEW_PRODUCT = (By.XPATH, "(//a[contains(text(),'View Product')])[1]")

    #Locatior for testcase_009
    SEARCH_INPUT = (By.ID, 'search_product')
    SEARCH_BUTTON = (By.ID, 'submit_search')
    SEARCHED_PRODUCTS_TITLE = (By.XPATH, "//h2[text()='Searched Products']")
    SEARCH_RESULT_ITEMS = (By.XPATH, "//div[@class='productinfo text-center']/p")

    def __init__(self, driver):
        super().__init__(driver)

    def is_all_products_page_displayed(self):
        return self.is_visible(self.PRODUCTS_HEADER)

    def is_product_list_visible(self):
        return self.is_visible(self.FIRST_PRODUCT)

    def click_first_view_product(self):
        self.click(self.FIRST_VIEW_PRODUCT)

    #Methods for search
    def enter_search_text(self, product_name):
        self.enter_text(self.SEARCH_INPUT, product_name)

    def click_search_button(self):
        self.click(self.SEARCH_BUTTON)

    def is_searched_products_section_visible(self):
        return self.is_visible(self.SEARCHED_PRODUCTS_TITLE)

    def are_search_results_visible(self, expected_keyword):
        # This will return a list of texts from all result items
        items = self.get_elements_text_list(self.SEARCH_RESULT_ITEMS)

        expected_clean = self.clean_text(expected_keyword)

        # Check if expected_keyword is found in all search result texts
        for product_text in items:
            product_clean = self.clean_text(product_text)
            if expected_clean not in product_clean:
                return False  # Mismatch found
        return True  # all items matched

    #Regular expression to convert unformated text
    @staticmethod
    def clean_text(text):
        return re.sub(r'[^a-z]', '', text.lower())
