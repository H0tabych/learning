"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
"""

from random import uniform
from verification import isfloat


def main():
    amount_num = 12
    try:
        with open('text_5.txt', 'w+', encoding='utf-8') as f:
            print(*[uniform(-100, 100) for _ in range(amount_num)], file=f)
            f.seek(0)
            if isfloat(*(numbers := f.readline().split())):
                print(f'the sum of the numbers in the file: {sum(list(map(float, numbers)))}')
    except IOError:
        print('An I/O error has occurred')


if __name__ == '__main__':
    main()
