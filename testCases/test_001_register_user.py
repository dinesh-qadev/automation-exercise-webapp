import time
import random
from pageObjects.home_page import HomePage
from pageObjects.signup_login_page import SignupLoginPage
from pageObjects.account_page import AccountPage
from utilities.data_generator import generate_random_email
from utilities.data_loader import load_test_data


def test_register_user(browser):
    home_page = HomePage(browser)
    signup_login_page = SignupLoginPage(browser)
    account_page = AccountPage(browser)

    # Load data from json fie
    user_data = load_test_data("users.json")
    account_info = user_data["account_info"]
    address_info = user_data["address_info"]

    # Step 3
    assert home_page.is_logo_displayed(), "Home page is not visible"

    # Step 4
    home_page.click_signup_login()

    # Step 5
    assert signup_login_page.is_new_user_signup_visible(), "'New User Signup!' is not visible"

    # Step 6-7
    #random_email = f"user{random.randint(1000,9999)}@test.com"
    random_email = generate_random_email()
    signup_login_page.signup(
        name=address_info["firstname"]+address_info["lastname"],
        email=random_email
    )

    # Step 8
    assert signup_login_page.is_enter_account_info_visible(), "'ENTER ACCOUNT INFORMATION' is not visible"

    # Step 9-11
    signup_login_page.fill_account_info(
        password=account_info["password"],
        day=account_info["day"],
        month=account_info["month"],
        year=account_info["year"]
    )

    # Step 12
    signup_login_page.fill_address_info(
        firstname=address_info["firstname"],
        lastname=address_info["lastname"],
        company=address_info["company"],
        address1=address_info["address1"],
        address2=address_info["address2"],
        country=address_info["country"],
        state=address_info["state"],
        city=address_info["city"],
        zipcode=address_info["zipcode"],
        mobile=address_info["mobile"]
    )

    # Step 13
    signup_login_page.click_create_account()

    # Step 14
    assert account_page.is_account_created_visible(), "'ACCOUNT CREATED!' is not visible"

    # Step 15
    account_page.click_continue()

    # Step 16
    assert account_page.is_logged_in_as_visible(user_name=address_info["firstname"]+address_info["lastname"]), "'Logged in as username' is not visible"

    # Step 17
    account_page.click_delete_account()

    # Step 18
    assert account_page.is_account_deleted_visible(), "'ACCOUNT DELETED!' is not visible"

    account_page.click_continue_after_delete()

    # Optionally: Wait to see result before browser closes
    time.sleep(2)
