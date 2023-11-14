"""
4. Программа принимает действительное положительное число x и целое отрицательное число y.
Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y).
При решении задания нужно обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""


def verification_base(base):
    """
    Cyclic function of checking the value for the possibility of converting types to float,
    as well as checking the positivity of the entered value.
    If the check fails, a new value entry is requested cyclically until the error limit is reached.
    Циклическая функция проверки значения на возможность преобразования типов в float,
    а также проверка положительности введённого значения.
    В случае неудачной проверки циклически запрашивается новый ввод значения
    до достижения предельного количества ошибочных вводов.
    :param base: checked value
    :return: float(base) > 0
    """
    max_err_input = 5
    amount_err_input = 0
    while amount_err_input < max_err_input:
        try:
            float(base)
        except ValueError:
            print('Incorrect data entered, value is not a number')
            print(f'{max_err_input - amount_err_input} attempts left to enter the correct value')
            base = input(f'Enter the base of the degree (real positive number) again: ')
            amount_err_input += 1
        else:
            base = float(base)
            if base <= 0:
                print('Incorrect data entered, value is not a positive number')
                print(f'{max_err_input - amount_err_input} attempts left to enter the correct value')
                base = input(f'Enter the base of the degree (real positive number) again: ')
                amount_err_input += 1
            else:
                return base

    print('Number of invalid value entries exceeded.')
    print('Program completed ahead of schedule.')
    exit(0)


def verification_degree(degree):
    """
    Cyclic function of checking the value for the possibility of type conversion to int,
    as well as checking the negativeness of the entered value.
    If the check fails, a new value entry is requested cyclically until the error limit is reached.
    Циклическая функция проверки значения на возможность преобразования типов в int,
    а также проверка отрицательности введённого значения.
    В случае неудачной проверки циклически запрашивается новый ввод значения
    до достижения предельного количества ошибочных вводов.
    :param degree: checked value
    :return: int(degree) < 0
    """
    max_err_input = 5
    amount_err_input = 0
    while amount_err_input < max_err_input:
        try:
            int(degree)
        except ValueError:
            print('Incorrect data entered, value is not a integer number')
            print(f'{max_err_input - amount_err_input} attempts left to enter the correct value')
            degree = input(f'Enter degree (integer negative number) again: ')
            amount_err_input += 1
        else:
            degree = int(degree)
            if degree >= 0:
                print('Incorrect data entered, value is not a negative number')
                print(f'{max_err_input - amount_err_input} attempts left to enter the correct value')
                degree = input(f'Enter degree (integer negative number) again: ')
                amount_err_input += 1
            else:
                return degree

    print('Number of invalid value entries exceeded.')
    print('Program completed ahead of schedule.')
    exit(0)


def standard_degree(base, degree):
    """
    exponentiation function by standard operator **
    функция возведения в степень стандартным оператором **
    :param base: real positive number
    :param degree: integer negative number
    :return: base ** degree
    """
    return base ** degree


def degree_use_loop(base, degree):
    """
    exponentiation function using a loop
    функция возведения в степень с помощью цикла
    :param base: real positive number
    :param degree: integer negative number
    :return: base exponentiation degree using a loop
    """
    base = 1 / base
    degree = -degree
    result = 1
    for i in range(degree):
        result *= base

    return result


def main():
    """
    Main program function
    Основная функция программы
    :return: None
    """
    base = verification_base(input('Enter the base of the degree (real positive number): '))
    degree = verification_degree(input('Enter degree (integer negative number): '))

    print('exponentiation by the standard operator **: ', standard_degree(base, degree))
    print('exponentiation using a loop: ', degree_use_loop(base, degree))


if __name__ == '__main__':
    main()
