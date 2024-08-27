from pages.google_finance_page import GoogleFinancePage

def test_google_finance(driver):
    google_finance_page = GoogleFinancePage(driver)
    google_finance_page.verify_page_title()
    google_finance_page.compare_stock_symbols()
