"""
7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор. Функция вызывается следующим образом: for el in fact(n).
Она отвечает за получение факториала числа. В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""


def factorial(n: int) -> int:
    """
    function to calculate the factorial of a number
    функция вычисления факториала числа
    :param n: the number for which the factorial is calculated
    :return: factorial function generator
    """
    fact = 1
    for i in range(n+1):
        if i == 0:
            yield fact
        else:
            fact *= i
            yield fact


def main():
    num = input('enter the number(positive integer) whose factorial you want to calculate: ')
    n = 0
    if num.isdigit():
        num = int(num)
        for el in factorial(num):
            print(f'{n}! =', el)
            n += 1
    else:
        print('ERROR: the number you entered is not a positive integer.')


if __name__ == '__main__':
    main()
