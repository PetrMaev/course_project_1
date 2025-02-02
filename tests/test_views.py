from unittest.mock import patch, mock_open

from freezegun import freeze_time

from src.utils import greeting, cards_info, top_transactions, get_exchange_rate


def test_greeting():
    with freeze_time("2025-01-29 01:00:00"):
        assert greeting() == "Доброй ночи"


def test_cards_info():
    assert cards_info("25.12.2021") == [{'Номер карты': '*5091', 'Сумма операции с округлением': 53.83, 'Кешбэк': 0.54}, {
        'Номер карты': '*7197', 'Сумма операции с округлением': 3873.8999999999996, 'Кешбэк': 38.74}]


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


# @patch("requests.get")
# def test_get_exchange_rate(mock_get):
#     mocked_open = mock_open(read_data='{"user_currencies": ["USD", "EUR"]}')
#     with patch("builtins.open", mocked_open):
#         result = get_exchange_rate(r".\user_settings.json")
#         mock_get.return_value.json.return_value = {
#             "success": True,
#             "query": {"from": "USD", "to": "RUB", "amount": 1},
#             "info": {"timestamp": 1736152444, "rate": 98.33},
#             "date": "2025-01-06",
#             "result": 98.33,
#         }, {
#             "success": True,
#             "query": {"from": "EUR", "to": "RUB", "amount": 1},
#             "info": {"timestamp": 1736152444, "rate": 102.46},
#             "date": "2025-01-06",
#             "result": 102.46,
#         }
#     assert result == [
#         {"currency": "USD", "rate": 98.33},
#         {"currency": "EUR", "rate": 102.46},
#     ]
