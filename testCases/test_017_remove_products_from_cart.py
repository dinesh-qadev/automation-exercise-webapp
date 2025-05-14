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

    # Step 1–3: Verify home page
    assert home.is_home_page_displayed()

    # Add products to cart
    expected_product_name, expected_price = product.hover_and_add_to_cart_and_get_price(product_index=1)

    # Click 'Cart' button
    product.click_view_cart()

    # Verify that cart page is displayed
    assert cart.is_cart_page_visible(), "Cart page URL is incorrect or not loaded"

    # Click 'X' button corresponding to particular product
    cart.delete_product_from_cart()

    # Verify that product is removed from the cart
    assert cart.is_product_removed(), "Product was not removed from the cart as expected."
