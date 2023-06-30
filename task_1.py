"""
Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
Ответьте на вопросы:
1) Какие вещи взяли все три друга
2) Какие вещи уникальны, есть только у одного друга и имя этого друга
3) Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.
"""
friends = { "Денис":("Палатка", "Спички", "Топор"),
            "Егор": ("Палатка", "Удочка","Припасы"),
            "Сергей": ("Палатка", "Спички", "Дождевик"),
            "Олег": ("Палатка", "Спички", "Дрова")}

def all_things(friends_dc: dict):
    friends = []

    for friend in friends_dc.keys():
        friends += friends_dc[friend]
    print(f"Вещи троих друзей: {set(friends)}")
    print()

def unique_things(friends_dc: dict):
    count = 0

    while count < len(friends_dc.keys()):
        friends = list(friends_dc.keys())
        name = friends.pop(count)
        result = set(friends_dc[name])

        for friend in friends:
            result -= set(friends_dc[friend])

        print(f"Уникальные вещи {name}: {result}")
        count += 1
        
    print()

def all_but_one(friends_dc: dict):
    count = 0

    while count < len(friends_dc.keys()):
        friends = list(friends_dc.keys())
        name = friends.pop(count)
        things_name = set(friends_dc[name])
        things_all = set(friends_dc[friends[0]])

        for friend in friends[1:]:
            things_all &= set(friends_dc[friend])
            things_name &= set(friends_dc[friend])

        result = things_all - things_name

        if result:
            print(f"{name} - {result}")
        count += 1

    print()

all_things(friends)
unique_things(friends)
all_but_one(friends)