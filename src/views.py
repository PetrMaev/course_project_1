import json
import os
from datetime import datetime, time

import pandas as pd
import requests
from dotenv import load_dotenv

from config import PATH_TO_OPERATIONS

load_dotenv()


def greeting() -> str:
    """ Функция приветствия, в зависимости от текущего времени """
    time_now = datetime.now().time()
    if time(hour=23) < time_now <= time(hour=23, minute=59, second=59) or time(hour=0) < time_now <= time(hour=6):
        return 'Доброй ночи'
    elif time(hour=18) < time_now <= time(hour=23):
        return 'Добрый вечер'
    elif time(hour=12) < time_now <= time(hour=18):
        return 'Добрый день'
    else:
        return 'Доброе утро'


def cards_info(df_transactions: pd.DataFrame) -> str:
    """ Возвращает информацию по каждой карте """
    df_transactions_sort = df_transactions.loc[df_transactions['Сумма платежа'] < 0]
    cashback = df_transactions_sort['Сумма операции с округлением'] / 100
    df_transactions['Кешбэк'] = cashback
    grouped_df = df_transactions.groupby('Номер карты').agg(
        {'Сумма операции с округлением': 'sum', 'Кешбэк': 'sum'}).reset_index()
    result = grouped_df.loc[:, ['Номер карты', 'Сумма операции с округлением', 'Кешбэк']]
    result_to_dict = result.to_dict(orient='records')
    return json.dumps(result_to_dict, ensure_ascii=False, indent=4)


def top_transactions(df_transactions: pd.DataFrame, pay_amount: int | float) -> str:
    """ Возвращает топ 5 транзакций по сумме платежа """
    sorted_df = df_transactions.loc[df_transactions['Сумма операции с округлением'] < pay_amount]
    top_5 = sorted_df.sort_values(by='Сумма операции с округлением', ascending=False).head()
    top_transactions_sort = top_5.loc[:, ['Дата платежа', 'Сумма операции с округлением', 'Категория', 'Описание']]
    top_5_dict = top_transactions_sort.to_dict(orient='records')
    return json.dumps(top_5_dict, ensure_ascii=False, indent=4)


def get_exchange_rate() -> str:
    """ Получение актуальных данных курса валют """
    # Получение курса доллара
    payload = {"to": "RUB", "from": "USD"}
    get_api = os.getenv("API_KEY_CURRENCIES")
    headers = {"apikey": f"{get_api}"}
    url = f"https://api.apilayer.com/exchangerates_data/convert?&amount=1"
    response = requests.get(url, headers=headers, params=payload)
    response.raise_for_status()
    currency_usd = response.json()['query']['from']
    rate_usd = response.json()['info']['rate']
    # Получение курса евро
    payload = {"to": "RUB", "from": "EUR"}
    get_api = os.getenv("API_KEY_CURRENCIES")
    headers = {"apikey": f"{get_api}"}
    url = f"https://api.apilayer.com/exchangerates_data/convert?&amount=1"
    response = requests.get(url, headers=headers, params=payload)
    response.raise_for_status()
    currency_eur = response.json()['query']['from']
    rate_eur = response.json()['info']['rate']
    # Вывод результата
    result = dict()
    result["currency_rates"] = {"currency": currency_usd, "rate": rate_usd}, {"currency": currency_eur,
                                                                              "rate": rate_eur},
    return json.dumps(result, ensure_ascii=False, indent=4)


def get_stock_price() -> str:
    """ Получение актуальных данных стоимости акций """
    stock = "AAPL"
    get_api = os.getenv("API_KEY_STOCKS")
    url = f"https://financialmodelingprep.com/api/v3/quote-short/{stock}?apikey={get_api}"
    response = requests.get(url)
    response.raise_for_status()
    stock_name = response.json()[0]['symbol']
    stock_price = round(response.json()[0]['price'], 2)
    result = dict()
    result["stock_prices"] = {"stock": stock_name, "price": stock_price}
    return json.dumps(result, ensure_ascii=False, indent=4)


def views():
    """ Собирает все данные и возвращает JSON-объект """
    pass



if __name__ == '__main__':
    print(greeting())
    df_operations = pd.read_excel(PATH_TO_OPERATIONS)
    # print(top_transactions(df_operations, 800))
    # print(cards_info(df_operations))
    # print(get_exchange_rate())
    # print(get_stock_price())
