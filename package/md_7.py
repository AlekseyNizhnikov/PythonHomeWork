def new_file(name_dir=None, ext="txt", min_name=6, max_name=30, number=255, max_byte=4096, quantity_file=1):
    import os
    from random import randint


    while quantity_file > 0:
        file_name = "".join(chr(randint(97, 122)) for _ in range(randint(min_name, max_name)))
        if name_dir != None:
            if not os.path.isdir(name_dir):
                os.mkdir(name_dir)
            path = f"{name_dir}/{file_name}.{ext}"
        else:
            path = f"{file_name}.{ext}"
            
        with open(path, "wb", buffering=max_byte) as file:
            for _ in range(max_byte):
                file.write(b'\x9b')

        quantity_file -= 1


def generate_ext(dict_ext):
    video = ["mp4", "avi", "mpeg"]
    images = ["jpg", "gif", "bmp"]
    text = ["txt", "doc", "docx"]

    for key, val in dict_ext.items():
        if key in video:
            new_file("video", ext=key, quantity_file=val)
        elif key in images:
            new_file("images", ext=key, quantity_file=val)
        elif key in text:
            new_file("text", ext=key, quantity_file=val)
        else:
            new_file(ext=key, quantity_file=val)



dict_ext = {"txt": 2, "jpg": 3, "mp4": 4}
generate_ext(dict_ext)