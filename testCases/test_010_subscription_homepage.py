# tests/test_subscription_home.py
from pageObjects.home_page import HomePage


def test_subscription_in_home_page(browser):
    home = HomePage(browser)

    # Step 3: Verify home page is loaded
    home.is_home_page_displayed()

    # Step 4: Scroll to footer
    home.scroll_to_footer()

    # Step 5: Verify 'SUBSCRIPTION' text is visible
    assert home.is_subscription_text_visible(), "'SUBSCRIPTION' text not visible"

    # Step 6: Enter email and click arrow
    home.subscribe_with_email("testemail@example.com")

    # Step 7: Verify success message
    message = home.get_success_message_text()

    assert message == "You have been successfully subscribed!", f"Unexpected message: {message}"
