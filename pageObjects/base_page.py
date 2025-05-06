import os
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from utilities.logger import Logger   # <<<<< Import your logger
from selenium.webdriver.common.action_chains import ActionChains


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

    def submit_enter(self, locator):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            element.send_keys(Keys.ENTER)
            logger.info(f"Pressed ENTER in element: {locator}")
        except (TimeoutException, NoSuchElementException) as e:
            logger.error(f"Failed to press ENTER in element: {locator}. Error: {str(e)}")
            self.take_screenshot("submit_enter_failure")
            raise

    def get_elements_text_list(self, locator):
        try:
            elements = self.wait.until(EC.presence_of_all_elements_located(locator))
            texts = []
            for el in elements:
                text = el.text.strip()
                if text:  # Check if the text is not empty
                    texts.append(text)
            #print(text)
            return texts
        except (TimeoutException, NoSuchElementException) as e:
            logger.error(f"Failed to get texts from elements: {locator}. Error: {str(e)}")
            self.take_screenshot("get_elements_text_list_failure")
            raise

    def is_text_present_in_element(self, locator, expected_text):
        try:
            result = self.wait.until(EC.text_to_be_present_in_element(locator, expected_text))
            logger.info(f"Text '{expected_text}' is present in element: {locator}")
            return result
        except (TimeoutException, NoSuchElementException) as e:
            logger.error(f"Text '{expected_text}' not found in element: {locator}. Error: {str(e)}")
            self.take_screenshot("text_presence_failure")
            raise

    def get_attribute(self, locator, attribute_name):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.get_attribute(attribute_name)

    def hover(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        ActionChains(self.driver).move_to_element(element).perform()
