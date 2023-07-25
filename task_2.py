def generator_rnd_numbers(file_name):
    """
    Метод формирует csv-файл списков трех случайных чисел.

    :quantity: int случайное число наборов чисел.
    :fields: list[str] заголовок csv-файла.    
    """
    
    import random, csv

    with open(f"{file_name}.csv", "w", encoding="UTF-8", newline="") as file:
        quantity = random.randint(100, 999)
        fields = ["number_1", "number_2", "number_3"]

        writer_number = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
        writer_number.writerow(fields)

        for _ in range(quantity):
            result = [random.randint(-10, 10) for _ in range(3)]
            if result[0] == 0:
                result[0] = 1
            writer_number.writerow(result)


generator_rnd_numbers("csv_file")