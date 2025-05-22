import allure
import pytest
from pageObjects.home_page import HomePage
from pageObjects.product_page import ProductsPage
from utilities.data_loader import load_test_data


@allure.feature("Products")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Search Product by Name")
@allure.description("Verify search functionality returns relevant products.")
def test_search_product(browser):
    # Step 1 & 2: Launch browser and navigate to URL (handled by fixture)

    # Step 3: Verify home page is visible
    home_page = HomePage(browser)
    product_info = load_test_data("products.json")
    search_data = product_info["search"]
    assert home_page.is_home_page_displayed(), "Home page is not visible"

    # Step 4: Click on 'Products' button
    home_page.click_products()

    # Step 5: Verify ALL PRODUCTS page is visible
    products_page = ProductsPage(browser)
    assert products_page.is_all_products_page_displayed(), "All Products page is not visible"

    # Step 6: Enter product name in search input and click search button
    product_name = search_data["product_search"]  # Fetched product name from json
    products_page.enter_search_text(product_name)
    products_page.click_search_button()

    # Step 7: Verify 'SEARCHED PRODUCTS' is visible
    assert products_page.is_searched_products_section_visible(), "Searched Products section not visible"

    # Step 8: Verify all search result products are visible
    assert products_page.are_search_results_visible(product_name), f"Search results for '{product_name}' are not displayed correctly"
