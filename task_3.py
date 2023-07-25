def decorator_csv(function):
    def _wrapper(*args, **kwargs):
        import csv, os

        file_dir = "./"
        file_ext = r".csv"
        files_csv = None
        files_csv = [_ for _ in os.listdir(file_dir) if _.endswith(file_ext)]

        fields = ["number_1", "number_2", "number_3"]

        if not files_csv:
            print("CSV-файл не найден.")
            return 
        
        for file_csv in files_csv:
            with open(file_csv, "r", encoding="UTF-8", newline="") as file:
                numbers = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC)

                for i, row in enumerate(numbers):
                    if i == 0 and row == fields:
                        continue

                    elif i == 0 and row != fields:
                        break

                    arg_a, arg_b, arg_c = row
                    print(function(int(arg_a), int(arg_b), int(arg_c)))
                    
    return _wrapper
