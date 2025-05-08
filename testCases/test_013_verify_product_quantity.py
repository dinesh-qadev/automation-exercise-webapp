import pytest
from pageObjects.home_page import HomePage
from pageObjects.product_detail_page import ProductDetailPage
from pageObjects.cart_page import CartPage


def test_verify_product_quantity_in_cart(browser):
    home_page = HomePage(browser)
    product_page = ProductDetailPage(browser)
    cart_page = CartPage(browser)

    assert home_page.is_home_page_displayed(), "Home page is not visible"

    home_page.click_view_product()
    assert product_page.is_product_detail_visible(), "Product detail page not visible"

    product_page.set_quantity(int(4))
    product_page.click_add_to_cart()
    product_page.click_view_cart()

    quantity = cart_page.get_product_quantity()
    assert quantity == 4, f"Expected quantity 4, but got {quantity}"
