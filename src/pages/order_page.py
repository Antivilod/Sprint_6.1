from src.pages.base_page import BasePage
from src.locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    def fill_first_form(self, name, surname, address, metro_station, phone):
        self.input_text(OrderPageLocators.NAME_INPUT, name)
        self.input_text(OrderPageLocators.SURNAME_INPUT, surname)
        self.input_text(OrderPageLocators.ADDRESS_INPUT, address)
        
        # Выбор станции метро
        self.click_element(OrderPageLocators.METRO_STATION_INPUT)
        metro_locator = (OrderPageLocators.METRO_STATION_ITEM[0],
                        OrderPageLocators.METRO_STATION_ITEM[1].format(metro_station))
        self.click_element(metro_locator)
        
        self.input_text(OrderPageLocators.PHONE_INPUT, phone)
        self.click_element(OrderPageLocators.NEXT_BUTTON)
    
    def fill_second_form(self, date, rental_period, color, comment):
        self.input_text(OrderPageLocators.DATE_INPUT, date)
        
        # Выбор периода аренды
        self.click_element(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        period_locator = (OrderPageLocators.RENTAL_PERIOD_OPTION[0],
                         OrderPageLocators.RENTAL_PERIOD_OPTION[1].format(rental_period))
        self.click_element(period_locator)
        
        # Выбор цвета
        if color:
            color_locator = (OrderPageLocators.COLOR_CHECKBOX[0],
                           OrderPageLocators.COLOR_CHECKBOX[1].format(color))
            self.click_element(color_locator)
        
        if comment:
            self.input_text(OrderPageLocators.COMMENT_INPUT, comment)
        
        self.click_element(OrderPageLocators.ORDER_BUTTON)
    
    def confirm_order(self):
        self.click_element(OrderPageLocators.CONFIRM_ORDER_BUTTON)
    
    def is_order_created(self):
        return self.is_element_visible(OrderPageLocators.SUCCESS_MESSAGE)
    
    def get_success_message(self):
        return self.get_text(OrderPageLocators.SUCCESS_MESSAGE)
    
    def click_view_status(self):
        self.click_element(OrderPageLocators.VIEW_STATUS_BUTTON)