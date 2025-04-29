import os
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from utilities.logger import Logger   # <<<<< Import your logger

logger = Logger.get_logger()   # <<<<< Initialize logger

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")

    def take_screenshot(self, action_name="screenshot"):
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        filename = f"screenshots/{action_name}_{timestamp}.png"
        self.driver.save_screenshot(filename)
        logger.info(f"📸 Screenshot saved: {filename}")

    def click(self, locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
            logger.info(f"Clicked on element: {locator}")
        except (TimeoutException, NoSuchElementException) as e:
            logger.error(f"Failed to click on element: {locator}. Error: {str(e)}")
            self.take_screenshot("click_failure")
            raise

    def enter_text(self, locator, text):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            element.clear()
            element.send_keys(text)
            logger.info(f"Entered text '{text}' into element: {locator}")
        except (TimeoutException, NoSuchElementException) as e:
            logger.error(f"Failed to enter text into element: {locator}. Error: {str(e)}")
            self.take_screenshot("enter_text_failure")
            raise

    def is_visible(self, locator):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            visible = element.is_displayed()
            logger.info(f"Element is visible: {locator}")
            print(visible)
            return visible
        except (TimeoutException, NoSuchElementException) as e:
            logger.error(f"Element not visible: {locator}. Error: {str(e)}")
            self.take_screenshot("is_visible_failure")
            raise

    def get_element_text(self, locator):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            text = element.text
            logger.info(f"Got text from element {locator}: '{text}'")
            print(text)
            return text
        except (TimeoutException, NoSuchElementException) as e:
            logger.error(f"Failed to get text from element: {locator}. Error: {str(e)}")
            self.take_screenshot("get_text_failure")
            raise

    def wait_for_element(self, locator):
        """Wait until an element is visible"""
        return self.wait.until(EC.visibility_of_element_located(locator))