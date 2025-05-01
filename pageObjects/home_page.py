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

    #Locators for testcase subscription in home page
    SUBSCRIPTION_TEXT = (By.XPATH, "//h2[normalize-space()='Subscription']")
    EMAIL_INPUT = (By.ID, "susbscribe_email")
    SUBMIT_BUTTON = (By.ID, "subscribe")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@id='success-subscribe']//div[contains(text(), 'successfully subscribed')]")

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

    # Cliks on Test Cases menu option
    def click_test_cases(self):
        self.click(self.TEST_CASES_BUTTON)

    #Click on product menu
    def click_products(self):
        self.click(self.PRODUCTS_BUTTON)

    #Pageobject Methods for Subscription verification in Homepage
    def scroll_to_footer(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def is_subscription_text_visible(self):
        return self.is_visible(self.SUBSCRIPTION_TEXT)

    def subscribe_with_email(self, email):
        self.enter_text(self.EMAIL_INPUT, email)
        self.click(self.SUBMIT_BUTTON)
        # with open("page_source.html", "w", encoding="utf-8") as f:
        #     f.write(self.driver.page_source) #This is written to find out alert text from DOM

    def get_success_message_text(self, timeout=5):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(self.SUCCESS_MESSAGE)
            )

            return element.text.strip()
        except Exception as e:
            return e


