import os, csv, json, pickle

class ConvertFileInfo():
    def __init__(self, path) -> list[dict]:
        self.path = path


    def pickle_file(function):
        """
        Метод формирует pickle-файл, принимая на вход имя файла и исходный словарь данных.
        :file_name: str имя pickle-файла.
        :dict_data: dict словарь данных для преобразования в pickle-файл.
        """
        def _wrapper(*args, **kwargs):
            file_name = function.__name__
            data = function(*args, *kwargs)

            with open(f"{file_name}.pkl", "wb") as file:
                pickle.dump(data, file)
        
        return _wrapper
    
    def csv_file(function):
        """
        Метод формирует csv-файл, принимая на вход имя файла и исходный словарь данных.
        :file_name: str имя csv-файла.
        :dict_data: dict словарь данных для преобразования в csv-файл.
        """
        def _wrapper(*args, **kwargs):
            fields = ["Имя файла", "Тип файла", "Родительская директория", "Размер файла"]
            file_name = function.__name__
            data = function(*args, **kwargs)

            with open(f"{file_name}.csv", "w", encoding="UTF-8", newline="") as file:
                result = csv.writer(file)
                result.writerow(fields)
                for obj in data:
                    for name, propertys in obj.items():
                        type_file, father, width = propertys
                        result.writerow((name, type_file, father, width))
        return _wrapper
    

    def json_file(function):
        """
        Метод формирует json-файл, принимая на вход имя файла и исходный словарь данных.
        :file_name: str имя json-файла.
        :dict_data: dict словарь данных для преобразования в json-файл.
        """
        def _wrapper(*args, **kwargs):
            file_name = function.__name__
            data = function(*args, **kwargs)

            with open(f"{file_name}.json", "w", encoding="UTF-8") as file:
                json.dump(data, file)
            
        return _wrapper

    @pickle_file
    @json_file
    @csv_file
    def dir_walk(self):
        """
        Метод рекурсивно обходит все дерево директорий и формирует словарь из имени файла и
        кортежа(тип файла, родительская директория и размер файла), принимая на вход путь к директории.

        :path: str абсолютный путь к директории.
        """

        result = []
        self.path = self.path.replace('\\', '/')

        for root, dirs, files in os.walk(self.path):
            *_prefix, sufix = root.split("/")
            *_prefix, father = sufix.split("\\")

            for file in files:
                result.append({file: ("file", father, os.path.getsize(f"{root}\{file}"))})

            for dir in dirs:
                result.append({dir: ("dir", father, self.get_dir_size(root))})

        return result


    def get_dir_size(self, path):
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
                    total_size += self.get_dir_size(item.path)
        return total_size


cfi = ConvertFileInfo("/home/a/Test/Liza")
cfi.dir_walk()