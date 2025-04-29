from selenium.webdriver.common.by import By
from pageObjects.base_page import BasePage


class HomePage(BasePage):
    # Locators
    LOGO = (By.XPATH, "//img[@alt='Website for automation practice']")
    HOME_LINK = (By.XPATH, "//a[@href='/' and contains(text(), 'Home')]")
    SIGNUP_LOGIN_BUTTON = (By.XPATH, "//a[@href='/login']")
    CONTACT_US_BUTTON = (By.XPATH, "//a[@href='/contact_us']")  # Locator for the 'Contact Us' button
    TEST_CASES_BUTTON = (By.XPATH, "//a[@href='/test_cases']")

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