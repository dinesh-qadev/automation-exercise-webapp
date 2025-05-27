import allure
from pageObjects.home_page import HomePage
from pageObjects.product_page import ProductsPage
from pageObjects.cart_page import CartPage
from pageObjects.signup_login_page import SignupLoginPage
from utilities.data_loader import load_test_data


@allure.feature("Cart")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Search Products and Verify Cart After Login")
@allure.description("Verify searched products are added to cart and persist after user login.")
def test_search_products_and_verify_cart_after_login(browser):
    home = HomePage(browser)
    products = ProductsPage(browser)
    cart = CartPage(browser)
    signup_login = SignupLoginPage(browser)

    # 3. Click on 'Products' button
    home.click_products()

    # 4. Verify user is navigated to ALL PRODUCTS page successfully
    assert products.is_all_products_page_displayed(), "All Products page not visible"

    # 5. Enter product name in search input and click search button
    product_info = load_test_data("products.json")  # Test Data initialized
    search_data = product_info["search"]

    product_name = search_data["product_search"]  # Fetched product name from json
    products.enter_search_text(product_name)
    products.click_search_button()

    # 6. Verify 'SEARCHED PRODUCTS' is visible
    assert products.is_searched_products_section_visible(), "Searched Products section not visible"

    # 7. Verify all the products related to search are visible
    assert products.are_search_results_visible(product_name), f"Search results for '{product_name}' are not displayed correctly"

    # 8. Add those products to cart: for faster test we are only adding two products to cart
    product_1_name, product_1_price = products.hover_and_add_to_cart_and_get_price(1) # over and add first product to cart, capture price

    print(product_1_name)
    products.click_continue_shopping()
    product_2_name, product_2_price = products.hover_and_add_to_cart_and_get_price(2) # Hover and add second product to cart, capture price

    added_products = [product_1_name, product_2_name]
    # 9. Click 'Cart' button and verify that products are visible in cart
    products.click_view_cart()

    assert cart.are_products_in_cart(added_products), "First product not found in cart"  # Verify Product-1 is on cart
    #assert cart.are_products_in_cart(product_2_name), "Second product not found in cart"  # Verify Product-2 is on cart

    assert cart.verify_product_details(1, product_1_price), "Product 1 price/quantity/total is incorrect"  # Verify Product-1 details is correct on cart
    assert cart.verify_product_details(2, product_2_price), "Product 2 price/quantity/total is incorrect"  # Verify Product-1 details is correct on cart

    # 10. Click 'Signup / Login' button and submit login details
    home.click_signup_login()
    user_info = load_test_data("users.json")  # Test data loaded from json file
    correct_credential = user_info["valid_user"]
    signup_login.login_user(
        email=correct_credential["email"],
        password=correct_credential["password"])

    # 11. Again, go to Cart page
    home.click_cart_button()

    # 12. Verify that those products are visible in cart after login as well
    assert cart.are_products_in_cart(added_products), "Products are not found in cart"  # Verify Product is on cart
    #assert cart.are_products_in_cart(product_2_name), "Second product not found in cart"  # Verify Product-2 is on cart

    assert cart.verify_product_details(2,
                                       product_1_price), "Product 1 price/quantity/total is incorrect"  # Verify Product-1 details is correct on cart
    assert cart.verify_product_details(2,
                                       product_2_price), "Product 2 price/quantity/total is incorrect"  # Verify Product-1 details is correct on cart


