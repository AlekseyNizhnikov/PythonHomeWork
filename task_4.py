"""
Задача 4: Напишите программу банкомат. Доступные действия: пополнить, снять, выйти.
    Сумма пополнения и снятия кратны 50 у.е.. 
    Процент за снятие 1.5% от суммы снятия, но не менее 30 и не более 60 у.е..
    После каждой 3-й операции начисляется процент 3%.
    Нельзя снять больше чем есть на счете.
    При превышении суммы в 5 млн. вычитать налог на богатство 10% перед каждой операцией,
даже ошибочной. Любое действие выводит счет.
"""

import datetime

MULTIPLE: float = 50.0 # Кратность у.е..

PERCENT_OUTPUT: float = 1.5 # Процент за снятие от суммы снятия.
MIN_LIMIT_OUTPUT: float = 30.0 # Минимальный порог налога.
MAX_LIMIT_OUTPUT: float = 600.0 # Максимальный порог налога.

PERCENT_ACCRUALS: float = 3.0 # Начисление бонуса за каждую 3 операцию.
STEP = 3 # Шаг начисления бонусов.

LIMIT_MONEY: float = 5_000_000.0 # Сумма больше которой берется налог на богатство.
PERCENT_WEALTH: float = 10.0 # Налог на богатство.

wallet: float = 0.0 # Кошелек.


def main(wallet:float=0.0, PERCENT_ACCRUALS:float=0.0, LIMIT_MONEY:float=0.0, PERCENT_WEALTH:float=0.0, STEP:int=1):
    """
    Метод имитирует работу банкомата.

    :item str: Пункт меню, выбираемый пользователем.
    """
    count = 0

    with open("log.txt", "a", encoding="UTF-8") as log_file:
        print(f"Ваш баланс: {wallet} у.е..")

        while True:
            print("1 - Внести\n2 - Снять\n3 - Выйти\n")
    
            item = input("Выберите действие: ")
                
            if item == "1":
                money = inputMoney(MULTIPLE)

                if money:
                    wallet += money
                    print(f"Деньги внесены. Баланс: {wallet}.")
                    log_file.write(f"{datetime.datetime.now()} Внесена сумма: {money}. Баланс: {wallet}.\n")

                else: 
                    log_file.write(f"{datetime.datetime.now()} ОШИБКА! Невозможно выполнить операцию! Баланс: {wallet}.\n")
                    print("ОШИБКА! Невозможно выполнить операцию!\n")
                    continue

                count += 1

            elif item == "2":
                money, difference = outputMoney(wallet, PERCENT_OUTPUT, MIN_LIMIT_OUTPUT, MAX_LIMIT_OUTPUT)

                if money:
                    wallet -= (money + difference)
                    print(f"Выдача наличных {money}. С учетом налога {difference}. Баланс: {wallet}.")
                    log_file.write(f"{datetime.datetime.now()} Выдача наличных: {money}. С учетом налога {difference}. Баланс: {wallet}.\n")

                else: 
                    log_file.write(f"{datetime.datetime.now()} ОШИБКА! Невозможно выполнить операцию! Баланс: {wallet}.\n")
                    print(f"ОШИБКА! Невозможно выполнить операцию! Баланс: {wallet}.\n")
                    continue

                count += 1

            elif item == "3":
                log_file.write(f"{datetime.datetime.now()} Выход из программы. Баланс: {wallet}.\n")
                exit()

            else:
                log_file.write(f"{datetime.datetime.now()} ОШИБКА! Невозможно выполнить операцию! Баланс: {wallet}.\n")
                print("ОШИБКА! Невозможно выполнить операцию!\n")

            # Проверка на возможность начисления бонуса.
            if count == STEP:
                count = 0
                bonus = (wallet / 100.0) * PERCENT_WEALTH
                wallet += bonus
                log_file.write(f"{datetime.datetime.now()} Накопительный процент: {bonus}. Баланс: {wallet}.\n")
                print(f"Накопительный процент: {bonus}. Баланс: {wallet}.\n")
            
            # Проверка на возможное списание налога на богатство.
            if wallet >= LIMIT_MONEY:
                tax = ((wallet - LIMIT_MONEY) / 100.0) * PERCENT_WEALTH
                wallet -= tax
                log_file.write(f"{datetime.datetime.now()} Уплата налога: {tax}. Баланс: {wallet}.\n")
                print(f"Уплата налога: {tax}. Баланс: {wallet}.\n")


def inputMoney(MULTIPLE: float=0.0) -> int|None:
    """
    Метод проверяет корректность введеной суммы на внесение на депозит. Возвращает сумму для вноса.

    :money int: Сумма для внесения на депозит указанная пользователем.
    """

    money = input("Укажите сумму: ")
    if money.isdigit() and int(money) % MULTIPLE == 0:
        return int(money)
        


def outputMoney(wallet:float=0.0, PERCENT_OUTPUT:float=0.0, MIN_LIMIT_OUTPUT:float=0.0, MAX_LIMIT_OUTPUT:float=0.0) -> int|None:
    """
    Метод проверяет корректность введеной суммы, высчитывает налог и возвращает кортеж: сумма для вывода, величина налога.

    :money int: сумма предложенная пользователем для вывода.
    :difference float: сумма налога.
    """
    
    money = input("Укажите сумму: ")

    if money.isdigit() and int(money) % MULTIPLE == 0:
        difference = (int(money) / 100.0) * PERCENT_OUTPUT
        
        if wallet - (int(money) + difference) >= 0:

            if difference < MIN_LIMIT_OUTPUT:
                return int(money), MIN_LIMIT_OUTPUT
            
            elif difference > MAX_LIMIT_OUTPUT:
                return int(money), MAX_LIMIT_OUTPUT        
            
            else:
                return int(money), difference
        else:
            return None, None


if __name__ == "__main__":
    main(wallet, PERCENT_ACCRUALS, LIMIT_MONEY, PERCENT_WEALTH, STEP)