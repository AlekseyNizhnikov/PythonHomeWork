"""
4. Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно
вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.
"""

BACKPACK = 45

hike = {"Палатка": 10,
        "Припасы": 9,
        "Вода": 8,
        "Спирт": 7,
        "Карта": 6,
        "Одежда": 5,
        "Оружие": 4,
        "Аптечка": 3,
        "Телефон": 2,
        "Спички": 1}

thingths = list(hike.keys())
count = 0

while count < len(thingths):
    wt = 0
    result = {}

    while thingths and wt <= BACKPACK:
        thingth = thingths.pop(0)
        weight = hike[thingth]
        wt += weight
        result[thingth] = weight

    if not thingths and wt <= BACKPACK:
        print(f"Вариант 1: {result}")
        break

    thingths = list(hike.keys())
    thingths.append(thingths.pop(count))
    count += 1

    print(f"Вариант {count:<2}: {result}")

