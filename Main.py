"""
Задание 1: Вывести в консоль таблицу умножения от 2 до 9, как на обратной стороне тетрадного листа.
"""
START = 2
STOP = 10
start = START
stop = STOP//2 + 1
LIM_CHAR = 2
ROW = 2
count = 0

print("Таблица умножения:")
while count < ROW:
    for i in range(START, STOP):
        for j in range(start, stop):
            result = str(i * j).ljust(LIM_CHAR, " ")
            print(f"{j} * {i} = {result} ", end=" ")
        print()
    start = stop
    stop = STOP
    count += 1
    print()

"""Задание 2: Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны
с суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то
треугольника с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним,
равнобедренным или равносторонним."""

SIDE = 3

while True:
    try:
        ls_side = list(map(int, input("Введите размер сторон через пробел: ").strip().split(" ")))
    except ValueError as e:
        print(f"Некорректный ввод. {e}")
        continue
    break

ls_side = sorted(ls_side)
sum_side = sum(ls_side)

for i in range(SIDE):
    if (sum_side - ls_side[i]) < ls_side[i]: 
        print("Треугольник не существует.")
        break
else:
    if ls_side[0] == max(ls_side):
        print("Треугольник равносторонний.")

    elif ls_side[len(ls_side) // 2] == max(ls_side) or ls_side[len(ls_side) // 2] == ls_side[0]:
        print("Треугольник равнобедренный.")

    else:
        print("Треугольник разносторонний.")

"""
Задание 3: Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и
на себя”. Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
"""
while True:
    try:
        number = int(input("Введите число от 1 до 100 000: "))
    except ValueError as e:
        print(f"Некорректный ввод: {e}")
        continue
    if number < 0:
        print("Попробуйте еще...")
        continue
    elif 1 >= number or number > 100000:
        print("Попробуйте еще...")
        continue
    break

for i in range(3, number, 2):
    if number % i == 0: 
        print(f"{number} - составное число.")
        break
else:
    print(f"{number} - простое число.")

"""
Задание 5: . Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
Программа должна подсказывать «больше» или «меньше» после каждой попытки.
"""
from random import randint

LIM_MAX = 1000
LIM_MIN = 0
trial = 10

_number = randint(LIM_MIN, LIM_MAX)

while trial > 0:
    try:
        user_number = int(input(f"Угадайте число, от  0 до 1000  и выграйте ДВА ПОЛУЦАРСТВА! Осталось {trial} попыток.\nИтаааак, ваше число: "))  
    except ValueError as e:
        print(f"Попробуйте еще... {e}")
        continue

    
    if user_number == _number:
        print("Да ты везунчик! Этот парень не так прост!")
        break
    elif user_number > _number:
        print("Попробуйте взять на децел меньше...")
    elif user_number < _number:
        print("Попробуйте взять на децел больше...")
    trial -= 1
else:
    print("Увы! ВЫ проиграли!... Ребята, снимите-ка с него шкуру.")