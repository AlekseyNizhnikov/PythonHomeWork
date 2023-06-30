"""
В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии
или из документации к языку.
"""

with open("waw.txt", encoding="UTF-8") as file:
    text_read = " "
    result = dict()
    exceptions_chars = (".", ",", "!", "?", "-", "—", '"', "'", "(", ")", "[", "]")

    while text_read:
        text_read = file.readline()

        for word in text_read.split():
            word = word.lower()

            if word in exceptions_chars: 
                continue
            elif word[-1] in exceptions_chars:
                word.removeprefix(word[-1])

            result[word] = result.get(word, 0) + 1

sort_result = sorted(result.items(), key=lambda x: x[1], reverse=True)

for i in range(10):
    print(f"{sort_result[i][0]}: {sort_result[i][1]}", end=" | ")
print()