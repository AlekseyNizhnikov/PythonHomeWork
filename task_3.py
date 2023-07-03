"""
Задача 3: Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем,
используйте его строковое представление.
"""

arg_1 = []
arg_2 = 123.0
arg_3 = "123"


def key_parametrs(**kwargs) -> dict:
    """
    Метод проверяет есть ли у переменной магический метод __hash__ и если есть, возвращает словарь.
    """

    return {val if val.__hash__ else str(val): key for key, val in kwargs.items()}



print(key_parametrs(arg_1=arg_1, arg_2=arg_2, arg_3=arg_3))