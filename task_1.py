"""
Задача 1: Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""

# Test Linux: "/home/a/Test/Test_5/main.py"
# Test Windows: "C:\Users\Professional\Desktop\main.py"

pathFile = input("Введите путь до файла: ")


def fun(pathFile:str) -> tuple:
    """
    Метод принимает путь до файла и возвращает кортеж: (путь, имя, расширение).

    :path: str  путь до файла.
    :name: str имя файла.
    :ext: str расширение файла.
    """

    *path, file = pathFile.replace("\\", "/").split("/")
    name, ext = file.split(".")
    return "/".join(path), name, ext


print(fun(pathFile))
