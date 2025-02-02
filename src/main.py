import pandas as pd

from config import PATH_TO_OPERATIONS
from src.reports import spending_by_category
from src.services import get_transactions_with_phone_numbers, simple_searching
from src.views import views


def main_views() -> str:
    """ Вызов функции из модуля "Веб-страницы" """
    result = views('25.12.2021')
    return result


def main_services_1() -> str:
    """ Вызов функции из модуля "Сервисы", возвращающей транзакции, содержащие в описании мобильные номера """
    df_transactions = pd.read_excel(PATH_TO_OPERATIONS)
    transactions = df_transactions.to_dict(orient='records')
    result = get_transactions_with_phone_numbers(transactions)
    return result


def main_services_2() -> str:
    """ Вызов функции простого поиска из модуля "Сервисы" """
    df_transactions = pd.read_excel(PATH_TO_OPERATIONS)
    transactions = df_transactions.to_dict(orient='records')
    result = simple_searching(transactions, "Магнит")
    return result


def main_reports() -> str:
    """
    Вызов функции из модуля "Отчеты", которая возвращает траты по заданной категории
    за последние три месяца от переданной даты
    """
    df_transactions = pd.read_excel(PATH_TO_OPERATIONS)
    result = spending_by_category(df_transactions, 'Аптеки', '08.2018')
    return result


if __name__ == '__main__':
    print(main_views())
    print(main_services_1())
    print(main_services_2())
    print(main_reports())
