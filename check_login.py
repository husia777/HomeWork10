import re
import json
from typing import Any


def get_login(pk_input: str) -> Any:
    """
    Загружает данные о студентах из файла
    :return: Выводит логин студента
    """
    with open('students.json') as file:
        contents = json.load(file)
    for i in contents:
        if pk_input == i['pk']:
            return i['login']



def correct_login(login: str) -> Any:
    """
    Проверка логина по регулярному выражению
    :param login: Логин студента
    :return: Возвращаем строку с логином и его корректностью
    """
    response = re.compile(r'^[a-z][A-Za-z0-9]+[\W |_]{1}[a-z0-9]+$')
    is_correct_login = response.search(login)
    k = bool(is_correct_login)
    print(f'Логин {login} {"корректен" if k else "не корректен"}')
