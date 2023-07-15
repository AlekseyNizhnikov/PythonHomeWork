def generate_names():
    from random import randint as rnd

    result = ""
    len_name = rnd(4, 7)
    glas = "aeiouy"

    with open("names.txt", "a", encoding="UTF-8") as file:
        for _ in range(len_name):
            result += chr(rnd(97, 122))
        print(result.replace(result[rnd(0, len(result)-1)], glas[rnd(0, len(glas)-1)]).capitalize(), file=file)


generate_names()