import task_3, task_4


@task_3.decorator_csv
@task_4.decorator_json
def solution_of_equation(arg_a:int, arg_b:int, arg_c:int) -> str:
    """
    Метод находит корни квадратного уравнения.

    :arg_a: int аргумент а.
    :arg_b: int аргумент b.
    :arg_c: int аргумент c.
    """

    d = (arg_b**2 - 4 * arg_a * arg_c)**0.5

    if type(d) == complex or d < 0:
        return "Корней нет"
    
    elif d == 0:
        x_1 = (arg_b * (-1)) / (2 * arg_a)
        return f"Один корень: {x_1}"
    
    elif d > 0:
        x_1 = (arg_b*(-1) + d) / (2 * arg_a)
        x_2 = (arg_b*(-1) - d) / (2 * arg_a)
        return f"Два корня: {x_1} и {x_2}"

    
solution_of_equation(1, -4, -5)