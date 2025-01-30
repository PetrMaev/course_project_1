from unittest.mock import patch, mock_open

from freezegun import freeze_time

from src.views import greeting, cards_info, top_transactions, get_exchange_rate


def test_greeting():
    with freeze_time("2025-01-29 01:00:00"):
        assert greeting() == "Доброй ночи"


def test_cards_info():
    assert cards_info("25.12.2021") == [
        {
            "Номер карты": "*1112",
            "Сумма операции с округлением": 46207.08,
            "Кешбэк": 462.08,
        },
        {
            "Номер карты": "*4556",
            "Сумма операции с округлением": 4144689.17,
            "Кешбэк": 41446.99,
        },
        {
            "Номер карты": "*5091",
            "Сумма операции с округлением": 19816.84,
            "Кешбэк": 198.16,
        },
        {
            "Номер карты": "*5441",
            "Сумма операции с округлением": 470854.8,
            "Кешбэк": 4708.55,
        },
        {
            "Номер карты": "*5507",
            "Сумма операции с округлением": 84000.0,
            "Кешбэк": 840.0,
        },
        {
            "Номер карты": "*6002",
            "Сумма операции с округлением": 69200.0,
            "Кешбэк": 692.0,
        },
        {
            "Номер карты": "*7197",
            "Сумма операции с округлением": 2557824.54,
            "Кешбэк": 25579.12,
        },
    ]


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
