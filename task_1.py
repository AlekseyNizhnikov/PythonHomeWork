"""
Задача 1: Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
Напишите функцию, которая при запуске заменяет содержимое переменных оканчивающихся
на s (кроме переменной из одной буквы s) на None. Значения не удаляются, а
помещаются в одноимённые переменные без s на конце.
"""

numb = 1234
numbers = (123, 123, 123)
s = "123" 

print(f"До: {numb = }, {numbers = }, {s = }")


def fun():
    """
    Функция создает в глобальной области видимости новую(ые) переменную(ые).

    :all_parametrs list: список всех параметров в глобальной области видимости.
    """

    all_parameetrs = list(filter(lambda x: not x.startswith("__") and x.endswith("s") and len(x) > 1, globals()))

    for i in all_parameetrs:
        globals()[i[:-1]], globals()[i] = globals()[i], None

    return globals()


fun()

print(f"После: {numb = }, {numbers = }, {s = }, {number = }")
