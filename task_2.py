class Arhive:
    """
    Класс накапливает в переменной result, списки аргументов переданных классу.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.result = []
        else:
            cls._instance.result.append((cls._instance.key, cls._instance.value))
        return cls._instance

    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value

    def __str__(self) -> str:
        return f"Результат: {self.result}"
    
    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.key}, '{self.value}')"


a_1 = Arhive(1, "q")
print(a_1)
a_2 = Arhive(2, "w")
print(a_2)
a_3 = Arhive(3, "e")
print(a_3)
a_4 = repr(a_3)
print(a_4)
print(a_3.__doc__)