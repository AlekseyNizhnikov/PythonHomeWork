def random_numbers(file_name, rows):
    from random import randint, uniform

    with open(file_name, "a", encoding="UTF-8") as file:
        for _ in range(rows):
            print(f"{randint(-1000, 1000)}|{uniform(-1000.0, 1000.0)}", file=file)


random_numbers("file.txt", 10)