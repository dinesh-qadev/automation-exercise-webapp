import pytest
from pageObjects.home_page import HomePage
from pageObjects.testcases_page import TestCasesPage
import allure


@allure.feature("Navigation")
@allure.severity(allure.severity_level.MINOR)
@allure.title("Navigate to Test Cases Page")
@allure.description("Verify user can navigate to the Test Cases page from home page.")
def test_verify_test_cases_page(browser):

    # Step 3: Verify that home page is visible successfully
    home_page = HomePage(browser)
    assert home_page.is_home_page_displayed(), "Home page is not visible"

    # Step 4: Click on 'Test Cases' button
    home_page.click_test_cases()

    # Step 5: Verify user is navigated to test cases page successfully
    test_cases_page = TestCasesPage(browser)
    assert test_cases_page.is_test_cases_page_displayed(), "Test Cases page is not visible"
