from datetime import datetime, time


def greeting() -> str:
    """ Функция приветствия, в зависимости от текущего времени """
    time_now = datetime.now().time()
    if time(hour=23) < time_now <= time(hour=23, minute=59, second=59) or time(hour=0) < time_now <= time(hour=6):
        return "Доброй ночи"
    elif time(hour=18) < time_now <= time(hour=23):
        return "Добрый вечер"
    elif time(hour=12) < time_now <= time(hour=18):
        return "Добрый день"
    else:
        return "Доброе утро"



if __name__ == '__main__':
    print(greeting())
