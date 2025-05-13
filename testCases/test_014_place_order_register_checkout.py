import pytest
import time
import random
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


def test_place_order_register_checkout(browser):
    home = HomePage(browser)
    product = ProductsPage(browser)
    cart = CartPage(browser)
    signuplogin = SignupLoginPage(browser)
    account = AccountPage(browser)
    checkout = CheckoutPage(browser)
    payment = PaymentPage(browser)

    # Step 1–3: Verify home page
    assert home.is_home_page_displayed()

    # Step 4–6: Add product and go to cart

    expected_product_name, expected_price = product.hover_and_add_to_cart_and_get_price(product_index=1)
    product. click_view_cart()
    assert cart.is_cart_page_visible(), "Cart page URL is incorrect or not loaded"

    # Step 7–8: Proceed to checkout then click Register/Login
    cart.click_proceed_to_checkout()
    cart.click_register_login_button()

    # Step 9–10: Fill signup, create account
    random_email = generate_random_email()
    # Load data from json fie
    user_data = load_test_data("users.json")
    account_info = user_data["account_info"]
    address_info = user_data["address_info"]
    signuplogin.signup(
        name=address_info["firstname"]+address_info["lastname"],
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
    assert account.is_account_created_visible(), "'ACCOUNT CREATED!' is not visible"
    account.click_continue()

    # Step 11–13: Logged in, go to cart and proceed to checkout
    assert account.is_logged_in_as_visible(user_name=address_info["firstname"]+address_info["lastname"]), "'Logged in as username' is not visible"
    home.click_cart_button()
    cart.click_proceed_to_checkout()

    # Step 14: Verify address and review order
    assert checkout.is_address_and_review_visible(), f"Review section is not visible in checkout page"

    #Verify address content and order details
    expected_address = f"{address_info['firstname']} {address_info['lastname']} {address_info['company']} {address_info['address1']} {address_info['address2']} {address_info['city']} {address_info['state']} {address_info['zipcode']} {address_info['country']} {address_info['mobile']}"
    actual_address = checkout.get_delivery_address_text()
    assert compare_data(expected_address, actual_address), f"Address mismatch: Expected - '{expected_address}', but got - '{actual_address}'"

    checkout.verify_product_review_details(
        expected_name=expected_product_name,
        expected_price=expected_price,
        expected_quantity=1
    )

    # Step 15: Enter comment and click Place Order
    checkout.enter_comment("Please deliver between 9AM and 5PM")
    checkout.click_place_order()

    # Step 16-18: Payment
    payment_test_data = load_test_data("payment_test_data.json")
    card_details = payment_test_data["test_payment_data"]
    payment.fill_payment_form(card_details)
    payment.click_pay_and_confirm()
    payment.verify_order_success_message()

    # Step 19-20
    account.click_delete_account()
    assert account.is_account_deleted_visible(), "'ACCOUNT DELETED!' is not visible"
