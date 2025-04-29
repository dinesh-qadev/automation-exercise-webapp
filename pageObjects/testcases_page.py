from selenium.webdriver.common.by import By
from .base_page import BasePage


class TestCasesPage(BasePage):
    TEST_CASES_HEADER = (By.XPATH, "//b[normalize-space()='Test Cases']")

    def __init__(self, driver):
        self.driver = driver

    def is_test_cases_page_displayed(self):
        return self.is_visible(self.TEST_CASES_HEADER)