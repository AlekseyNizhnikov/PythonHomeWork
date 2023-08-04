"""
Создайте класс студента.
* Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
* Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
* Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
* Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.
"""

import csv, os
from random import randint


class NameDescriptor:
    """
    Дескриптор. Проверяет ФИО пользователя.
    """

    def __init__(self):
        pass
    
    def __set_name__(self, owner, name):
        """
        Магический метод, который отлавливает имя атрибута вызывающего дескриптор и создает новую, защищенную переменную.
        """

        self.param_name = "_" + name

    def __get__(self, instance, owner):
        """
        Метод получает объект дескриптора, и обращается к созданной ранее защищенной переменной self.param_name.
        """

        return getattr(instance, self.param_name)
    
    def __set__(self, instance, value):
        """
        Метод записсывает в переменную self.param_name значение атрибута, если он прошел проверку self.chek_name.
        """

        self.chek_name(value)
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        """
        Метод вызывает ошибку AtributeError, если свойство пытаются удалить.
        """

        raise AttributeError(f"Свойство {self.param_name} нельзя удаляять.")

    def chek_name(self, value):
        """
        Метод проверяет, является ли переданный объект строкой, состоящей только из букв и начинается ли строка с заглавной буквы.
        Иначе вызывает ошибку.
        """

        if not value.isalpha():
            raise TypeError(f"Значение {value} должно состоять из букв.")
        
        if value != value.title():
            raise ValueError(f"Значение {value} должно начинаться с заглавной буквы.")


class Student:
    """
    Класс-методо студента.
    """

    _name = NameDescriptor()

    def __init__(self) -> None:
        self._MIN_EST = 2
        self._MAX_EST = 5
        self._MIN_TEST = 0.0
        self._MAX_TEST = 100.0
    
        self._midle_estimation = -1.0
        self._midle_test = -1.0

    def __call__(self, name):
        """
        Метод позволяет обращаться к классу как к методу.
        Считываем данные о предметах, генерируем случайным образом оценки для них.
        """

        self._name = name
        self._subject = self._load_subjects()
        self._estimation()
        return self

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
    
    def _estimation(self):
        """
        Метод генерирует случайные оценки и баллы для всех предметов и подсчитывает среднее значение.

        :self._midle_estimation: int средняя оценка.
        :self._midle_test: int средний балл.
        """

        subjects = self._subject.split(",")
        self._midle_estimation = sum([randint(self._MIN_EST, self._MAX_EST) for _ in subjects]) / len(subjects)
        self._midle_test = sum([randint(self._MIN_TEST, self._MAX_TEST) for _ in subjects]) / len(subjects)

    def _load_subjects(self):
        """
        Метод вызывает контекстного менеджера и считывает содержимое файла, с предметами.
        """

        with Subject("subject.csv") as f:
            result = f.read()
        return result

    def __repr__(self):
        return f"Имя студента: {self._name}\nПредметы: {self._subject}\nСредняя оценка: {self._midle_estimation}\nСредний балл: {self._midle_test}\n"

    
class Subject:
    """
    Контекстный менеджер. Ищет csv файл по имени, содержащий наименование предметов.
    При необходимости создает и заполняет этот файл.
    """

    def __init__(self, file_name) -> None:
        self.file_name = file_name
        self.file = None

    def __enter__(self):
        subject = ["Русский язык", "Математика", "Физкультура", "Литература", "История"]

        if not os.path.exists(self.file_name):
            with open(self.file_name, "a", encoding="UTF-8", newline="") as file:
                csv_write = csv.writer(file)
                csv_write.writerow(subject)


        self.file = open(self.file_name, "r", encoding="UTF-8", newline="")
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


st = Student()
print(st("Алексей"))
print(st("Сергей"))
#print(st.__dict__)

