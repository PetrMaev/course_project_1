import pytest
from numpy import nan


@pytest.fixture
def transactions_for_test():
    return [
        {'Дата операции': '31.12.2021 16:44:00', 'Дата платежа': '31.12.2021', 'Номер карты': '*7197', 'Статус': 'OK',
         'Сумма операции': -160.89, 'Валюта операции': 'RUB', 'Сумма платежа': -160.89, 'Валюта платежа': 'RUB',
         'Кэшбэк': 0, 'Категория': 'Супермаркеты', 'MCC': 5411.0, 'Описание': 'Колхоз', 'Бонусы (включая кэшбэк)': 3,
         'Округление на инвесткопилку': 0, 'Сумма операции с округлением': 160.89},
        {'Дата операции': '31.12.2021 16:42:04', 'Дата платежа': '31.12.2021', 'Номер карты': '*7197', 'Статус': 'OK',
         'Сумма операции': -64.0, 'Валюта операции': 'RUB', 'Сумма платежа': -64.0, 'Валюта платежа': 'RUB',
         'Кэшбэк': 0, 'Категория': 'Супермаркеты', 'MCC': 5411.0, 'Описание': 'Колхоз', 'Бонусы (включая кэшбэк)': 1,
         'Округление на инвесткопилку': 0, 'Сумма операции с округлением': 64.0},
        {'Дата операции': '31.12.2021 16:39:04', 'Дата платежа': '31.12.2021', 'Номер карты': '*7197', 'Статус': 'OK',
         'Сумма операции': -118.12, 'Валюта операции': 'RUB', 'Сумма платежа': -118.12, 'Валюта платежа': 'RUB',
         'Кэшбэк': 0, 'Категория': 'Супермаркеты', 'MCC': 5411.0, 'Описание': 'Магнит', 'Бонусы (включая кэшбэк)': 2,
         'Округление на инвесткопилку': 0, 'Сумма операции с округлением': 118.12},
        {'Дата операции': '31.12.2021 15:44:39', 'Дата платежа': '31.12.2021', 'Номер карты': '*7197', 'Статус': 'OK',
         'Сумма операции': -78.05, 'Валюта операции': 'RUB', 'Сумма платежа': -78.05, 'Валюта платежа': 'RUB',
         'Кэшбэк': 0, 'Категория': 'Супермаркеты', 'MCC': 5411.0, 'Описание': 'Колхоз', 'Бонусы (включая кэшбэк)': 1,
         'Округление на инвесткопилку': 0, 'Сумма операции с округлением': 78.05}]


@pytest.fixture
def transactions_with_phone_numbers():
    return [
        {'Дата операции': '31.12.2021 16:44:00', 'Дата платежа': '31.12.2021', 'Номер карты': '*7197', 'Статус': 'OK',
         'Сумма операции': -160.89, 'Валюта операции': 'RUB', 'Сумма платежа': -160.89, 'Валюта платежа': 'RUB',
         'Кэшбэк': 0, 'Категория': 'Супермаркеты', 'MCC': 5411.0, 'Описание': 'Колхоз', 'Бонусы (включая кэшбэк)': 3,
         'Округление на инвесткопилку': 0, 'Сумма операции с округлением': 160.89},
        {'Дата операции': '18.11.2021 21:15:27', 'Дата платежа': '19.11.2021', 'Номер карты': 'NaN', 'Статус': 'OK',
         'Сумма операции': -200.0, 'Валюта операции': 'RUB', 'Сумма платежа': -200.0, 'Валюта платежа': 'RUB',
         'Кэшбэк': 'NaN', 'Категория': 'Мобильная связь', 'MCC': 'NaN', 'Описание': 'Тинькофф Мобайл +7 995 555-55-55',
         'Бонусы (включая кэшбэк)': 2, 'Округление на инвесткопилку': 0, 'Сумма операции с округлением': 200.0},
        {'Дата операции': '31.12.2021 16:39:04', 'Дата платежа': '31.12.2021', 'Номер карты': '*7197', 'Статус': 'OK',
         'Сумма операции': -118.12, 'Валюта операции': 'RUB', 'Сумма платежа': -118.12, 'Валюта платежа': 'RUB',
         'Кэшбэк': 0, 'Категория': 'Супермаркеты', 'MCC': 5411.0, 'Описание': 'Магнит', 'Бонусы (включая кэшбэк)': 2,
         'Округление на инвесткопилку': 0, 'Сумма операции с округлением': 118.12}]
