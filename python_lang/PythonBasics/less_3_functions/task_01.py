"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def verification(num):
    """
    A cyclic function to check if a value can be converted to float.
    In case of an unsuccessful check, a cyclic request for a new input of a value.
    Циклическая функция проверки значения на возможность преобразования типов в float.
    В случае неудачной проверки циклический запрос нового ввода значения.
    :param num: checked value
    :return: float(num)
    """
    max_err_input = 5
    amount_err_input = 0
    while amount_err_input < max_err_input:
        try:
            return float(num)
        except ValueError:
            print('Incorrect data entered, value is not a number')
            num = input('Enter the number again: ')
            amount_err_input += 1
    print('Number of invalid value entries exceeded.')
    print('Program completed ahead of schedule.')
    exit(0)


def divide(divisible, divisor):
    """
    Function for dividing two numbers (divisible/divisor)
    Функция осуществляющая деление двух чисел (divisible/divisor)
    :param divisible: type(Float)
    :param divisor: type(Float) and not NULL
    :return: None
    """
    try:
        quotient = divisible/divisor
        print('quotient:', quotient)
    except ZeroDivisionError:
        print('Division by zero is not allowed')
        print('program completed ahead of schedule.')


def main():
    """
    Main program function
    Основная функция программы
    """

    num_1 = input('Enter a divisible number: ')
    num_1 = verification(num_1)
    num_2 = input('Please enter a divisor: ')
    num_2 = verification(num_2)

    divide(num_1, num_2)


if __name__ == '__main__':
    main()
