"""Доработаем задачи 3 и 4. Создайте класс Project, содержащий атрибуты – список пользователей проекта и админ проекта. Класс имеет следующие методы:
Классовый метод загрузки данных из JSON файла (из второй задачи 8 семинара)
Метод входа в систему – требует указать имя и id пользователя. Далее метод создает пользователя и проверяет есть ли он в списке пользователей проекта. Если в списке его нет, то вызывается исключение доступа. Если пользователь присутствует в списке пользователей проекта, то пользователь, который входит получает его уровень доступа и становится администратором.
Метод добавление пользователя в список пользователей. Если уровень пользователя меньше, чем уровень админа, вызывайте исключение уровня доступа.
* метод удаления пользователя из списка пользователей проекта
* метод сохранения списка пользователей в JSON файл при выходе из контекстного менеджера"""

import json


class Error(Exception):
    pass

class LevelError(Error):
    """
    Класс обработки исключения. Проверяет уровень доступа порльзователя.
    """

    def __init__(self, level, name, *args) -> None:
        super().__init__(*args)
        self.level = level
        self.name = name

    def __str__(self) -> str:
        return f"Уровень доступа '{self.level}' пользователя '{self.name}' слишком низкий."

class AcessError(Error):
    """
    Класс обработки исключения. Проверяет наличие пользователя, который входит в систему.
    """

    def __init__(self, name, *args) -> None:
        super().__init__(*args)
        self.name = name

    def __str__(self) -> str:
        return f"Пользователь с именем '{self.name}' не найден."


class User:
    """
    Класс пользователя. Принимает в конструктор имя, идентификатор и уровень доступа.
    """

    def __init__(self, name, user_id, level=0):
        self.name = name
        self.user_id = user_id
        self.level = level

    def __eq__(self, other):
        return self.name == other.name and self.user_id == other.user_id
    

class Project:
    """Класс Project, содержащий атрибуты – список пользователей проекта и админ проекта."""

    def __init__(self, admin, users:list) -> None:
        self.admin = admin
        self.users = users

    @classmethod
    def import_json(cls, file_name):
        """
        Метод возвращает экземпляр класса, предварительно считав из файла данные о пользователях.
        """

        with open(file_name, "r", encoding="UTF-8") as file:
            data = json.load(file)

        admin = User("Admin", 1, 1)
        users = [User(val[0], int(key), int(val[1])) for user in data for key, val in user.items()]

        return cls(admin, users)

    def export_json(self, file_name):
        """
        Метод сохраняет в файл список существующих пользователей.
        """

        users = [{user.user_id: (user.name, user.level)} for user in self.users]
        with open(file_name, "w", encoding="UTF-8") as file:
            json.dump(users, file, ensure_ascii=False, indent=2)

    def input_data(self):
        """
        Метод выполняет проверку корректности введеной информации о пользователе.
        """

        while True:
            try:
                user_id = int(input("Введите id: "))
                name = input("Введите имя пользователя: ").title()
                level = input("Введите уровень доступа: ")
                if level != "":
                    level = int(level)
            except Exception as e:
                print(f"Некорректный ввод: {e}")
                continue
            return user_id, name, level

    def enter_user_sistem(self):
        """Метод входа в систему – требует указать имя и id пользователя. Далее метод создает пользователя и проверяет есть ли он в списке пользователей проекта.
        Если в списке его нет, то вызывается исключение доступа. Если пользователь присутствует в списке пользователей проекта, то пользователь, который входит
        получает его уровень доступа и становится администратором."""

        user_id, name, *_ = self.input_data()
        user = list(filter(lambda x: x.user_id == user_id and x.name == name, [i for i in self.users]))

        if len(user) != 0:
            self.admin = user[0]
        else:
            raise AcessError(name)

    def set_user(self):
        """Метод добавление пользователя в список пользователей. Если уровень пользователя меньше, чем уровень админа, вызывайте исключение уровня доступа."""
        user_id, name, level = self.input_data()

        if level < self.admin.level:
            raise LevelError
        
        user = list(filter(lambda x: x.user_id == user_id and x.name == name, [i for i in self.users]))
        if len(user) != 0:
            raise AcessError(name)
        
        self.users.append(User(name, user_id, level))

    def del_user(self):
        user_id, name, *_ = self.input_data()
        user = list(filter(lambda x: x.user_id == user_id and x.name == name, [i for i in self.users]))

        if len(user) != 0:
            self.users.remove(user[0])
            print("Пользователь удален.")
        else:
            raise AcessError(name)

    def __str__(self):
        return f"Администратор: {self.admin.name}. Пользователи: {[user.user_id for user in self.users]}"


test = Project.import_json("test.json")

test.enter_user_sistem()
print(test)

test.set_user()
print(test)

test.del_user()
print(test)