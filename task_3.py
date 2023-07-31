class Rectangle:
    """
    Класс создает объект прямоугольник, принимая на вход длину и ширину, либо просто длину.
    Переопределяет методы вычитания, сложения и сравнения, позволяя скалдывать объекты Rectangle
    и сравнивать их между собой.
    """

    def __init__(self, a, b=None) -> None:
        """
        :a: int длина прямоугольника.
        :b: int ширина прямоугольника.
        """

        self.a, self.b = a, b
        if self.b is None:
            self.b = a

    def get_square(self):
        """
        Метод возвращает площадь прямоугольника.
        """

        return self.a * self.b
    
    def get_perimetr(self):
        """
        Метод возвращает периметр прямоугольника.
        """

        return 2 * ( self.a + self.b)
    
    def __add__(self, other):
        perimetr = self.get_perimetr() + other.get_perimetr()
        return Rectangle(perimetr/4, perimetr/4)
    
    def __sub__(self, other):
        perimetr = abs(self.get_perimetr() - other.get_perimetr())
        return Rectangle(perimetr/4, perimetr/4)

    def __eq__(self, __value: object) -> bool:
        return self.get_square() == __value.get_square()
    
    def __gt__(self, __value: object) -> bool:
        return self.get_square() > __value.get_square()

    def __le__(self, __value: object) -> bool:
        return self.get_square() >= __value.get_square()


r_1 = Rectangle(4, 1)
print(r_1.get_perimetr())
#print(r_1.get_square())

r_2 = Rectangle(4, 17)
print(r_2.get_perimetr())
#print(r_2.get_square())

r_3 = r_1 - r_2
print(r_3.get_perimetr())
print(r_3 < r_1)
print(r_3.__doc__)
