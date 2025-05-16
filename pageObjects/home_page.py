from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.base_page import BasePage


class HomePage(BasePage):
    # Locators
    LOGO = (By.XPATH, "//img[@alt='Website for automation practice']")
    HOME_LINK = (By.XPATH, "//a[@href='/' and contains(text(), 'Home')]")
    SIGNUP_LOGIN_BUTTON = (By.XPATH, "//a[@href='/login']")
    CONTACT_US_BUTTON = (By.XPATH, "//a[@href='/contact_us']")  # Locator for the 'Contact Us' button
    TEST_CASES_BUTTON = (By.XPATH, "//a[@href='/test_cases']")
    PRODUCTS_BUTTON = (By.XPATH, "//a[@href='/products']")
    CART_BUTTON = (By.XPATH, "//a[@href='/view_cart']")

    #Locators for subscription in home page
    SUBSCRIPTION_TEXT = (By.XPATH, "//h2[normalize-space()='Subscription']")
    EMAIL_INPUT = (By.ID, "susbscribe_email")
    SUBMIT_BUTTON = (By.ID, "subscribe")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@id='success-subscribe']//div[contains(text(), 'successfully subscribed')]")

    #Locators for TestCase_013
    VIEW_PRODUCT_LINK = (By.XPATH, "(//a[contains(text(),'View Product')])[1]")

    # Locators for TestCase_018
    CATEGORY_SECTION = (By.CSS_SELECTOR, "div.left-sidebar > h2")
    MAIN_CATEGORY_TOGGLE = (By.XPATH, "//a[normalize-space()='{category}']")
    SUB_CATEGORY_LINK = (By.XPATH, "//div[@id='{category_id}']//a[contains(text(),'{subcategory}')]")

    def __init__(self, driver):
        #self.driver = driver
        super().__init__(driver)

    # Actions
    def is_logo_displayed(self):
        """Checks if the logo is visible on the homepage."""
        return self.is_visible(self.LOGO)

    def click_signup_login(self):
        """Clicks on the 'Signup / Login' button."""
        self.click(self.SIGNUP_LOGIN_BUTTON)

    def is_home_link_active(self):
        """Checks if the 'Home' link is active (based on its color)."""
        home_link_element = self.driver.find_element(*self.HOME_LINK)

        # Get the style attribute of the "Home" link
        style = home_link_element.get_attribute("style")

        # Check if the color is orange (active state)
        return "color: orange" in style

    def is_home_page_displayed(self):
        """Verifies that the 'Home' link is active (orange color), indicating the homepage is displayed."""
        # Check if the 'Home' link is active (has the orange color)
        return self.is_home_link_active()

    def click_contact_us(self):
        """Click on the 'Contact Us' button to navigate to the contact us page"""
        self.click(self.CONTACT_US_BUTTON)

    def click_test_cases(self):
        """Clicks on the 'TestCases' button"""
        self.click(self.TEST_CASES_BUTTON)

    def click_products(self):
        """Clicks on the 'Product' button"""
        self.click(self.PRODUCTS_BUTTON)

    #Pageobject Methods for Subscription verification in Home/Cart Page
    def scroll_to_footer(self):
        """Scrolls to bottom of the page"""
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def is_subscription_text_visible(self):
        """Check visibility of Subscription text"""
        return self.is_visible(self.SUBSCRIPTION_TEXT)

    def subscribe_with_email(self, email):
        """enter email address and clicks to submit"""
        self.enter_text(self.EMAIL_INPUT, email)
        self.click(self.SUBMIT_BUTTON)
        # with open("page_source.html", "w", encoding="utf-8") as f:
        #     f.write(self.driver.page_source) #This is written to find out alert text from DOM

    def get_success_message_text(self, timeout=5):
        """When subscribed, captures a successful text"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(self.SUCCESS_MESSAGE)
            )

            return element.text.strip()
        except Exception as e:
            return e

    def click_cart_button(self):
        """Clicks on the 'Cart' button"""
        self.click(self.CART_BUTTON)

    #Method for TestCase_013
    def click_view_product(self):
        self.click(self.VIEW_PRODUCT_LINK)

    # Methods for TestCase_018
    def is_category_section_visible(self):
        """Verify the left sidebar 'CATEGORY' title is visible."""
        return self.is_visible(self.CATEGORY_SECTION)

    def expand_main_category(self, category_name):
        """
        Expands a main category (like 'Women').

        :param category_name: e.g., 'Women'
        """
        toggle_locator = (
            By.XPATH,
            self.MAIN_CATEGORY_TOGGLE[1].format(category=category_name)
        )
        self.click(toggle_locator)

    def click_sub_category(self, category_name, sub_category_name):
        """
        Clicks on a sub-category (e.g., 'Dress' under 'Women').

        :param category_name: e.g., 'Women'
        :param sub_category_name: e.g., 'Dress'
        """
        category_id = category_name.strip().replace(" ", "")
        sub_cat_locator = (
            By.XPATH,
            self.SUB_CATEGORY_LINK[1].format(category_id=category_id, subcategory=sub_category_name)
        )
        self.click(sub_cat_locator)
