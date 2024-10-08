from locators.locators import GoogleFinanceLocators
from testdata.test_data import TestData
from utilities.utils import WebDriverUtils

class GoogleFinancePage:
    def __init__(self, driver):
        self.driver = driver

    def verify_page_title(self):
        assert TestData.GOOGLE_FINANCE_TITLE in self.driver.title, f"The page title does not contain '{TestData.GOOGLE_FINANCE_TITLE}'"

    def get_missing_symbols(self):
        stock_elements = WebDriverUtils.wait_for_elements_presence(self.driver, GoogleFinanceLocators.STOCK_SYMBOLS)
        ui_symbols = [element.text for element in stock_elements]

        given_test_data = TestData.GIVEN_STOCK_SYMBOLS
        missing_in_ui = set(given_test_data) - set(ui_symbols)

        return missing_in_ui

    def get_extra_symbols(self):
        stock_elements = WebDriverUtils.wait_for_elements_presence(self.driver, GoogleFinanceLocators.STOCK_SYMBOLS)
        ui_symbols = [element.text for element in stock_elements]

        given_test_data = TestData.GIVEN_STOCK_SYMBOLS
        extra_in_ui = set(ui_symbols) - set(given_test_data)

        return extra_in_ui


        # assert not missing_in_ui, f"Missing symbols: {missing_in_ui}"
        # assert not extra_in_ui, f"Extra symbols: {extra_in_ui}"