"""Задача 3: Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
Результаты обхода сохраните в файлы json, csv и pickle. Для дочерних объектов указывайте родительскую
директорию. Для каждого объекта укажите файл это или директория. Для файлов сохраните его размер в байтах,
а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий."""

import os


def dir_walk(path):
    """
    Метод рекурсивно обходит все дерево директорий и формирует словарь из имени файла и
    кортежа(тип файла, родительская директория и размер файла), принимая на вход путь к директории.

    :path: str абсолютный путь к директории.
    """

    import pprint


    result = {}
    path = path.replace('\\', '/')

    for root, dirs, files in os.walk(path):
        *_prefix, sufix = root.split("/")
        *_prefix, father = sufix.split("\\")

        for file in files:
            result[file]=("file", father, os.path.getsize(f"{root}\{file}"))

        for dir in dirs:
            result[dir]=("dir", father, get_dir_size(root))

    csv_file("csv_dir.csv", result)
    json_file("json_dir.json", result)
    pickle_file("pickle_dir.pkl", result)


def get_dir_size(path='.'):
    """
    Метод рекурсивно обходит директорию и подсчитывает размер всех файлов,
    вычисляя таким образом размер исходной директории. Возвращает размер директории.

    :path: str путь до директории.
    total_size: str размер исходной директории.
    """

    total_size = 0
    with os.scandir(path) as items:
        for item in items:
            if item.is_file():
                total_size += item.stat().st_size
            elif item.is_dir():
                total_size += get_dir_size(item.path)
    return total_size


def csv_file(file_name, dict_data):
    """
    Метод формирует csv-файл, принимая на вход имя файла и исходный словарь данных.
    :file_name: str имя csv-файла.
    :dict_data: dict словарь данных для преобразования в csv-файл.
    """

    import csv

    fields = ["Имя файла", "Тип файла", "Родительская директория", "Размер файла"]

    with open(file_name, "w", encoding="UTF-8", newline="") as file:
        result = csv.writer(file)
        result.writerow(fields)
        for name, propertys in dict_data.items():
            type_file, father, width = propertys
            result.writerow((name, type_file, father, width))


def json_file(file_name, dict_data):
    """
    Метод формирует json-файл, принимая на вход имя файла и исходный словарь данных.
    :file_name: str имя json-файла.
    :dict_data: dict словарь данных для преобразования в json-файл.
    """

    import json

    with open(file_name, "w", encoding="UTF-8") as file:
        json.dump(dict_data, file)


def pickle_file(file_name, dict_data):
    """
    Метод формирует pickle-файл, принимая на вход имя файла и исходный словарь данных.
    :file_name: str имя pickle-файла.
    :dict_data: dict словарь данных для преобразования в pickle-файл.
    """
    
    import pickle

    with open(file_name, "wb") as file:
        pickle.dump(dict_data, file)


dir_walk(r"C:\Users\HP\Desktop\Project")
