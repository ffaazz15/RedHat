import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--headless")  # This should be added before creating the driver

    driver = webdriver.Chrome(options=options)  # Initialize driver after setting options
    driver.get("https://www.google.com/finance")
    driver.maximize_window()

    yield driver  # Provide the driver instance to the tests

    driver.quit()  # Quit the driver after the tests are done
