import json
import logging
import re
from typing import Any

import pandas as pd

from config import PATH_TO_OPERATIONS, PATH_TO_SERVICES_LOGS

logger = logging.getLogger()
file_handler = logging.FileHandler(PATH_TO_SERVICES_LOGS, "w", encoding="utf-8")
logger.addHandler(file_handler)
file_formatter = logging.Formatter(
    "%(asctime)s; %(filename)s; %(levelname)s; %(message)s", "%d-%m-%Y %H:%M:%S"
)
file_handler.setFormatter(file_formatter)
logger.setLevel(logging.DEBUG)


def simple_searching(transactions_list: list[dict[str, Any]], search_str: str) -> str:
    """ Функция поиска транзакций по описанию или категории """
    logger.info('Начало работы функции поиска транзакций по описанию или категории')
    result = []
    for transaction in transactions_list:
        if re.search(f'.*{search_str}.*', str(transaction['Категория']), flags=re.IGNORECASE):
            result.append(transaction)
        elif re.search(f'.*{search_str}.*', str(transaction['Описание']), flags=re.IGNORECASE):
            result.append(transaction)
    logger.info(f'Успешно. Вывод транзакций по критерию "{search_str}"')
    return json.dumps(result, ensure_ascii=False)


def get_transactions_with_phone_numbers(transactions_list: list[dict[str, Any]]) -> str:
    """ Функция возвращает JSON со всеми транзакциями, содержащими в описании мобильные номера """
    logger.info('Начало работы функции вывода транзакций, содержащие в описании мобильные номера')
    result = []
    for transaction in transactions_list:
        if re.search(r'.*\W\d\s\d{3}.', transaction['Описание'], flags=re.IGNORECASE):
            result.append(transaction)
    logger.info('Успешно. Вывод транзакций, содержащие в описании мобильные номера')
    return json.dumps(result, ensure_ascii=False)


if __name__ == '__main__':
    df_transactions = pd.read_excel(PATH_TO_OPERATIONS)
    transactions = df_transactions.to_dict(orient='records')
    print(get_transactions_with_phone_numbers(transactions))
    # print(simple_searching(transactions, "Магнит"))
