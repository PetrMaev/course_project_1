import json
import os
from datetime import datetime, time
from typing import Any

import pandas as pd
import requests
from dotenv import load_dotenv

from config import PATH_TO_OPERATIONS, PATH_TO_USER_SETTINGS

load_dotenv()


def greeting() -> str:
    """ Возвращает приветствие, в зависимости от текущего времени """
    time_now = datetime.now().time()
    if time(hour=23) < time_now <= time(hour=23, minute=59, second=59) or time(hour=0) <= time_now <= time(hour=3,
                                                                                                           minute=59,
                                                                                                           second=59):
        return 'Доброй ночи'
    elif time(hour=18) < time_now <= time(hour=23):
        return 'Добрый вечер'
    elif time(hour=12) < time_now <= time(hour=18):
        return 'Добрый день'
    else:
        return 'Доброе утро'


def cards_info(set_time: str) -> Any:
    """ Возвращает информацию по каждой карте """
    df_transactions = pd.read_excel(PATH_TO_OPERATIONS)
    cashback = round(df_transactions['Сумма операции с округлением'] / 100, 2)
    df_transactions['Кешбэк'] = cashback
    df_transactions_sort = df_transactions.loc[
        (df_transactions['Сумма платежа'] < 0) & (df_transactions['Дата платежа'] == set_time)]
    grouped_df = df_transactions_sort.groupby('Номер карты').agg(
        {'Сумма операции с округлением': 'sum', 'Кешбэк': 'sum'}).reset_index()
    result = grouped_df.loc[:, ['Номер карты', 'Сумма операции с округлением', 'Кешбэк']]
    result_dict = result.to_dict(orient='records')
    return result_dict


def top_transactions(set_time: str) -> Any:
    """ Возвращает топ 5 транзакций по сумме платежа """
    df_transactions = pd.read_excel(PATH_TO_OPERATIONS)
    df_transactions_sort = df_transactions.loc[
        (df_transactions['Сумма платежа'] < 0) & (df_transactions['Дата платежа'] == set_time)]
    top_5 = df_transactions_sort.sort_values(by='Сумма операции с округлением', ascending=False).head()
    top_transactions_sort = top_5.loc[:, ['Дата платежа', 'Сумма операции с округлением', 'Категория', 'Описание']]
    top_5_dict = top_transactions_sort.to_dict(orient='records')
    return top_5_dict


def get_exchange_rate(path_to_user_file: str) -> list:
    """ Получение актуальных данных курса валют """
    currency_list = []
    with open(path_to_user_file) as user_file:
        data = json.load(user_file)
    for currency in data['user_currencies']:
        currency_dict = {}
        payload = {"to": "RUB", "from": f"{currency}"}
        get_api = os.getenv("API_KEY_CURRENCIES")
        headers = {"apikey": f"{get_api}"}
        url = "https://api.apilayer.com/exchangerates_data/convert?&amount=1"
        response = requests.get(url, headers=headers, params=payload)
        response.raise_for_status()
        currency_dict['currency'] = response.json()['query']['from']
        currency_dict['rate'] = round(response.json()['info']['rate'], 2)
        currency_list.append(currency_dict)
    return currency_list


def get_stock_price(path_to_user_file: str) -> list:
    """ Получение актуальных данных стоимости акций """
    stocks_list = []
    with open(path_to_user_file) as user_file:
        data = json.load(user_file)
    for stock in data['user_stocks']:
        stocks_dict = {}
        get_api = os.getenv("API_KEY_STOCKS")
        url = f"https://financialmodelingprep.com/api/v3/quote-short/{stock}?apikey={get_api}"
        response = requests.get(url)
        response.raise_for_status()
        stocks_dict["stock"] = response.json()[0]['symbol']
        stocks_dict["price"] = round(response.json()[0]['price'], 2)
        stocks_list.append(stocks_dict)
    return stocks_list


if __name__ == '__main__':
    print(greeting())
    print(cards_info('25.12.2021'))
    # print(top_transactions('25.12.2021'))
    # print(get_exchange_rate(PATH_TO_USER_SETTINGS))
    # print(get_stock_price(PATH_TO_USER_SETTINGS))
