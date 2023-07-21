"""Задание 1: Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный
csv файл. Для тестированию возьмите pickle версию файла из предыдущей задачи.
Функция должна извлекать ключи словаря для заголовков столбца из переданного файла."""

def pickle_file(file_name):
    """
    Метод генерирует pikle-файл, принимая на вход имя файла.

    :file_name: str имя pickle-файла.
    """

    import pickle

    with open(file_name, "wb") as file:
        test_dict = {"1":{"Алексей": "12345"}, "2": {"Анна": "122346", "Сергей": "123457"}, "3": {"Ольга": "3464567"}}
        pickle.dump(obj=test_dict, file=file)


def csv_file(file_name_csv, file_name_pickle):
    """
    Метод преобразует pickle-файл в csv-файл, принимая на вход два имени файла.

    :file_name_csv: str имя csv-файла.
    :file_name_pickle: str имя pickle-файла.
    """
    
    import csv, pickle

    fields = ["level", "id", "name"]
    with open(file_name_pickle, "rb") as pickle_file, open(file_name_csv, "w", encoding="UTF-8", newline="") as csv_file:
        pickle_dict = pickle.load(pickle_file)
        result = csv.writer(csv_file)
        result.writerow(fields)

        for levels, users in pickle_dict.items():
            for name, user_id in users.items():
                result.writerow((levels, name, user_id))


#pickle_file("pickle_file.pkl")
csv_file("csv_file.csv", "pickle_file.pkl")