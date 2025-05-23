import pytest
from selenium.webdriver.common.by import By
from pageObjects.home_page import HomePage
from pageObjects.signup_login_page import SignupLoginPage
from utilities.data_loader import load_test_data
import allure


@allure.feature("User Authentication")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Login User with Incorrect Credentials")
@allure.description("Verify error message appears when user logs in with invalid email/password.")
def test_003_login_user_with_incorrect_credentials(browser):
    # Initialize page objects
    home_page = HomePage(browser)
    signup_login_page = SignupLoginPage(browser)

    # Step 1: Verify home page is displayed by checking if 'Home' link is active
    assert home_page.is_home_page_displayed(), "Home page is not visible or 'Home' link is not active"

    # Step 2: Click on 'Signup / Login' button
    home_page.click_signup_login()

    # Step 3: Verify 'Login to your account' is visible on the login page
    assert signup_login_page.is_login_header_visible(), "'Login to your account' header not visible"

    # Step 4: Enter incorrect email and password in the login form\
    user_info = load_test_data("users.json")
    incorrect_info = user_info["invalid_user"]
    signup_login_page.login_user(
        email=incorrect_info["email"],
        password=incorrect_info["password"]
    )

    # Step 5: Verify error message 'Your email or password is incorrect!' is visible
    error_message_locator = (By.XPATH, "//p[contains(text(), 'Your email or password is incorrect!')]")
    error_message = signup_login_page.wait_for_element(error_message_locator)
    assert error_message.is_displayed(), "Error message 'Your email or password is incorrect!' is not visible"
