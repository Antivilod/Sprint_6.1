from src.pages.base_page import BasePage
from src.locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://qa-scooter.praktikum-services.ru/"
    
    def open(self):
        self.driver.get(self.url)
        self.accept_cookies()
    
    def click_order_button_top(self):
        self.click_element(MainPageLocators.ORDER_BUTTON_TOP)
    
    def click_order_button_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.click_element(MainPageLocators.ORDER_BUTTON_BOTTOM)
    
    def click_question_button(self, question_number):
        locator = (MainPageLocators.QUESTION_BUTTON[0], 
                  MainPageLocators.QUESTION_BUTTON[1].format(question_number))
        self.click_element(locator)
    
    def get_answer_text(self, question_number):
        locator = (MainPageLocators.ANSWER_TEXT[0], 
                  MainPageLocators.ANSWER_TEXT[1].format(question_number))
        return self.get_text(locator)
    
    def click_scooter_logo(self):
        self.click_element(MainPageLocators.SCOOTER_LOGO)
    
    def click_yandex_logo(self):
        self.click_element(MainPageLocators.YANDEX_LOGO)
    
    def is_main_page(self):
        return "qa-scooter" in self.driver.current_url
    
    def scroll_to_questions(self):
        element = self.find_element(MainPageLocators.QUESTIONS_SECTION)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)