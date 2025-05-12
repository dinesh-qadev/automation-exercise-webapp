from selenium.webdriver.common.by import By
from pageObjects.base_page import BasePage
from utilities.text_formatter import clean_text


class ProductsPage(BasePage):
    #Locators
    PRODUCTS_HEADER = (By.XPATH, "//h2[normalize-space()='All Products']")
    PRODUCT_LIST = (By.XPATH, "//div[@class='features_items']//div[@class='productinfo text-center']")
    FIRST_VIEW_PRODUCT = (By.XPATH, "(//a[contains(text(),'View Product')])[1]")

    #Locatior for testcase_009
    SEARCH_INPUT = (By.ID, 'search_product')
    SEARCH_BUTTON = (By.ID, 'submit_search')
    SEARCHED_PRODUCTS_TITLE = (By.XPATH, "//h2[text()='Searched Products']")
    SEARCH_RESULT_ITEMS = (By.XPATH, "//div[@class='productinfo text-center']/p")

    # Locators for Test_0012
    PRODUCT_CARD_1 = (By.XPATH, "(//div[@class='product-image-wrapper'])[1]")
    ADD_TO_CART_BUTTON_1 = (By.XPATH,
                            "(//div[@class='product-image-wrapper'])[1]//div[@class='product-overlay']//a["
                            "@data-product-id='1']")
    PRICE_1 = (By.XPATH, "(//div[@class='productinfo text-center'])[1]//h2")

    PRODUCT_CARD_2 = (By.XPATH, "(//div[@class='product-image-wrapper'])[2]")
    ADD_TO_CART_BUTTON_2 = (By.XPATH,
                            "(//div[@class='product-image-wrapper'])[2]//div[@class='product-overlay']//a["
                            "@data-product-id='2']")
    PRICE_2 = (By.XPATH, "(//div[@class='productinfo text-center'])[2]//h2")

    CONTINUE_SHOPPING_BUTTON = (By.XPATH, "//button[text()='Continue Shopping']")
    VIEW_CART_BUTTON = (By.XPATH, "//u[text()='View Cart']")

    def __init__(self, driver):
        super().__init__(driver)

    def is_all_products_page_displayed(self):
        return self.is_visible(self.PRODUCTS_HEADER)

    def is_product_list_visible(self):
        return self.is_visible(self.PRODUCT_LIST)

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

        expected_clean = clean_text(expected_keyword)

        # Check if expected_keyword is found in all search result texts
        for product_text in items:
            product_clean = clean_text(product_text)
            if expected_clean not in product_clean:
                return False  # Mismatch found
        return True  # all items matched

    #Actions for Tes_0012
    def hover_and_add_to_cart_and_get_price(self, product_index):
        print("hover_and_add_to_cart_and_get_price execution started")
        if product_index == 1:

            price_element = self.wait_for_element(self.PRICE_1) #self.wait.until(EC.visibility_of_element_located(self.PRICE_1))
            price = price_element.text.strip()
            print(price)
            self.hover(self.PRODUCT_CARD_1)
            self.click(self.ADD_TO_CART_BUTTON_1)
            print("added to cart")
        elif product_index == 2:
            price_element = self.wait_for_element(self.PRICE_2) #self.wait.until(EC.visibility_of_element_located(self.PRICE_2))
            price = price_element.text.strip()
            self.hover(self.PRODUCT_CARD_2)
            self.click(self.ADD_TO_CART_BUTTON_2)
        return price

    def click_continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING_BUTTON)
        print("continue clicked")

    def click_view_cart(self):
        self.click(self.VIEW_CART_BUTTON)
