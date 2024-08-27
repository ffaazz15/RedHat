import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
    # Navigate to Google Finance
    driver.get("https://www.google.com/finance")
    driver.maximize_window()

    yield driver  # Return the driver instance to the test function
    # Quit the browser after the tests are done
    driver.quit()
