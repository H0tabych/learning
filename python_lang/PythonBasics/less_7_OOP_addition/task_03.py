"""
3. Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
умножение и целочисленное (с округлением до целого) деление клеток, соответственно.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если
разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как
произведение количества ячеек этих двух клеток.
Деление. Создаётся общая клетка из двух.
Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернёт строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернёт строку: *****\n*****\n*****.
"""


class Cell:
    def __init__(self, count):
        if str(count).isdigit() and int(count) > 0:
            self.count = count
        else:
            raise ValueError('the number of cells(count) must be a natural number')

    def __add__(self, other):
        return Cell(self.count + other.count)

    def __sub__(self, other):
        if self.count > other.count:
            return Cell(self.count - other.count)
        else:
            return f'difference cannot be negative or zero'

    def __mul__(self, other):
        return Cell(self.count * other.count)

    def __truediv__(self, other):
        if self.count / other.count >= 1:
            return Cell(self.count // other.count)
        else:
            return f'the resulting cell has no cells'

    def make_order(self, per_row: int) -> str:
        rows, tail = self.count // per_row, self.count % per_row
        return '\n'.join(['*' * per_row] * rows + (['*' * tail] if tail else []))

    def __str__(self) -> str:
        return str(self.count)


def main():
    cell1 = Cell(8)
    print(cell1)
    cell2 = Cell(10)
    print(cell2)

    print(cell1 + cell2)
    print(cell1 - cell2)
    print(cell2 - cell1)
    print(cell2 - cell2)
    print(cell1 * cell2)
    print(cell1 / cell2)
    print((cell1 * cell2).make_order(7))


if __name__ == '__main__':
    main()
