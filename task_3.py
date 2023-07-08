"""
Задача 3: Создайте функцию генератор чисел Фибоначчи (см. Википедию).
"""


def fibonachi() -> int:
    """
    Генератор возвращает текущее число Фибоначи.
    """
    count_1 = 0
    count_2 = 1
    while True:
        yield  count_1
        count_1, count_2 = count_2, count_1 + count_2


number = int(input("Введите число: "))
fib = fibonachi()

for _ in range(number):
    print(next(fib))