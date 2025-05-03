from selenium.webdriver.common.by import By
from pageObjects.base_page import BasePage


class SignupLoginPage(BasePage):
    # Locators for signup
    NEW_USER_SIGNUP = (By.XPATH, "//h2[text()='New User Signup!']")
    NAME_INPUT = (By.XPATH, "//input[@data-qa='signup-name']")
    EMAIL_INPUT = (By.XPATH, "//input[@data-qa='signup-email']")
    SIGNUP_BUTTON = (By.XPATH, "//button[@data-qa='signup-button']")
    ENTER_ACCOUNT_INFO = (By.XPATH, "//b[text()='Enter Account Information']")

    TITLE_MR = (By.ID, "id_gender1")
    PASSWORD = (By.ID, "password")
    DAYS = (By.ID, "days")
    MONTHS = (By.ID, "months")
    YEARS = (By.ID, "years")
    NEWSLETTER_CHECKBOX = (By.ID, "newsletter")
    SPECIAL_OFFERS_CHECKBOX = (By.ID, "optin")

    FIRSTNAME = (By.ID, "first_name")
    LASTNAME = (By.ID, "last_name")
    COMPANY = (By.ID, "company")
    ADDRESS1 = (By.ID, "address1")
    ADDRESS2 = (By.ID, "address2")
    COUNTRY = (By.ID, "country")
    STATE = (By.ID, "state")
    CITY = (By.ID, "city")
    ZIPCODE = (By.ID, "zipcode")
    MOBILE_NUMBER = (By.ID, "mobile_number")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[@data-qa='create-account']")

    # Locators for Login
    LOGIN_HEADER = (By.XPATH, "//h2[text()='Login to your account']")
    LOGIN_EMAIL_INPUT = (By.XPATH, "//input[@data-qa='login-email']")
    LOGIN_PASSWORD_INPUT = (By.XPATH, "//input[@data-qa='login-password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@data-qa='login-button']")

    #Locators for Logout
    LOGGED_IN_TEXT = (By.XPATH, "//a[contains(text(), 'Logged in as')]")
    LOGOUT_BUTTON = (By.XPATH, "//a[@href='/logout']")

    #Locatior for "email already exist" validation
    EMAIL_EXISTS_ERROR = (By.XPATH, "//p[text()='Email Address already exist!']")

    def is_new_user_signup_visible(self):
        return self.is_visible(self.NEW_USER_SIGNUP)

    def signup(self, name, email):
        self.enter_text(self.NAME_INPUT, name)
        self.enter_text(self.EMAIL_INPUT, email)
        self.click(self.SIGNUP_BUTTON)

    def is_enter_account_info_visible(self):
        return self.is_visible(self.ENTER_ACCOUNT_INFO)

    def fill_account_info(self, password, day, month, year):
        self.click(self.TITLE_MR)
        self.enter_text(self.PASSWORD, password)
        self.driver.find_element(*self.DAYS).send_keys(day)
        self.driver.find_element(*self.MONTHS).send_keys(month)
        self.driver.find_element(*self.YEARS).send_keys(year)
        self.click(self.NEWSLETTER_CHECKBOX)
        self.click(self.SPECIAL_OFFERS_CHECKBOX)

    def fill_address_info(self, firstname, lastname, company, address1, address2, country, state, city, zipcode, mobile):
        self.enter_text(self.FIRSTNAME, firstname)
        self.enter_text(self.LASTNAME, lastname)
        self.enter_text(self.COMPANY, company)
        self.enter_text(self.ADDRESS1, address1)
        self.enter_text(self.ADDRESS2, address2)
        self.driver.find_element(*self.COUNTRY).send_keys(country)
        self.enter_text(self.STATE, state)
        self.enter_text(self.CITY, city)
        self.enter_text(self.ZIPCODE, zipcode)
        self.enter_text(self.MOBILE_NUMBER, mobile)

    def click_create_account(self):
        self.click(self.CREATE_ACCOUNT_BUTTON)

    # Login Methods
    def is_login_header_visible(self):
        return self.is_visible(self.LOGIN_HEADER)

    def login_user(self, email, password):
        self.enter_text(self.LOGIN_EMAIL_INPUT, email)
        self.enter_text(self.LOGIN_PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    ''' Methods for Testcase_004'''
    def is_logged_in_as_user(self, username):
        """Checks if 'Logged in as username' is visible"""
        return self.is_text_present_in_element(self.LOGGED_IN_TEXT, username)

    def click_logout(self):
        self.click(self.LOGOUT_BUTTON)

    ''' Method for "Email already exist" validation text'''

    def is_email_exists_error_visible(self):
        return self.is_visible(self.EMAIL_EXISTS_ERROR)
