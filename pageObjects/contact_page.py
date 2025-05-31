from selenium.webdriver.common.by import By
from pageObjects.base_page import BasePage

class ContactUsPage(BasePage):
    # Locators for the Contact Us page
    GET_IN_TOUCH_HEADER = (By.XPATH, "//h2[text()='Get In Touch']")
    NAME_INPUT = (By.XPATH, "//input[@name='name']")
    EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
    SUBJECT_INPUT = (By.XPATH, "//input[@name='subject']")
    MESSAGE_TEXTAREA = (By.XPATH, "//textarea[@name='message']")
    UPLOAD_FILE_INPUT = (By.XPATH, "//input[@name='upload_file']")
    SUBMIT_BUTTON = (By.XPATH, "//input[@name='submit']")
    OK_BUTTON = (By.XPATH, "//button[text()='OK']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(text(),'Success! Your details have been submitted successfully.')]")
    HOME_BUTTON = (By.XPATH, "//a[@href='/' and contains(text(), 'Home')]")

    def __init__(self, driver):
        super().__init__(driver)

    # Action to verify 'GET IN TOUCH' header
    def is_get_in_touch_header_visible(self):
        return self.is_visible(self.GET_IN_TOUCH_HEADER)

    # Action to fill in the contact form
    def fill_contact_form(self, name, email, subject, message):
        self.enter_text(self.NAME_INPUT, name)
        self.enter_text(self.EMAIL_INPUT, email)
        self.enter_text(self.SUBJECT_INPUT, subject)
        self.enter_text(self.MESSAGE_TEXTAREA, message)

    # Action to upload a file
    def upload_file(self, file_path):
        self.enter_text(self.UPLOAD_FILE_INPUT, file_path)

    # Action to click the 'Submit' button
    def click_submit_button(self):
        self.click(self.SUBMIT_BUTTON)

    # Action to click 'OK' on the success message
    def click_ok_button(self):
        self.click(self.OK_BUTTON)

    # Action to check if success message is visible
    def is_success_message_visible(self):
        return self.is_visible(self.SUCCESS_MESSAGE)

    # Action to click on the 'Home' button
    def click_home_button(self):
        self.click(self.HOME_BUTTON)
