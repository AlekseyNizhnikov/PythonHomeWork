"""
Задача 3: Напишите программу, которая принимает две строки вида “a/b” - дробь с
числителем и знаменателем. Программа должна возвращать сумму и произведение* дробей.
Для проверки своего кода используйте модуль fractions.
"""

def calculate(task: list) -> list:
    result_plus, result_mult = list(), list()
    denominator = None

    for i in range(len(task) - 1, 1, -1):
        result_mult.append(task[i] * task[i-2])

        if not denominator:
            denominator = task[i] * task[i-2]
            result_plus.append(denominator)
            result_plus.append(task[i] * task[i-(len(task) - 1)])
        else:
            result_plus.append(result_plus.pop() + (task[i] * task[i-1]))
    
    result_plus = increments(result_plus)
    result_mult = increments(result_mult)

    return result_plus, result_mult


def increments(task: list) -> list:
    for i in range(2, max(task)):
        if task[0] % i == 0 and task[1] % i == 0:
            task[i] = [lambda x=x: int(task[x] / i) for x in range(2)]
    
    return task


def print_task(tasks: list):
    operation = ("сложения", "умножения")

    for task, oper in zip(tasks, operation):
        result = '/'.join(map(str, task[::-1]))
        print(f"Результат {oper} дробей: {result}")    


def check(fraction_1: tuple, fraction_2: tuple, tasks: list):
    from fractions import Fraction

    x = "/".join(map(str, fraction_1))
    y = "/".join(map(str, fraction_2))

    result_plus = Fraction(x) + Fraction(y)
    result_mult = Fraction(x) * Fraction(y)

    for task in tasks:
        result = '/'.join(map(str, task[::-1]))
        print(f"Проверка: {str(result_plus) == result or str(result_mult) == result}")

 
while True:
    fraction_1 = tuple(map(int, input("Введите первую дробь вида a/b: ").split("/")))
    fraction_2 = tuple(map(int, input("Введите вторую дробь вида c/d: ").split("/")))
    break

equation = fraction_1 + fraction_2
result = calculate(equation)

print_task(result)
check(fraction_1, fraction_2, result)                                                                                                        