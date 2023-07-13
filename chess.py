"""
Задача 1: Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код,
решающий задачу о 8 ферзях. Известно, что на доске 8×8 можно расставить 8 ферзей так,
чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите,
есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел,
каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните
истину, а если бьют - ложь.
"""


def queen(coordinat:list[list]) -> bool:
    """
    Метод принимает на вход список списков, содержащий в себе координаты по X и Y.
    Возвращает True, если ферзи бьют не бьют друг друга и False, если бьют.

    :x:list[int] координаты фферзей по горизонтали.
    :y:list[int] координаты ферзей по вертикали.
    """

    x, y = coordinat[0], coordinat[1]

    for i in range(len(coordinat[0])):
        for j in range(i + 1, len(coordinat[0])):
            if abs(x[j] - x[i]) == abs(y[j] - y[i]):
                return False 
            if x[j] == x[i] or y[j]==y[i]:
                return False

    return True


"""
Задача 2: Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной
расстановки ферзей в задаче выше. Проверяйте различные случайные варианты и выведите 4 успешных
расстановки. *Выведите все успешные варианты расстановок.
"""


def all_successfully(VAL_RESULT=4022):
    """
    Метод генерирует указанное количество возможных успешных положений ферзя.
    При указание количества равного 4022, получим максимальное количество возможных комбинаций.
    4022 - это наименьшее количество комбинаций, которе нужно перебрать для получения правильного
    результата, в их число входит проверка диагонали и контроль вертикали и горизонтали.
    (https://ru.wikipedia.org/wiki/Задача_о_восьми_ферзях).
    Если хочется сильно быстрее то можно установить 1000. Тогда вообще мигом ищет.

    :SIZES_CHESS: int размер поля.
    :VAL_RESULT: int количество комбинаций.
    """

    from random import shuffle

    SIZES_CHESS = 8

    coord_x, coord_y = [i for i in range(1, SIZES_CHESS + 1)], [i for i in range(1, SIZES_CHESS + 1)]
    result = set()
    count = 0

    while count < VAL_RESULT:
        shuffle(coord_x)

        if queen([coord_x, coord_y]) == True:
            result.add(tuple(coord_x))
            count += 1
        
    print_result(result)


def print_result(result:list[list]):
    """
    Метод выводит на печать полученные комбинации.

    :count: int счетчик комбинаций.
    """

    count = 1

    for items in result:
        print(f"\n{count=}\n{'='*18}")
        print(*[i for i in range(9)])

        for i, item in enumerate(items):
            print(f"{i+1}{' _'*(int(item) - 1)}{' x'}{' _'*(8 - int(item))}")
        count += 1


if __name__ == "__main__":

    ALL_RESULT = 4022
    # FOUR_RESULT = 4

    all_successfully(ALL_RESULT)
    # all_successfully(FOUR_RESULT)

