"""
Задача 1: Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
строковое представление. Функцию hex используйте для проверки своего результата.
"""

SYSTEM: int = 16
result: str = "" 

while True:
    number = input("Введите любое число: ")
    if not number.isdigit():
        print("Попробуйте еще...")
        continue
    break

number = int(number)
if number == 0: result = "0"

check = hex(number)

while number > 0: 
    number, remains = divmod(number, SYSTEM)
    if remains > 10: remains =chr(remains + 55)
    result = str(remains) + result

print(f"Ответ: {result}")
print("Проверка ->",check == "0x" + result.lower())