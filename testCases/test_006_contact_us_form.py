import pytest
from selenium.webdriver.common.by import By
from pageObjects.home_page import HomePage
from pageObjects.contact_page import ContactUsPage


def test_006_contact_us_form(browser):
    # Initialize page objects
    home_page = HomePage(browser)
    contact_us_page = ContactUsPage(browser)

    # Step 1: Verify home page is displayed by checking if 'Home' link is active
    assert home_page.is_home_page_displayed(), "Home page is not visible or 'Home' link is not active"

    # Step 2: Click on 'Contact Us' button
    home_page.click_contact_us()

    # Step 3: Verify 'GET IN TOUCH' header is visible on the Contact Us page
    assert contact_us_page.is_get_in_touch_header_visible(), "'GET IN TOUCH' header is not visible"

    # Step 4: Enter name, email, subject, and message
    name = "John Doe"
    email = "john.doe@example.com"
    subject = "Test Subject"
    message = "This is a test message."
    contact_us_page.fill_contact_form(name, email, subject, message)

    # Step 5: Upload file
    file_path = "C:\\Users\\Dell\\Downloads\\2149192357.jpg"  # Provide the correct path to the file
    contact_us_page.upload_file(file_path)

    # Step 6: Click 'Submit' button
    contact_us_page.click_submit_button()

    # Step 7: Click 'OK' button on success pop-up
    contact_us_page.click_ok_button
