"""
Задание 1: Доработаем задачи 5-6. Создайте класс-фабрику. Класс принимает тип животного (название одного из созданных классов)
и параметры для этого типа. Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
"""   

class Fabrica():
    def __init__(self, cls, param) -> None:
        self.cls = cls
        self.param = param
    
    def fabrication(self):
        return self.cls(self.param)


class Animals():
    name = None


class Bird(Animals):
    def __init__(self, wingspan) -> None:
        self.wingspan = wingspan

    def get_wingspan(self):
        print(f"Длина крыла: {self.wingspan / 2}")


class Fish(Animals):
    def __init__(self, depth) -> None:
        self.depth = depth

    def get_depth(self):
        print(f"Глубина обитания: {self.depth}")


class Mammal(Animals):
    def __init__(self, weight) -> None:
        self.weight = weight

    def get_weight(self):
        print(f"Вес животного: {self.weight}")


# fabrication = Fabrica(Bird, 120)
# bird = fabrication.fabrication(Bird, 120)
# bird.get_wingspan()

fabrication = Fabrica(Mammal, 250)
mammal = fabrication.fabrication()
mammal.get_weight()