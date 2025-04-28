Testcases- https://docs.google.com/spreadsheets/d/1NUxqXTgNuichaF1jcYwfu4PFWOOiKpK-FEF60RkuZe4/edit?gid=0#gid=0

Test Automation Framework for AutomationExercise.com
This repository contains a Selenium + Python-based test automation framework using Page Object Model (POM) and Pytest. The framework is designed to automate the testing of https://www.automationexercise.com/, focusing on various test scenarios such as user authentication, product management, UI validations, and basic workflows.

Framework Structure
The framework follows a modular design using Page Object Model (POM), making it scalable, maintainable, and easy to extend.

1. Directory Structure
configurations/: Contains environment-specific configuration files (e.g., UAT, PROD configurations).

config_uat.ini and config_prod.ini to store URLs, credentials, and other configurations based on the environment.

logs/: Stores logs for debugging and auditing purposes.

automationexercise.log logs key actions and results during test execution.

pageObjects/: Contains page classes for different pages of the website.

Examples: homePage.py, registerPage.py, cartPage.py for managing page interactions.

testCases/: Holds the test case scripts organized into different categories.

Example: test_regression.py for main regression tests, basetest.py for common setup and teardown functionality, and conftest.py for common fixtures.

utilities/: Includes utility functions and helper classes.

Examples: customLogger.py for logging, readProperties.py for reading configuration files, and dynamicTestData.py for generating random test data.

testData/: Stores test data files (e.g., Excel, JSON files).

Example: test_data.xlsx for user credentials, product details, etc.

reports/: Stores generated test execution reports in HTML format.

Example: reports.html for test execution summary.

pytest.ini: Configuration file for Pytest to set parameters and markers.

2. Key Technologies
Selenium WebDriver: For automating browser interactions.

Pytest: For test execution, handling fixtures, and generating reports.

Page Object Model (POM): To manage UI interactions in a modular way.

pytest-html or Allure: For generating detailed test reports.

webdriver-manager: To automatically manage browser drivers.

Test Strategy
The test cases are organized to cover the following areas:

User Authentication: Login, Signup, Password Recovery.

Product Management: Add to Cart, View Products, Checkout.

UI Validations: Verifying homepage elements, product details, navigation links.

Form Submissions: User registration, contact forms, etc.

Basic Workflows: Login, Add Products to Cart, Checkout.

Hybrid Testing Approach
Data-Driven Testing (DDT): Used for tests that require different input combinations (e.g., login with multiple user credentials).

Action-Based Testing: For tests that involve sequential actions like navigating the site or verifying elements.

Test Execution Flow
Driver Setup: Each test begins with the setup of a browser instance using the driver fixture from Pytest.

Test Initialization: Navigate to the base URL of the site and instantiate page objects (e.g., HomePage, ProductPage).

Action: Perform actions like adding products to the cart, navigating through pages, and filling out forms using the methods defined in the page objects.

Assertions: After actions, assertions validate that the expected outcome is achieved (e.g., product is added to the cart).

Logging: Log key actions and results throughout the test execution.

Reporting: After the tests, an HTML report is generated and saved in the reports/ directory.

How to Set Up and Run the Tests
Clone this repository to your local machine:


git clone https://github.com/yourusername/test-automation-framework.git

Install required dependencies:


pip install -r requirements.txt
Configure environment-specific settings:

Update config_uat.ini and config_prod.ini with your credentials and URLs.

Run the tests with Pytest:


pytest --maxfail=1 --disable-warnings -q
This will run the tests and generate an HTML report in the reports/ directory.

Author:
Your Name
GitHub:


This README.txt file serves as a detailed guide to setting up and running the test automation framework for the AutomationExercise.com website. It outlines the structure, execution flow, and other key components to ensure smooth implementation and usage of the framework.