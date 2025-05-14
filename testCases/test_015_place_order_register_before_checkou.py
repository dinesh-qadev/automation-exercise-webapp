from pageObjects.home_page import HomePage
from pageObjects.product_page import ProductsPage
from pageObjects.cart_page import CartPage
from pageObjects.signup_login_page import SignupLoginPage
from pageObjects.account_page import AccountPage
from pageObjects.checkoutPage import CheckoutPage
from pageObjects.payment_page import PaymentPage
from utilities.data_generator import generate_random_email
from utilities.data_loader import load_test_data
from utilities.utils import compare_data


def test_place_order_register_before_checkout(browser):
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

    # Step 5: Fill all details in Signup and create account
    random_email = generate_random_email()
    # Load data from json fie
    user_data = load_test_data("users.json")
    account_info = user_data["account_info"]
    address_info = user_data["address_info"]
    signuplogin.signup(
        name=address_info["firstname"] + address_info["lastname"],
        email=random_email)

    signuplogin.fill_account_info(
        password=account_info["password"],
        day=account_info["day"],
        month=account_info["month"],
        year=account_info["year"]
    )
    signuplogin.fill_address_info(
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
    signuplogin.click_create_account()

    # Verify 'ACCOUNT CREATED!' and click 'Continue' button
    assert account.is_account_created_visible(), "'ACCOUNT CREATED!' is not visible"
    account.click_continue()

    # Verify ' Logged in as username' at top
    assert account.is_logged_in_as_visible(
        user_name=address_info["firstname"] + address_info["lastname"]), "'Logged in as username' is not visible"

    # Add products to cart
    expected_product_name, expected_price = product.hover_and_add_to_cart_and_get_price(product_index=1)

    # Click 'Cart' button
    product.click_view_cart()

    #Verify that cart page is displayed
    assert cart.is_cart_page_visible(), "Cart page URL is incorrect or not loaded"

    # Click Proceed To Checkout
    cart.click_proceed_to_checkout()

    # Verify Address Details and Review Your Order
    assert checkout.is_address_and_review_visible(), f"Review section is not visible in checkout page"
    expected_address = f"{address_info['firstname']} {address_info['lastname']} {address_info['company']} {address_info['address1']} {address_info['address2']} {address_info['city']} {address_info['state']} {address_info['zipcode']} {address_info['country']} {address_info['mobile']}"
    actual_address = checkout.get_delivery_address_text()
    assert compare_data(expected_address,
                        actual_address), f"Address mismatch: Expected - '{expected_address}', but got - '{actual_address}'"

    checkout.verify_product_review_details(
        expected_name=expected_product_name,
        expected_price=expected_price,
        expected_quantity=1
    )

    # Enter description in comment text area and click 'Place Order'
    checkout.enter_comment("Please deliver between 9AM and 5PM")
    checkout.click_place_order()

    # Enter payment details: Name on Card, Card Number, CVC, Expiration date
    payment_test_data = load_test_data("payment_test_data.json")
    card_details = payment_test_data["test_payment_data"]
    payment.fill_payment_form(card_details)

    # Click 'Pay and Confirm Order' button
    payment.click_pay_and_confirm()

    # Verify success message 'Your order has been placed successfully!'
    payment.verify_order_success_message()

    # Click 'Delete Account' button
    account.click_delete_account()

    # Verify 'ACCOUNT DELETED!' and click 'Continue' button
    assert account.is_account_deleted_visible(), "'ACCOUNT DELETED!' is not visible"
