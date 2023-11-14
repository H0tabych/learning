"""
Data Validation Function Module
Модуль функций для проверки данных
"""


def isfloat(*args) -> bool:
    """
    function of checking for the possibility of converting input data elements into real numbers
    функция проверки на возможность преобразования в вещесвенные числа элементов входных данных
    :param args: input arguments (int)
    :return: bool
    """
    for x in args:
        try:
            float(x)
        except ValueError:
            print(f'WARNING: {x}, is not a real number')
            return False
    return True
