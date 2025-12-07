from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопки заказа
    ORDER_BUTTON_TOP = (By.XPATH, "//button[@class='Button_Button__ra12g']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//button[contains(@class, 'Button_Middle')]")
    
    # Логотипы
    SCOOTER_LOGO = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']")
    YANDEX_LOGO = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']")
    
    # Вопросы о важном
    QUESTIONS_SECTION = (By.CLASS_NAME, "Home_FAQ__3uVm4")
    QUESTION_BUTTON = (By.ID, "accordion__heading-{}")
    ANSWER_TEXT = (By.XPATH, "//div[@id='accordion__panel-{}']/p")
    
    # Cookie
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")