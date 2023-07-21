"""Задача 2: Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
Распечатайте его как pickle строку."""

def reader_csv_file(file_name_csv):
    """
    Метод преобразует сым-файл в pickle-строку, принимая на вход имя csv-файла.

    :file_name_csv: str имя csv-файла.
    """

    import csv, pickle
    result = {}

    with open(file_name_csv, "r", encoding="UTF-8", newline="") as file_csv:
        csv_data = csv.reader(file_csv, delimiter='|')
        
        for item, row in enumerate(csv_data):
            user = {}

            if item == 0:
                continue

            user_data = row[0].split(",")
            user[user_data[2]] = user_data[1]

            if add_user:=result.get(user_data[0], user):
                add_user[user_data[2]] = user_data[1]
                result[user_data[0]] = add_user
    
    return pickle.dumps(result)


print(reader_csv_file("csv_file.csv"))
