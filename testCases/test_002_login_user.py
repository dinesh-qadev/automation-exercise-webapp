import pytest
from pageObjects.home_page import HomePage
from pageObjects.signup_login_page import SignupLoginPage
from pageObjects.account_page  import AccountPage


def test_002_login_user_with_correct_credentials(browser):
    # Initialize page objects
    home_page = HomePage(browser)
    signup_login_page = SignupLoginPage(browser)
    account_page = AccountPage(browser)

    # Step 1: Verify home page is displayed by checking if 'Home' link is active
    assert home_page.is_home_page_displayed(), "Home page is not visible or 'Home' link is not active"

    # Step 2: Click on 'Signup / Login' button
    home_page.click_signup_login()

    # Step 3: Verify 'Login to your account' is visible on the login page
    assert signup_login_page.is_login_header_visible(), "'Login to your account' header not visible"

    # Step 4: Enter correct email and password in the login form
    email = "djoc301@gmail.com"  # Replace with valid email
    password = "1234"        # Replace with valid password
    signup_login_page.login_user(email=email, password=password)

    # Step 5: Verify 'Logged in as username' is visible after login
    assert account_page.is_logged_in_as_visible(), "'Logged in as username' message is not visible"

    # Step 6: Click 'Delete Account' button to delete the account
    account_page.click_delete_account()

    # Step 7: Verify 'ACCOUNT DELETED!' message is visible after account deletion
    assert account_page.is_account_deleted_visible(), "'ACCOUNT DELETED!' message is not visible"
