from pages.google_finance_page import GoogleFinancePage

def test_google_finance_page_title(driver):
    google_finance_page = GoogleFinancePage(driver)
    google_finance_page.verify_page_title()

def test_symbols_missing_in_ui(driver):
    google_finance_page = GoogleFinancePage(driver)
    missing_in_ui = google_finance_page.get_missing_symbols()
    print(f"Symbols missing in UI: {missing_in_ui}")


def test_extra_symbols_in_ui(driver):
    google_finance_page = GoogleFinancePage(driver)
    extra_in_ui = google_finance_page.get_extra_symbols()
    print(f"Extra symbols in UI: {extra_in_ui}")

