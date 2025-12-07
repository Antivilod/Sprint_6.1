import pytest
import allure
from src.pages.main_page import MainPage
from src.pages.order_page import OrderPage
from data.test_data import first_order_data, second_order_data


@allure.feature("Заказ самоката")
class TestOrderPage:
    
    @allure.title("Тест: Заказ самоката через верхнюю кнопку с набором данных 1")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_order_via_top_button_first_data(self, driver):
        self._run_order_test(driver, first_order_data, "top")
    
    @allure.title("Тест: Заказ самоката через нижнюю кнопку с набором данных 1")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_order_via_bottom_button_first_data(self, driver):
        self._run_order_test(driver, first_order_data, "bottom")
    
    @allure.title("Тест: Заказ самоката через верхнюю кнопку с набором данных 2")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_order_via_top_button_second_data(self, driver):
        self._run_order_test(driver, second_order_data, "top")
    
    @allure.title("Тест: Заказ самоката через нижнюю кнопку с набором данных 2")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_order_via_bottom_button_second_data(self, driver):
        self._run_order_test(driver, second_order_data, "bottom")
    
    def _run_order_test(self, driver, order_data, button_position):
        with allure.step("Открыть главную страницу"):
            main_page = MainPage(driver)
            main_page.open()
        
        with allure.step(f"Нажать кнопку 'Заказать' ({button_position})"):
            if button_position == "top":
                main_page.click_order_button_top()
            else:
                main_page.click_order_button_bottom()
        
        with allure.step("Заполнить первую форму заказа"):
            order_page = OrderPage(driver)
            order_page.fill_first_form(
                name=order_data.name,
                surname=order_data.surname,
                address=order_data.address,
                metro_station=order_data.metro_station,
                phone=order_data.phone
            )
        
        with allure.step("Заполнить вторую форму заказа"):
            order_page.fill_second_form(
                date=order_data.date,
                rental_period=order_data.rental_period,
                color=order_data.color,
                comment=order_data.comment
            )
        
        with allure.step("Подтвердить заказ"):
            order_page.confirm_order()
        
        with allure.step("Проверить успешное создание заказа"):
            assert order_page.is_order_created(), "Не появилось окно с подтверждением заказа"
            
            success_message = order_page.get_success_message()
            assert "Заказ оформлен" in success_message, \
                f"Неверное сообщение об успехе. Получено: {success_message}"
            
            allure.attach(
                f"Сообщение об успехе: {success_message}",
                name="Success Message",
                attachment_type=allure.attachment_type.TEXT
            )
    
    @allure.title("Тест: Весь флоу заказа с разными точками входа")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("button_position", ["top", "bottom"])
    @pytest.mark.parametrize("order_data", [first_order_data, second_order_data])
    def test_complete_order_flow_parametrized(self, driver, button_position, order_data):
        with allure.step("Открыть главную страницу"):
            main_page = MainPage(driver)
            main_page.open()
        
        with allure.step(f"Нажать кнопку 'Заказать' ({button_position})"):
            if button_position == "top":
                main_page.click_order_button_top()
            else:
                main_page.click_order_button_bottom()
        
        with allure.step("Заполнить формы заказа"):
            order_page = OrderPage(driver)
            order_page.fill_first_form(
                name=order_data.name,
                surname=order_data.surname,
                address=order_data.address,
                metro_station=order_data.metro_station,
                phone=order_data.phone
            )
            
            order_page.fill_second_form(
                date=order_data.date,
                rental_period=order_data.rental_period,
                color=order_data.color,
                comment=order_data.comment
            )
        
        with allure.step("Подтвердить и проверить заказ"):
            order_page.confirm_order()
            assert order_page.is_order_created(), "Заказ не был создан"