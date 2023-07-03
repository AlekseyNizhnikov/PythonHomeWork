"""
Задача 2: Напишите функцию для транспонирования матрицы.
"""

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("До:")
print(*matrix, sep="\n")
print()


def transparentMatrix(matrix: list[list]) -> list[tuple]:
    """
    Метод принимает на вход матрицу и транспонирует ее, возращая список кортежей.
    """

    return zip(*matrix)


print("После:")
print(*transparentMatrix(matrix), sep="\n")