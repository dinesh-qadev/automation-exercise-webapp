import allure
from pageObjects.home_page import HomePage
from pageObjects.categoryPage import CategoryPage
from pageObjects.product_detail_page import ProductDetailPage
from utilities.data_loader import load_test_data


@allure.feature("Products")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("View Category Products")
@allure.description("Verify user can view products by category and sub-category.")
def test_view_category_products(browser):
    # Load category data from JSON
    categories = load_test_data("categories.json")

    home_page = HomePage(browser)
    category_page = CategoryPage(browser)
    product_detail_page = ProductDetailPage(browser)

    # Step 3: Verify category sidebar is visible
    assert home_page.is_category_section_visible(), "Category sidebar is not visible."

    # --- Women > Tops ---
    women = categories["women"]
    home_page.expand_main_category(women["main_category"])
    home_page.click_sub_category(women["main_category"], women["sub_category"])

    # 6. Verify that category page is displayed and confirm text 'WOMEN - TOPS PRODUCTS'
    heading = category_page.get_category_heading_text()
    assert women["expected_heading"] in heading.upper(), f"Unexpected heading: {heading}"

    # Verify products listed are really belongs to selected category
    product_links = category_page.get_all_visible_product_links()

    for link in product_links:
        browser.get(link)
        product_category = product_detail_page.get_product_category_text()
        assert women[
                   "sub_category"] in product_category, f"Product does not belong to '{women['sub_category']}' category: {product_category}"

    # --- Men > Tshirts ---

    men = categories["men"]
    home_page.expand_main_category(men["main_category"])
    home_page.click_sub_category(men["main_category"], men["sub_category"])

    heading = category_page.get_category_heading_text()
    assert men["expected_heading"] in heading.upper(), f"Unexpected heading: {heading}"

    product_links = category_page.get_all_visible_product_links()
    for link in product_links:
        browser.get(link)
        product_category = product_detail_page.get_product_category_text()
        assert men[
                   "sub_category"] in product_category, f"Product does not belong to '{men['sub_category']}' category: {product_category}"
