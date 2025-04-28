import time
import random
from pageObjects.home_page import HomePage
from pageObjects.signup_login_page import SignupLoginPage
from pageObjects.account_page import AccountPage


def test_register_user(browser):
    home_page = HomePage(browser)
    signup_login_page = SignupLoginPage(browser)
    account_page = AccountPage(browser)

    # Step 3
    assert home_page.is_logo_displayed(), "Home page is not visible"

    # Step 4
    home_page.click_signup_login()

    # Step 5
    assert signup_login_page.is_new_user_signup_visible(), "'New User Signup!' is not visible"

    # Step 6-7
    random_email = f"user{random.randint(1000,9999)}@test.com"
    signup_login_page.signup(name="TestUser", email=random_email)

    # Step 8
    assert signup_login_page.is_enter_account_info_visible(), "'ENTER ACCOUNT INFORMATION' is not visible"

    # Step 9-11
    signup_login_page.fill_account_info(password="Test1234", day="1", month="January", year="2000")

    # Step 12
    signup_login_page.fill_address_info(
        firstname="Test",
        lastname="User",
        company="TestCompany",
        address1="123 Street",
        address2="Suite 456",
        country="Canada",
        state="Ontario",
        city="Toronto",
        zipcode="M5V2T6",
        mobile="1234567890"
    )

    # Step 13
    signup_login_page.click_create_account()

    # Step 14
    assert account_page.is_account_created_visible(), "'ACCOUNT CREATED!' is not visible"

    # Step 15
    account_page.click_continue()

    # Step 16
    assert account_page.is_logged_in_as_visible(), "'Logged in as username' is not visible"

    # Step 17
    account_page.click_delete_account()

    # Step 18
    assert account_page.is_account_deleted_visible(), "'ACCOUNT DELETED!' is not visible"

    account_page.click_continue_after_delete()

    # Optionally: Wait to see result before browser closes
    time.sleep(2)
