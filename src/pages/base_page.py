from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def find_elements(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))
    
    def click_element(self, locator):
        element = self.find_element(locator)
        element.click()
    
    def input_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text
    
    def is_element_visible(self, locator):
        try:
            element = self.find_element(locator)
            return element.is_displayed()
        except:
            return False
    
    def switch_to_new_window(self):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])
    
    def accept_cookies(self):
        from src.locators.main_page_locators import MainPageLocators
        try:
            self.click_element(MainPageLocators.COOKIE_BUTTON)
        except:
            pass