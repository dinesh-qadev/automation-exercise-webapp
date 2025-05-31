import time

import pytest
from pageObjects.home_page import HomePage
from pageObjects.contact_page import ContactUsPage
from utilities.data_loader import load_test_data
import allure
from utilities.data_loader import get_resource_file_path


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

    # Step 3: Verify home page is displayed by checking if 'Home' link is active
    assert home_page.is_home_page_displayed(), "Home page is not visible or 'Home' link is not active"

    # Step 4: Click on 'Contact Us' button
    home_page.click_contact_us()

    # Step 5: Verify 'GET IN TOUCH' header is visible on the Contact Us page
    assert contact_us_page.is_get_in_touch_header_visible(), "'GET IN TOUCH' header is not visible"

    # Step 6: Enter name, email, subject, and message
    name = required_testdata["name"]
    email = required_testdata["email"]
    subject = required_testdata["subject"]
    message = required_testdata["message"]
    contact_us_page.fill_contact_form(name, email, subject, message)

    # Step 7: Upload file
    file_path = get_resource_file_path("contact_us_upload_01.png")
    contact_us_page.upload_file(file_path)

    # Step 8: Click 'Submit' button
    contact_us_page.click_submit_button()

    # Step 9: Click 'OK' button (Handle JavaScript alert)
    alert = browser.switch_to.alert
    alert.accept()

    # Step 10: Verify success message is visible
    assert contact_us_page.is_success_message_visible(), "Success message is not visible after submitting contact form"

    # Step 11: Click 'Home' button and verify redirected to home page
    contact_us_page.click_home_button()
    assert home_page.is_home_page_displayed(), "Did not land back on home page after clicking 'Home'"
