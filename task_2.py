"""
Задача 2: Возьмите 1-3 любые задачи из прошлых семинаров, которые вы уже решали. Превратите функции в методы класса.
Задачи должны решаться через вызов методов экземпляра.
"""

import json
import os


class DecoratorJSON():
    """
    Класс декоратор. Формирует json-файл из результата работы функции и переданных ей аргументов.
    """
    
    def __init__(self, function) -> None:
        self.function = function

        if os.path.exists(f"/{self.function.__name__}.json"):
            with open(f"{self.function.__name__}.json", "r", encoding="UTF-8") as file:
                self.result_list = file.readlines()
        else:
            self.result_list = []

        self.file_name = function.__name__

    def __call__(self, *args, **kwargs):
        result = self.function(*args, **kwargs)
        res_dict = {"args": args,
                    "kwargs": kwargs,
                    "result": result}
        
        self.result_list.append(res_dict)

        with open(f"{self.file_name}.json", "w", encoding="UTF-8") as file:
            json.dump(self.result_list, file)

        return result

        
@DecoratorJSON
def solution_of_equation(arg_a:int, arg_b:int, arg_c:int) -> str:
    """
    Метод находит корни квадратного уравнения.

    :slf.arg_a: int аргумент а.
    :self.arg_b: int аргумент b.
    :self.arg_c: int аргумент c.
    """

    d = (arg_b**2 - 4 * arg_a * arg_c)**0.5

    if type(d) == complex or d < 0:
        return "Корней нет"
    
    elif d == 0:
        x_1 = (arg_b * (-1)) / (2 * arg_a)
        return f"Один корень: {x_1}"
    
    elif d > 0:
        x_1 = (arg_b*(-1) + d) / (2 * arg_a)
        x_2 = (arg_b*(-1) - d) / (2 * arg_a)
        return f"Два корня: {x_1} и {x_2}"


print(solution_of_equation(1, 10, 7))
print(solution_of_equation(1, 10, 8))