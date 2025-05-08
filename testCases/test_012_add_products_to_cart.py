import pytest
from pageObjects.home_page import HomePage
from pageObjects.product_page import ProductsPage
from pageObjects.cart_page import CartPage


def test_add_products_in_cart(browser):
    home_page = HomePage(browser)
    products_page = ProductsPage(browser)
    cart_page = CartPage(browser)

    # Step 1-2: Open home page

    # Step 3: Verify home page is visible
    assert home_page.is_home_page_displayed(), "Home page is not visible"

    # Step 4: Click 'Products' button
    home_page.click_products()

    # Step 5: Hover and add first product to cart, capture price
    print("hovering over to product test started")
    product_1_price = products_page.hover_and_add_to_cart_and_get_price(1)

    # Step 6: Click 'Continue Shopping'
    products_page.click_continue_shopping()

    # Step 7: Hover and add second product to cart, capture price
    product_2_price = products_page.hover_and_add_to_cart_and_get_price(2)

    # Step 8: Click 'View Cart'
    products_page.click_view_cart()

    # Step 9: Verify both products are in cart
    assert cart_page.is_product_in_cart(1), "First product not found in cart"
    assert cart_page.is_product_in_cart(2), "Second product not found in cart"

    # Step 10: Verify prices, quantities, and totals (including captured prices)
    assert cart_page.verify_product_details(1, product_1_price),"Product 1 price/quantity/total is incorrect"
    assert cart_page.verify_product_details(2, product_2_price), "Product 2 price/quantity/total is incorrect"
