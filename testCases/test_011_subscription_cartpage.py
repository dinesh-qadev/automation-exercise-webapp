from pageObjects.home_page import HomePage
from utilities.data_loader import load_test_data


def test_subscription_in_cart_page(browser):
    home = HomePage(browser)

    # Step 1: Navigate to Cart page
    home.click_cart_button()

    # Step 2: Scroll to footer
    home.scroll_to_footer()

    # Step 3: Verify 'SUBSCRIPTION' text is visible
    assert home.is_subscription_text_visible(), "'SUBSCRIPTION' text not visible"

    # Step 4: Enter email and click subscribe
    user_info = load_test_data("users.json")
    correct_credential = user_info["valid_user"]
    home.subscribe_with_email(
        email=correct_credential["email"]
    )

    # Step 5: Verify success message
    message = home.get_success_message_text()

    assert message == "You have been successfully subscribed!", f"Unexpected message: {message}"
