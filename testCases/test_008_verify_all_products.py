import pytest
from pageObjects.home_page import HomePage
from pageObjects.product_page import ProductsPage
from pageObjects.product_detail_page import ProductDetailPage
from utilities.logger import Logger

logger = Logger.get_logger()


def test_verify_all_products_and_product_detail(browser):
    # Step 1 & 2: Launch browser and navigate to URL

    """ This will be provided by fixture from conftest.py"""

    # Step 3: Verify home page is visible successfully
    home_page = HomePage(browser)
    assert home_page.is_home_page_displayed(), "Home page is not visible"

    # Step 4: Click on 'Products' button
    home_page.click_products()
    # logger.info("Step-4 executed")
    # Step 5 & 6: Verify navigation to ALL PRODUCTS page and product list is visible
    products_page = ProductsPage(browser)
    assert products_page.is_all_products_page_displayed(), "All Products page not visible"
    assert products_page.is_product_list_visible(), "Product list is not visible"
    #     logger.info("Step-5 and 6 executed")

    # Step 7: Click on 'View Product' of first product
    products_page.click_first_view_product()
    #     logger.info("Step-7 executed")

    # Step 8: Verify navigation to product detail page
    product_detail_page = ProductDetailPage(browser)
    assert product_detail_page.is_product_detail_page_displayed(), "Product detail page not displayed"
    #     logger.info("Step-8 executed")

    # Step 9: Verify product details are visible
    assert product_detail_page.is_product_name_visible(), "Product name not visible"
    #     logger.info("Step-9, check product name executed")
    assert product_detail_page.is_category_visible(), "Category not visible"
    #     logger.info("Step-4 category executed")
    assert product_detail_page.is_price_visible(), "Price not visible"
    #     logger.info("Step-4price executed")
    assert product_detail_page.is_availability_visible(), "Availability not visible"
    #     logger.info("Step-4 availability executed")
    assert product_detail_page.is_condition_visible(), "Condition not visible"
    #     logger.info("Step-4 condition executed")
    assert product_detail_page.is_brand_visible(), "Brand not visible"
    # logger.info("Step-4 brand executed")


""" logger is used to debug execution flow so it is commented after debuging"""
