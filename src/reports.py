import json
import logging
import os
from datetime import datetime, timedelta
from functools import wraps
from typing import Optional, Callable, Any

import pandas as pd

from config import PATH_TO_OPERATIONS, PATH_TO_REPORTS_LOGS

logger = logging.getLogger()
file_handler = logging.FileHandler(PATH_TO_REPORTS_LOGS, "w", encoding="utf-8")
logger.addHandler(file_handler)
file_formatter = logging.Formatter(
    "%(asctime)s; %(filename)s; %(levelname)s; %(message)s", "%d-%m-%Y %H:%M:%S"
)
file_handler.setFormatter(file_formatter)
logger.setLevel(logging.DEBUG)


def spending_by_category(transactions: pd.DataFrame, category: str,
                         date: Optional[str] = None) -> str:
    """ Функция возвращает траты по заданной категории за последние три месяца от переданной даты """
    logger.info(f'Начало работы функции вывода транзакций за три месяца от даты: {date} по категории: "{category}"')
    transaction_date_sorted = []
    if date is None:
        date_end = datetime.now()
        date_start = date_end - timedelta(days=90)
        transactions_sort = transactions[transactions['Категория'] == category]
        transactions_sort_dict = transactions_sort.to_dict(orient='records')
        for transaction in transactions_sort_dict:
            transaction_date = datetime.strptime(transaction['Дата операции'], '%d.%m.%Y %H:%M:%S')
            if date_start <= transaction_date <= date_end:
                transaction_date_sorted.append(transaction)

    elif date:
        date_end = datetime.strptime(date, '%m.%Y')
        date_start = date_end - timedelta(days=90)
        transactions_sort = transactions[transactions['Категория'] == category]
        transactions_sort_dict = transactions_sort.to_dict(orient='records')
        for transaction in transactions_sort_dict:
            transaction_date = datetime.strptime(transaction['Дата операции'], '%d.%m.%Y %H:%M:%S')
            if date_start <= transaction_date <= date_end:
                transaction_date_sorted.append(transaction)
    logger.info(f'Успешно. Вывод транзакций по категории: "{category}" за период: "{date_start} - {date_end}"')
    return json.dumps(transaction_date_sorted, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    df_transactions = pd.read_excel(PATH_TO_OPERATIONS)
    print(spending_by_category(df_transactions, 'Каршеринг', '12.2021'))
