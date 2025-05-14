from pageObjects.home_page import HomePage
from pageObjects.product_page import ProductsPage
from pageObjects.cart_page import CartPage
from pageObjects.signup_login_page import SignupLoginPage
from pageObjects.account_page import AccountPage
from pageObjects.checkoutPage import CheckoutPage
from pageObjects.payment_page import PaymentPage
from utilities.data_loader import load_test_data


def test_place_order_login_before_checkout(browser):
    home = HomePage(browser)
    product = ProductsPage(browser)
    cart = CartPage(browser)
    signuplogin = SignupLoginPage(browser)
    account = AccountPage(browser)
    checkout = CheckoutPage(browser)
    payment = PaymentPage(browser)

    # Step 1–3: Verify home page
    assert home.is_home_page_displayed()

    # Step 4: Click 'Signup / Login'
    home.click_signup_login()

    # Fill email, password and click 'Login' button
    user_info = load_test_data("users.json")
    correct_credential = user_info["valid_user"]
    signuplogin.login_user(
        email=correct_credential["email"],
        password=correct_credential["password"])

    # Verify 'Logged in as username' at top
    assert account.is_logged_in_as_visible(
        user_name=correct_credential["name"]), "'Logged in as username' is not visible"

    # Add products to cart
    expected_product_name, expected_price = product.hover_and_add_to_cart_and_get_price(product_index=1)

    #Click 'Cart' button
    product.click_view_cart()

    # Verify that cart page is displayed
    assert cart.is_cart_page_visible(), "Cart page URL is incorrect or not loaded"

    # Click Proceed To Checkout
    cart.click_proceed_to_checkout()

    #  Verify Address Details and Review Your Order
    assert checkout.is_address_and_review_visible(), f"Review section is not visible in checkout page"

    #  Enter description in comment text area and click 'Place Order'
    checkout.enter_comment("Please deliver between 9AM and 5PM")
    checkout.click_place_order()

    #  Enter payment details: Name on Card, Card Number, CVC, Expiration date
    payment_test_data = load_test_data("payment_test_data.json")
    card_details = payment_test_data["test_payment_data"]
    payment.fill_payment_form(card_details)

    #  Click 'Pay and Confirm Order' button
    payment.click_pay_and_confirm()

    #  Verify success message 'Congratulations! Your order has been confirmed!'
    payment.verify_order_success_message()

