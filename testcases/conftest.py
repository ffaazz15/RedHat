import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
    options.add_argument("--headless")
    driver.get("https://www.google.com/finance")
    driver.maximize_window()

    yield driver

    driver.quit()
