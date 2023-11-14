"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
Он должен извлекать число, месяц, год и преобразовывать их тип к типу «число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Date:

    def __init__(self, day: int, month: int, year: int):

        self.valid(day, month, year)
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def split_and_convert(cls, date: str) -> object:
        """
        a function that divides the date into components and converts to a natural number type
        :param: format string "day-month-year"
        :return: object of class Data
        """
        date = [int(i) for i in date.split(sep='-')]
        return cls(*date)

    @staticmethod
    def valid(day: int, month: int, year: int) -> True:
        """
        function that validates the day, month and year
        :return:
        """
        day_in_month = {m+1: 31 if m % 2 == 0 else 30 for m in range(7) if m+1 != 2}
        day_in_month.update({m: 31 if m % 2 == 0 else 30 for m in range(8, 13)})
        day_in_month[2] = 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
        try:
            if not 0 < day <= day_in_month[month]:
                raise ValueError(f'ERROR: the day number was entered incorrectly. '
                      f'Month {month} has {day_in_month[month]} days, not {day}')
        except KeyError:
            raise ValueError(f'ERROR: month number entered incorrectly. month number {month} does not exist.')

        return True


def main():
    date = Date.split_and_convert('08-06-2022')
    print(f'day: {date.day}')
    print(f'month: {date.month}')
    print(f'year: {date.year}')


if __name__ == '__main__':
    main()
