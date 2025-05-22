from pageObjects.home_page import HomePage
from pageObjects.signup_login_page import SignupLoginPage
from utilities.data_loader import load_test_data
import allure


@allure.feature("User Authentication")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Logout User Successfully")
@allure.description("Verify logged in user can logout and is redirected to login page.")
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
    user_info = load_test_data("users.json")
    correct_credential = user_info["valid_user"]
    login.login_user(
        email=correct_credential["email"],
        password=correct_credential["password"]
    )

    # Step 8: Verify that 'Logged in as username' is visible
    name = correct_credential["name"]
    assert login.is_logged_in_as_user(name), f"'Logged in as {name}' not visible"

    # Step 9: Click 'Logout' button
    login.click_logout()

    # Step 10: Verify user is navigated back to login page
    assert login.is_login_header_visible(), "User is not redirected to login page after logout"
