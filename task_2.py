"""
Задача 2: Возьмите 1-3 любые задачи из прошлых семинаров, которые вы уже решали. Превратите функции в методы класса.
Задачи должны решаться через вызов методов экземпляра.
"""

from typing import Any


class Decorator():
    def __init__(self, function) -> None:
        self.function = function

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        self.function()

