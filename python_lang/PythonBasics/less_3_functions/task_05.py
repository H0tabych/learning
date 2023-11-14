"""
5. Программа запрашивает у пользователя строку чисел, разделённых пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
разделённых пробелом и снова нажать Enter. Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введён после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""


def verification(list_numbers, pos_exit):
    """
    A cyclic function to check if a values can be converted to float.
    If the check fails, a new value entry is requested cyclically until the error limit is reached.
    Циклическая функция проверки значений на возможность преобразования типов в float.
    В случае неудачной проверки циклически запрашивается новый ввод значения
    до достижения предельного количества ошибочных вводов.
    :param list_numbers: checked values
    :param pos_exit: the position of the exit marker
    :return: list of elements converted to floating point numbers
    """
    max_err_input = 5
    amount_err_input = 0
    list_numbers = list(list_numbers.split())
    while amount_err_input < max_err_input:
        try:
            return list(map(lambda x: float(x),
                            list_numbers if pos_exit == -1 else list_numbers[:pos_exit]))
        except ValueError:
            print('One of the entered values is neither a number nor an escape character')
            print(f'{max_err_input - amount_err_input} attempts left to enter the correct value')
            list_numbers = input('Enter a string of numbers separated by spaces. Enter "Q" to exit: ')
            amount_err_input += 1

    print('Number of invalid value entries exceeded.')
    print('Program completed ahead of schedule.')
    exit(0)


def sum_numbers(numbers):
    """
    summation function of entered values
    функция суммирования введённых значений
    :param numbers: string of entered values
    :return: sum of elements (sum_num) and exit marker (usr_exit)
    """
    usr_exit = False
    if (pos_Q := numbers.upper().find('Q')) != -1:
        usr_exit = True

    numbers = verification(numbers, pos_Q)
    sum_num = sum(numbers)
    print(f'Sum of current entered values: {sum_num}')

    return sum_num, usr_exit


def main():
    """
    Main program function
    Основная функция программы
    :return: None
    """
    sum_all_num = 0
    usr_exit = False
    while not usr_exit:
        numbers = input('Enter a string of numbers separated by spaces. Enter "Q" to exit: ')
        sum_num, usr_exit = sum_numbers(numbers)
        sum_all_num += sum_num
        print(f'Sum of all entered values: {sum_all_num}')


if __name__ == '__main__':
    main()
