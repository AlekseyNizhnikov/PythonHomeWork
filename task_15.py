"""
Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
Соберите информацию о содержимом в виде объектов namedtuple.
Каждый объект хранит:
* имя файла без расширения или название каталога,
* расширение, если это файл,
* флаг каталога,
* название родительского каталога.
В процессе сбора сохраните данные в текстовый файл используя логирование.
"""

from collections import namedtuple
import os, logging, argparse


FORMAT = "{levelname: <8} - {asctime}, {msg}"
logging.basicConfig(filename="loging.log", level=logging.INFO, encoding="UTF-8",
                    format=FORMAT, style="{")
log_info = logging.getLogger(__name__)


def logger(function):
    """
    Декоратор. Сохраняет в журнал имя функции и переданные ей аргументы.
    """

    def _wrapper(*args, **kwargs):
        log_info.info(f"Функция: {function.__name__} с атрибутами {args, kwargs}. Результат: {function(*args)}")
    return _wrapper


def parser_folders(path):
    """
    Метод рекурсивно проходит по всем объектам директории, добавляя в результирующий спискок объекты именованного кортежа.
    Возвращает список объектов с именем папки/файла, расширением и именем корневой папки.
    """

    result = []
           
    for root, dirs, files in os.walk(path):
        for dir, file in zip(dirs, files):
            result.append(named_tuple(dir, "dir", root.split('/')[-1]))
            name, ext, *_ = f"{file}.None".split(".")          
            result.append(named_tuple(name, ext[0], root.split('/')[-1]))

    return result


@logger
def named_tuple(name, ext, root):
    """
    Метод возвращает объект именованного кортежа.
    """

    Path = namedtuple("Path", ["name", "ext", "root"])
    return Path(name, ext[0], root.split('/')[-1])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path", metavar="N", type=str, help="Укажите путь к директории.")
    args = parser.parse_args()
    parser_folders(args.path)
