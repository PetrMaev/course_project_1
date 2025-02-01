from src.services import simple_searching, get_transactions_with_phone_numbers

from numpy import nan


def test_simple_searching(transactions_for_test):
    assert simple_searching(transactions_for_test,
                            "Магнит") == '[{"Дата операции": "31.12.2021 16:39:04", "Дата платежа": "31.12.2021", "Номер карты": "*7197", "Статус": "OK", "Сумма операции": -118.12, "Валюта операции": "RUB", "Сумма платежа": -118.12, "Валюта платежа": "RUB", "Кэшбэк": 0, "Категория": "Супермаркеты", "MCC": 5411.0, "Описание": "Магнит", "Бонусы (включая кэшбэк)": 2, "Округление на инвесткопилку": 0, "Сумма операции с округлением": 118.12}]'


def test_get_transactions_with_phone_numbers(transactions_with_phone_numbers):
    assert get_transactions_with_phone_numbers(
        transactions_with_phone_numbers) == [
               {"Дата операции": "18.11.2021 21:15:27", "Дата платежа": "19.11.2021", "Номер карты": "NaN",
                "Статус": "OK", "Сумма операции": -200.0, "Валюта операции": "RUB", "Сумма платежа": -200.0,
                "Валюта платежа": "RUB", "Кэшбэк": "NaN", "Категория": "Мобильная связь", "MCC": "NaN",
                "Описание": "Тинькофф Мобайл +7 995 555-55-55", "Бонусы (включая кэшбэк)": 2,
                "Округление на инвесткопилку": 0, "Сумма операции с округлением": 200.0}]
