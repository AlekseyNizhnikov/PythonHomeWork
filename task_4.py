"""
Задание 2: Создайте класс Матрица. Добавьте методы для: вывода на печать, проверку
на равенство, сложения, *умножения матриц.
"""


class Matrix:
    """
    """  

    def __init__(self, matrix_a=None) -> None:
        self.matrix_a = matrix_a

    def __add__(self, other: object) -> float:
        result = []
        if len(self.matrix_a) == len(other.matrix_a):
            for i, j in zip(self.matrix_a, other.matrix_a):
                res = []
                if len(i) != len(j):
                    return None
                res = [x + y for x, y in zip(i, j)]
                result.append(res)
        return Matrix(result)

    def __mul__(self, other):
        for i in other.matrix_a:
            if len(self.matrix_a) != len(i):
                return None
        res = [[0 for x in range(3)] for y in range(3)]
 
        for i in range(len(self.matrix_a)):
            for j in range(len(other.matrix_a[0])):
                for k in range(len(other.matrix_a)):
                    res[i][j] += self.matrix_a[i][k] * other.matrix_a[k][j]
        return Matrix(res)

    def __eq__(self, other: object) -> bool:
        return bool([[1 for i, j in zip(row_1, row_2) if i != j] for row_1, row_2 in zip(self.matrix_a, other.matrix_a) if len(row_1) != len(row_2) and len(self.matrix_a) == len(other.matrix_a)])
        # for i, j in zip(self.matrix_a, other.matrix_a):
        #     if len(i) != len(j):
        #         return False
        #     for x, y in zip(i, j):
        #         if x != y:
        #             return False           

    def __str__(self) -> str:
        return f"Матрица: {self.matrix_a}"
    
mtr_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(mtr_1)
mtr_2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) # [2, 3, 4], [5, 6, 7], [8, 9, 0]
print(mtr_2)

print(mtr_1 == mtr_2)
