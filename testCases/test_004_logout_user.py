from pageObjects.home_page import HomePage
from pageObjects.signup_login_page import SignupLoginPage


def test_logout_user(browser):
    home = HomePage(browser)
    login = SignupLoginPage(browser)

    # Step 3: Verify that home page is visible successfully
    assert home.is_home_page_displayed(), "Home page is not visible"

    # Step 4: Click on 'Signup / Login' button
    home.click_signup_login()

    # Step 5: Verify 'Login to your account' is visible
    assert login.is_login_header_visible(), "'Login to your account' is not visible"

    # Step 6: Enter correct email address and password
    login.login_user("djoc301@gmail.com", "1234")

    # Step 8: Verify that 'Logged in as username' is visible
    assert login.is_logged_in_as_user("Dinesh"), "'Logged in as Dinesh' not visible"

    # Step 9: Click 'Logout' button
    login.click_logout()

    # Step 10: Verify user is navigated back to login page
    assert login.is_login_header_visible(), "User is not redirected to login page after logout"
