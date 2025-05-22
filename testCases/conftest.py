import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def browser():
    # Setup Chrome browser
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.automationexercise.com/")
    yield driver
    # Teardown
    driver.quit()
    # https://prnt.sc/jYKIcLDQFL03


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == 'call' and report.failed:
        driver = item.funcargs['browser']
        allure.attach(driver.get_screenshot_as_png(),
                      name="screenshot_on_failure",
                      attachment_type=allure.attachment_type.PNG)