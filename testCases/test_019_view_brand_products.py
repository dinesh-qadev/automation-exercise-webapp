
from pageObjects.home_page import HomePage
from pageObjects.brands_page import BrandsPage


def test_view_brand_products(browser):
    home = HomePage(browser)
    brands = BrandsPage(browser)

    # Step 3: Click on 'Products' button
    home.click_products()

    # Step 4: Verify Brands section is visible
    assert brands.is_brands_section_visible(), "Brands section is not visible"

    # Step 5-6: Click on first brand and verify brand on product detail page
    first_brand = brands.click_brand_by_index(0)

    assert brands.is_brand_products_header_visible(first_brand), f"Not navigated to brand page {first_brand}"
    brands.click_first_product_view_link()
    product_brand = brands.get_product_brand_name()

    assert first_brand.lower() in product_brand.lower(), f"Expected brand '{first_brand}' in product detail, found '{product_brand}'"

    # Step 7-8: Go back, click second brand and verify again
    browser.back()
    second_brand = brands.click_brand_by_index(1)
    assert brands.is_brand_products_header_visible(second_brand), f"Not navigated to brand page {second_brand}"
    brands.click_first_product_view_link()
    product_brand = brands.get_product_brand_name()
    assert second_brand.lower() in product_brand.lower(), f"Expected brand '{second_brand}' in product detail, found '{product_brand}'"
