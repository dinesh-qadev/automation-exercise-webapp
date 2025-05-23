import time

import pytest
from pageObjects.home_page import HomePage
from pageObjects.contact_page import ContactUsPage
from utilities.data_loader import load_test_data
import allure


@allure.feature("Contact Us")
@allure.severity(allure.severity_level.MINOR)
@allure.title("Submit Contact Us Form")
@allure.description("Verify user can submit contact form and success message is displayed.")
def test_006_contact_us_form(browser):
    # Initialize page objects
    home_page = HomePage(browser)
    contact_us_page = ContactUsPage(browser)

    #Initialize TestData
    messeges = load_test_data("contact_us.json")
    required_testdata = messeges["contact_form"]

    # Step 1: Verify home page is displayed by checking if 'Home' link is active
    assert home_page.is_home_page_displayed(), "Home page is not visible or 'Home' link is not active"

    # Step 2: Click on 'Contact Us' button
    home_page.click_contact_us()

    # Step 3: Verify 'GET IN TOUCH' header is visible on the Contact Us page
    assert contact_us_page.is_get_in_touch_header_visible(), "'GET IN TOUCH' header is not visible"

    # Step 4: Enter name, email, subject, and message
    name = required_testdata["name"]
    email = required_testdata["email"]
    subject = required_testdata["subject"]
    message = required_testdata["message"]
    contact_us_page.fill_contact_form(name, email, subject, message)

    # Step 5: Upload file
    file_path = required_testdata["filepath"]
    # Provide the correct path to the file
    contact_us_page.upload_file(file_path)

    # Step 6: Click 'Submit' button
    contact_us_page.click_submit_button()

    # Step 7: Click 'OK' button on success pop-up
    contact_us_page.click_ok_button
