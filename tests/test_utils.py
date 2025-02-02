import unittest
from unittest.mock import patch, mock_open
import requests

from freezegun import freeze_time

from src.utils import greeting, cards_info, top_transactions, get_exchange_rate, get_stock_price


def test_greeting():
    with freeze_time("2025-01-29 01:00:00"):
        assert greeting() == "Доброй ночи"


def test_cards_info():
    assert cards_info("25.12.2021") == [{'Номер карты': '*5091', 'Сумма операции с округлением': 53.83, 'Кешбэк': 0.54},
                                        {
                                            'Номер карты': '*7197', 'Сумма операции с округлением': 3873.8999999999996,
                                            'Кешбэк': 38.74}]


def test_top_transactions():
    assert top_transactions("25.12.2021") == [
        {
            "Дата платежа": "25.12.2021",
            "Сумма операции с округлением": 3400.0,
            "Категория": "Развлечения",
            "Описание": "sevs.eduerp.ru",
        },
        {
            "Дата платежа": "25.12.2021",
            "Сумма операции с округлением": 290.0,
            "Категория": "Фастфуд",
            "Описание": "IP Tupikova A.O.",
        },
        {
            "Дата платежа": "25.12.2021",
            "Сумма операции с округлением": 100.2,
            "Категория": "Госуслуги",
            "Описание": "Почта России",
        },
        {
            "Дата платежа": "25.12.2021",
            "Сумма операции с округлением": 78.0,
            "Категория": "Госуслуги",
            "Описание": "Почта России",
        },
        {
            "Дата платежа": "25.12.2021",
            "Сумма операции с округлением": 53.83,
            "Категория": "Каршеринг",
            "Описание": "Ситидрайв",
        },
    ]


class TestGetExchangeRate(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data='{"user_currencies": ["USD", "EUR"]}')
    @patch('requests.get')
    @patch('os.getenv', return_value='test_api_key')
    def test_get_exchange_rate_success(self, mock_getenv, mock_requests_get, mock_open):
        # Mock the response of the requests.get call
        mock_requests_get.return_value.status_code = 200
        mock_requests_get.return_value.json.return_value = {
            'query': {'from': 'USD'},
            'info': {'rate': 75.5}
        }

        response = get_exchange_rate('path/to/user/file.json')

        assert response == [
            {'currency': 'USD', 'rate': 75.5},
            {'currency': 'USD', 'rate': 75.5}  # предполагаем одинаковый курс для теста
        ]


class TestGetStockPrice(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data='{"user_stocks": ["AAPL", "GOOGL"]}')
    @patch('requests.get')
    @patch('os.getenv', return_value='test_api_key')
    def test_get_stock_price_success(self, mock_getenv, mock_requests_get, mock_open):
        # Mock the response of the requests.get call
        mock_requests_get.return_value.status_code = 200
        mock_requests_get.return_value.json.return_value = [
            {'symbol': 'AAPL', 'price': 150.0},
            {'symbol': 'GOOGL', 'price': 2800.0}
        ]

        response = get_stock_price('path/to/user/file.json')

        expected_response = [
            {'stock': 'AAPL', 'price': 150.0},
            {'stock': 'AAPL', 'price': 150.0}
        ]
        assert response == expected_response
