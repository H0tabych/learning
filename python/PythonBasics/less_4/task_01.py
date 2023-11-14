"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv
from verification import isfloat


def main():
    if isfloat(*argv[1:]) and False not in set(map(lambda x: float(x) >= 0, argv[1:3])):
        productivity, hourly_rate, bonus = argv[1:]
        salary = float(productivity) * float(hourly_rate) + float(bonus)
        print('Final salary:', salary)
    else:
        print('Invalid arguments were entered')
        print('first argument: productivity - real non-negative number')
        print('second argument: hourly_rate - real non-negative number')
        print('third argument: real number')


if __name__ == '__main__':
    main()
