"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и
возвращает сумму наибольших двух аргументов.
"""


def verification(value, num):
    """
    A cyclic function to check if a value can be converted to float.
    In case of an unsuccessful check, a cyclic request for a new input of a value.
    Циклическая функция проверки значения на возможность преобразования типов в float.
    В случае неудачной проверки циклический запрос нового ввода значения.
    :param value: checked value
    :param num: value number
    :return: float(value)
    """
    max_err_input = 5
    amount_err_input = 0
    while amount_err_input < max_err_input:
        try:
            return float(value)
        except ValueError:
            print('Incorrect data entered, value is not a number')
            print(f'{max_err_input - amount_err_input} attempts left to enter the correct value')
            value = input(f'{num} - Enter the number again: ')
            amount_err_input += 1

    print('Number of invalid value entries exceeded.')
    print('Program completed ahead of schedule.')
    exit(0)


def my_func(*args):
    """
    The function calculates the sum of the largest two arguments
    Функция вычисляет сумму наибольших двух аргументов
    :param args: tuple of real arguments
    :return: sum of largest two arguments
    """
    return sum((sorted(args, reverse=True)[:2]))


def main():
    """
    Main program function
    Основная функция программы
    :return: None
    """
    amount = 3
    print(f'Please, enter {amount} numbers')
    numbers = [verification(input(f'{n+1} - Input number: '), n+1) for n in range(amount)]
    print(f'sum of the largest two values: {my_func(*numbers)}')


if __name__ == '__main__':
    main()
