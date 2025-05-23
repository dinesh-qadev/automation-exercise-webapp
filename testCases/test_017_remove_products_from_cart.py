import allure
from pageObjects.home_page import HomePage
from pageObjects.product_page import ProductsPage
from pageObjects.cart_page import CartPage


@allure.feature("Cart")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Remove Products from Cart")
@allure.description("Verify user can remove products from the cart successfully.")
def test_place_order_register_before_checkout(browser):
    home = HomePage(browser)
    product = ProductsPage(browser)
    cart = CartPage(browser)

    # Step 1–3: Verify home page
    assert home.is_home_page_displayed()

    # Add products to cart
    expected_product_name, expected_price = product.hover_and_add_to_cart_and_get_price(1)

    # Click 'Cart' button
    product.click_view_cart()

    # Verify that cart page is displayed
    assert cart.is_cart_page_visible(), "Cart page URL is incorrect or not loaded"

    # Click 'X' button corresponding to particular product
    cart.delete_product_from_cart()

    # Verify that product is removed from the cart
    assert cart.is_product_removed(), "Product was not removed from the cart as expected."
