"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем.
При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class MyError(Exception):
    """
    exception class for divide-by-zero error
    """
    def __init__(self, text='division by zero forbidden'):
        self.text = text


def main():

    dividend, divider = map(float, input('Enter the dividend and divisor separated by a space: ').split())
    if divider == 0:
        raise MyError('division by zero forbidden')
    result = dividend/divider

    print(f'the result of dividing {dividend} by {divider} is: {result}')


if __name__ == '__main__':
    main()
