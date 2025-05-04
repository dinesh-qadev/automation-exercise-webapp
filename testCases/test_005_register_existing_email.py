from pageObjects.home_page import HomePage
from pageObjects.signup_login_page import SignupLoginPage


def test_register_user_with_existing_email(browser):
    home = HomePage(browser)
    login_page = SignupLoginPage(browser)

    # Step 3: Verify that home page is visible
    assert home.is_home_page_displayed(), "Home page is not visible"

    # Step 4: Click on 'Signup / Login' button
    home.click_signup_login()

    # Step 5: Verify 'New User Signup!' is visible
    assert login_page.is_new_user_signup_visible(), "'New User Signup!' is not visible"

    # Step 6 and 7: Enter name and already registered email address and clicks on Signup button
    login_page.signup("Dinesh", "djoc301@gmail.com")

    # Step 8: Verify error 'Email Address already exist!' is visible
    assert login_page.is_email_exists_error_visible(), "'Email Address already exist!' error not displayed"



