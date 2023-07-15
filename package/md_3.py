def read_file(file_1, file_2):
    with open(file_1, "r", encoding="UTF-8") as file_1, open(file_2, "r", encoding="UTF-8") as file_2, open("new_file.txt", "a", encoding="UTF-8") as nf:
        
        count = 0
        mx_count = max(len(file_1.readlines()), len(file_2.readlines()))
        file_1.seek(0), file_2.seek(0)

        while count < mx_count:
            number = 1
            name = file_1.readline()
            numbers = file_2.readline()

            if name == "": file_1.seek(0)
            if numbers == "": file_2.seek(0)

            for i in list(map(float, numbers.split("|"))):
                number *= i

            if number < 0: 
                result = (name[:-1].lower(), abs(number))
            else:
                result = (name[:-1].upper(), int(number))

            print(result, file=nf)
            count += 1




read_file("names.txt", "file.txt")