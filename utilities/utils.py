# utilities/utils.py
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebDriverUtils:
    @staticmethod
    def wait_for_elements_presence(driver, locator, timeout=10):
        return WebDriverWait(driver, timeout).until(EC.presence_of_all_elements_located(locator))