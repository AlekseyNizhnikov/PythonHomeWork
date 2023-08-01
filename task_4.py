"""
Задание 2: Создайте класс Матрица. Добавьте методы для: вывода на печать, проверку
на равенство, сложения, *умножения матриц.
"""


class Matrix:
    """
    Класс создает экземпляр матрицы, которые можно складывать, умножать и сравнивать друг с другом.
    """  

    def __init__(self, matrix_a=None) -> None:
        self.matrix_a = matrix_a

    def __add__(self, other: object) -> float:
        """
        Метод вызывается при сложение объектов Matrix.

        :result: list[list[int]] результат сложения матриц.
        """

        result = [[a + b for a, b in zip(row_1, row_2)] if row_1 == row_2 and self.matrix_a == other.matrix_a else None for row_1, row_2 in zip(self.matrix_a, other.matrix_a)]
        if None in result:
            return None
        
        return Matrix(result)

    def __mul__(self, other):
        """
        Метод вызывается при умножение объектов Matrix.

        :result: list[list[int]] результат умножения матриц.
        """
                
        for row in other.matrix_a:
            if len(self.matrix_a) != len(row):
                return None

        result = [[sum(a * b for a, b in zip(row_1, col_2)) for col_2 in zip(*other.matrix_a)] for row_1 in self.matrix_a]
        return Matrix(result)

    def __eq__(self, other: object) -> bool:
        """
        Метод вызывается, при проверке равенства двух матриц. Матрицы равны тогда и толко тогда, когда равны их элементы.
        """

        return False not in [False for row_1, row_2 in zip(self.matrix_a, other.matrix_a) if row_1 != row_2 or self.matrix_a != other.matrix_a]
    
    def __gt__(self, other):
        """
        Метод вызывается при проверке какой объект Matrix больше. По сути, чтоб не было ошибки при некорректном вводе.
        Так как матрица не может быть больше или меньше, они либо равны поэлементно, либо - нет.
        """

        return None
    
    def __le__(self, other):
        """
        Метод вызывается при проверке какой объект Matrix больше. По сути, чтоб не было ошибки при некорректном вводе.
        Так как матрица не может быть больше или меньше, они либо равны поэлементно, либо - нет.
        """
                
        return None

    def __str__(self) -> str:
        return f"Матрица: {self.matrix_a}"
    

mtr_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(mtr_1)
mtr_2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
print(mtr_2)

print(mtr_1 * mtr_2)
