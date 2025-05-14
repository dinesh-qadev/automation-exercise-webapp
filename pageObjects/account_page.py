from selenium.webdriver.common.by import By
from pageObjects.base_page import BasePage


class AccountPage(BasePage):
    ACCOUNT_CREATED = (By.XPATH, "//b[text()='Account Created!']")
    CONTINUE_BUTTON = (By.XPATH, "//a[@data-qa='continue-button']")
    #LOGGED_IN_AS = (By.XPATH, f"//a[contains(text(),'Logged in as {NAME}')]")
    DELETE_ACCOUNT_BUTTON = (By.XPATH, "//a[@href='/delete_account']")
    ACCOUNT_DELETED = (By.XPATH, "//b[text()='Account Deleted!']")
    CONTINUE_AFTER_DELETE = (By.XPATH, "//a[@data-qa='continue-button']")

    #Dynamic Locator
    def get_logged_in_as_locator(self, user_name):
        return By.XPATH, f"//a[normalize-space(.)='Logged in as {user_name}']"

    def is_account_created_visible(self):
        return self.is_visible(self.ACCOUNT_CREATED)

    def click_continue(self):
        self.click(self.CONTINUE_BUTTON)

    def is_logged_in_as_visible(self, user_name):
        return self.is_visible(self.get_logged_in_as_locator(user_name))

    def click_delete_account(self):
        self.click(self.DELETE_ACCOUNT_BUTTON)

    def is_account_deleted_visible(self):
        return self.is_visible(self.ACCOUNT_DELETED)

    def click_continue_after_delete(self):
        self.click(self.CONTINUE_AFTER_DELETE)