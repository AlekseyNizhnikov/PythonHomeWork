from time import time


class MyString(str):
    """
    Класс расширяет класс str, добавляя ему два новых атрибута.
    :author_name: str имя автора строки.
    :creat_time: int время создания.
    """

    def __new__(cls, value, author_name):
        instance = super().__new__(cls, value)
        instance.author_name = author_name
        instance.creat_time = time()
        return instance

    def __str__(self) -> str:
        return f"{self.author_name}: {self.creat_time}"


test = MyString(1212, "Алекксей")
print(test)
print(test.__doc__)
