from selenium.webdriver.common.by import By
from pageObjects.base_page import BasePage

class BrandsPage(BasePage):

    # Locators
    BRANDS_SECTION_TITLE = (By.XPATH, "//h2[text()='Brands']")
    BRAND_LINKS = (By.XPATH, "//div[@class='brands-name']//a")
    BRAND_PRODUCTS_HEADER = (By.XPATH, "//h2[contains(text(),'Brand -')]")
    PRODUCT_LINKS = (By.XPATH, "//div[@class='features_items']//a[@href and text()='View Product']")
    PRODUCT_BRAND_NAME = (By.XPATH, "//body//section//p[4]")

    # def __init__(self, driver):
    #     super().__init__(driver)

    def is_brands_section_visible(self):
        return self.is_visible(self.BRANDS_SECTION_TITLE)

    def click_brand_by_index(self, index):
        brands = self.get_elements(self.BRAND_LINKS)
        brand_text = brands[index].text.strip()  # e.g. "(6)\nPOLO"
        brand_name = brand_text.split('\n')[-1].strip()  # Take last line, the actual brand name
        self.click(brands[index])
        return brand_name

    def is_brand_products_header_visible(self, brand_name):
        header_text = self.get_element_text(self.BRAND_PRODUCTS_HEADER)

        return brand_name.lower() in header_text.lower()

    def click_first_product_view_link(self):
        product_links = self.get_elements(self.PRODUCT_LINKS)
        self.click(product_links[0])

    def get_product_brand_name(self):
        text = self.get_element_text(self.PRODUCT_BRAND_NAME)
        if "Brand:" in text:
            return text.replace("Brand:", "").strip()
        return ""
