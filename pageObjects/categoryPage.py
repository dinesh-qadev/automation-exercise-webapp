from selenium.webdriver.common.by import By
from pageObjects.base_page import BasePage  # Assuming this is your base_page.py


class CategoryPage(BasePage):
    CATEGORY_HEADING = (By.CSS_SELECTOR, ".features_items h2.title.text-center")
    PRODUCT_VIEW_BUTTONS = (By.XPATH, "//a[text()='View Product']")

    def get_category_heading_text(self):
        return self.get_element_text(self.CATEGORY_HEADING)

    def get_all_visible_product_links(self):
        elements = self.get_elements(self.PRODUCT_VIEW_BUTTONS)
        product_links = []
        for el in elements:
            link = el.get_attribute("href")
            if link:  # avoid None values
                product_links.append(link)
        return product_links


