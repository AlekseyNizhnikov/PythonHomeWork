import os


def group_rename_file(new_name:list[str], old_exps:list[str], new_exps:list[str]):
    """
    Метод принимает на вход три списка: новые имена файлов, старые расширения и новые расширения.
    Затем переименовываеет файлы, добавляя им старое имя и порядковый номер.

    :file_names: list[str] список файлов каталога, у которых совпало расширение с old_exp.
    :new_name:list[str] список новых имен файлов.
    :old_exps:list[str] список старых расширений файлов.
    :new_exps:list[str] список новых расширений файлов.
    """

    import os
    
    files_names = list(filter(lambda x: any(x.endswith(f".{i}") for i in old_exps), os.listdir()))

    for old_name, exp, name, i in zip(files_names, new_exps, new_name, range(len(new_name))):
        os.rename(old_name,f"{old_name.split('.')[0]}_{name}_{i}.{exp}" )


new_names = ["new_name_1", "new_name_2", "new_name_3"]
old_exps = ["txt", "png", "css"]
new_exps = ["doc", "jpg", "mp4"]

group_rename_file(new_names, old_exps, new_exps)