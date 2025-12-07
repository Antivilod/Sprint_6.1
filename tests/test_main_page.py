import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pages.main_page import MainPage
from data.test_data import questions_data


@allure.feature("Главная страница Яндекс.Самокат")
class TestMainPage:
    
    @allure.title("Тест: Ответы на вопросы в разделе 'Вопросы о важном'")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("question_data", questions_data)
    def test_questions_section(self, driver, question_data):
        with allure.step("Открыть главную страницу"):
            main_page = MainPage(driver)
            main_page.open()
        
        with allure.step("Проскроллить к разделу с вопросами"):
            main_page.scroll_to_questions()
        
        with allure.step(f"Кликнуть на вопрос номер {question_data['question']}"):
            main_page.click_question_button(question_data['question'])
        
        with allure.step("Получить текст ответа"):
            answer_text = main_page.get_answer_text(question_data['question'])
        
        with allure.step(f"Проверить, что ответ содержит '{question_data['answer_contains']}'"):
            assert question_data['answer_contains'] in answer_text, \
                f"Ответ не содержит ожидаемый текст. Полученный ответ: {answer_text}"
    
    @allure.title("Тест: Логотип Самоката ведет на главную страницу")
    @allure.severity(allure.severity_level.NORMAL)
    def test_scooter_logo_redirect(self, driver):
        with allure.step("Открыть главную страницу"):
            main_page = MainPage(driver)
            main_page.open()
        
        with allure.step("Кликнуть на логотип Самоката"):
            main_page.click_scooter_logo()
        
        with allure.step("Проверить, что остались на главной странице"):
            assert main_page.is_main_page(), "Клик по логотипу Самоката не ведет на главную страницу"
    
    @allure.title("Тест: Логотип Яндекса открывает главную страницу Дзена")
    @allure.severity(allure.severity_level.NORMAL)
    def test_yandex_logo_redirect(self, driver):
        with allure.step("Открыть главную страницу"):
            main_page = MainPage(driver)
            main_page.open()
        
        with allure.step("Сохранить текущее окно"):
            current_window = driver.current_window_handle
        
        with allure.step("Кликнуть на логотип Яндекса"):
            main_page.click_yandex_logo()
        
        with allure.step("Переключиться на новое окно"):
            WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
            main_page.switch_to_new_window()
        
        with allure.step("Проверить, что открылась страница Дзена"):
            WebDriverWait(driver, 10).until(EC.url_contains("dzen.ru"))
            assert "dzen.ru" in driver.current_url, "Не открылась страница Дзена"
        
        with allure.step("Закрыть новое окно и вернуться на главную"):
            driver.close()
            driver.switch_to.window(current_window)