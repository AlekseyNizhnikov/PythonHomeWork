def new_file(name_dir, ext="txt", min_name=6, max_name=30, number=255, max_byte=4096, quantity_file=1):
    import os
    from random import randint

    if not os.path.isdir(name_dir):
        os.mkdir(name_dir)

    while quantity_file > 0:
        file_name = "".join(chr(randint(97, 122)) for _ in range(randint(min_name, max_name)))
        
        with open(f"{name_dir}/{file_name}.{ext}", "wb", buffering=max_byte) as file:
            for _ in range(max_byte):
                file.write(b'\x9b')

        quantity_file -= 1


def generate_ext(dict_ext):
    for key, val in dict_ext.items():
        new_file("folder", ext=key, quantity_file=val)



dict_ext = {"txt": 2, "txx": 3, "xxx": 4}
generate_ext(dict_ext)