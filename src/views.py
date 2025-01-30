import json

from config import PATH_TO_USER_SETTINGS
from src.utils import cards_info, get_exchange_rate, get_stock_price, greeting, top_transactions


def views(set_time: str) -> str:
    """ Собирает все данные и возвращает JSON-объект """
    views_dict = {'greeting': greeting(), 'cards': cards_info(set_time),
                  'top_transactions': top_transactions(set_time),
                  'currency_rates': get_exchange_rate(PATH_TO_USER_SETTINGS),
                  'stock_prices': get_stock_price(PATH_TO_USER_SETTINGS)}
    return json.dumps(views_dict, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    print(views('25.12.2021'))
