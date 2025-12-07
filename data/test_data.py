from dataclasses import dataclass
from datetime import datetime


@dataclass
class OrderData:
    name: str
    surname: str
    address: str
    metro_station: str
    phone: str
    date: str
    rental_period: str
    color: str
    comment: str


# Первый набор данных
first_order_data = OrderData(
    name="Иван",
    surname="Иванов",
    address="ул. Ленина, д. 1",
    metro_station="Сокольники",
    phone="+79991234567",
    date=datetime.now().strftime("%d.%m.%Y"),
    rental_period="сутки",
    color="black",
    comment="Позвонить за час"
)

# Второй набор данных
second_order_data = OrderData(
    name="Мария",
    surname="Петрова",
    address="пр. Мира, д. 10",
    metro_station="Черкизовская",
    phone="+79997654321",
    date=datetime.now().strftime("%d.%m.%Y"),
    rental_period="двое суток",
    color="grey",
    comment="Код от подъезда 1234"
)

# Данные для вопросов
questions_data = [
    {"question": 0, "answer_contains": "Сутки — 400 рублей. Оплата курьеру — наличными или картой."},
    {"question": 1, "answer_contains": "Пока что у нас так: один заказ — один самокат"},
    {"question": 2, "answer_contains": "Допустим, вы оформляете заказ на 8 мая"},
    {"question": 3, "answer_contains": "Только начиная с завтрашнего дня"},
    {"question": 4, "answer_contains": "Пока что нет! Но если что-то срочное"},
    {"question": 5, "answer_contains": "Самокат приезжает к вам с полной зарядкой"},
    {"question": 6, "answer_contains": "Да, пока самокат не привезли"},
    {"question": 7, "answer_contains": "Да, обязательно. Всем самокатов!"}
]