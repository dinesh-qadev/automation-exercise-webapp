import platform
import shutil
import tempfile

import pytest
import allure
import json
import os
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from configurations.config import StagingConfig, QAConfig, ProdConfig
from selenium.webdriver.chrome.options import Options


def get_config(env):
    envs = {
        "staging": StagingConfig,
        "qa": QAConfig,
        "production": ProdConfig
    }
    return envs.get(env.lower(), ProdConfig)  # default to Production in this case


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="production",
        help="Environment to run tests against: staging / qa / prod"
    )


@pytest.fixture(scope="session")
def config(request):
    env = request.config.getoption("--env")
    return get_config(env)


@pytest.fixture(scope="function")
def browser(config):

    options = Options()
    # Run Chrome headless on CI or if you want
    options.add_argument("--headless=new")  # newer headless mode
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")  # required in many CI environments
    options.add_argument("--disable-dev-shm-usage")  # overcome limited /dev/shm
    options.add_argument("--disable-extensions")
    options.add_argument("--remote-allow-origins=*")  # helps with Chrome 111+

    # Use a temp user data dir to avoid "profile in use" errors
    temp_user_data_dir = tempfile.mkdtemp()
    options.add_argument(f"--user-data-dir={temp_user_data_dir}")

    # Setup Chrome browser
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.maximize_window()

    driver.get(config.BASE_URL)
    yield driver
    # Teardown
    driver.quit()
    shutil.rmtree(temp_user_data_dir)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == 'call' and report.failed:
        driver = item.funcargs['browser']
        allure.attach(driver.get_screenshot_as_png(),
                      name="screenshot_on_failure",
                      attachment_type=allure.attachment_type.PNG)


def pytest_sessionfinish(session, exitstatus):
    """Hook runs after all tests complete — writes executor.json for Allure."""
    results_dir = os.path.join(os.getcwd(), "allure-results")
    os.makedirs(results_dir, exist_ok=True)

    # Get environment from command-line option
    env = session.config.getoption("--env")  # this gets the runtime env

    # Generate executor.json
    executor_data = {
        #"name": getpass.getuser(),  # Current system user (e.g., 'dinesh')
        "name": "Dinesh- Automation Test Engineer",
        "type": "SCript",  # Change to 'CI' or 'script' if needed
        "url": "http://localhost",  # Change if using a real CI URL
        "buildOrder": datetime.datetime.now().strftime("%Y%m%d%H%M%S"),
        "buildName": f"Test Run {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "buildUrl": "http://localhost/build"  # Change to actual build URL if needed
    }

    with open(os.path.join(results_dir, "executor.json"), "w") as f:
        json.dump(executor_data, f, indent=2)

        # Generate environment.properties
        environment_data = {
            "Browser": "Chrome 124",  # Update this if using different browsers
            "OS": platform.system() + " " + platform.release(),
            "Python_Version": platform.python_version(),
            "Test_Environment": env.capitalize(),
            "Allure_Version": "2.25.0"
        }

        with open(os.path.join(results_dir, "environment.properties"), "w") as f:
            for key, value in environment_data.items():
                f.write(f"{key}={value}\n")

        # 3. Generate categories.json
        categories_data = [
            {
                "name": "Product Defects",
                "matchedStatuses": ["failed"],
                "messageRegex": ".*AssertionError.*"
            },
            {
                "name": "Test Defects",
                "matchedStatuses": ["broken"],
                "messageRegex": ".*(NoSuchElementException|TimeoutException).*"
            },
            {
                "name": "Infrastructure Issues",
                "matchedStatuses": ["broken"],
                "messageRegex": ".*(Connection refused|ConnectionError|DNS failure).*"
            }
        ]
        with open(os.path.join(results_dir, "categories.json"), "w") as f:
            json.dump(categories_data, f, indent=2)

