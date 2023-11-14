"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31    32         3    5    32        3    5    8    3
37    43         2    4    6         8    3    7    1
51    86        -1   64   -8
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации
операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    """
    class of mathematical matrices
    """

    def __init__(self, matrix_data: list[list]) -> None:
        self.__matrix = matrix_data
        self.size = self.__matrix_size()

    def __str__(self) -> str:

        return '\n'.join('\t'.join(map(str, self.__matrix[i])) for i in range(self.size[0])) + '\n'

    def __add__(self, other):
        """
        the function of summing two matrices
        :param other: Matrix class object
        :return: Matrix class object
        """
        if not isinstance(other, Matrix):
            raise TypeError(f'Unsupported operand type(s) for +: {type(self)} and {type(other)}')
        elif self.size != other.size:
            raise ValueError(f'Different sizes of matrices: {self.size} and {other.size}')

        sum_matrix = []

        for i in range(self.size[0]):
            sum_matrix.append([sum((self.__matrix[i][j], other.__matrix[i][j])) for j in range(self.size[1])])

        return Matrix(sum_matrix)

    def __matrix_size(self) -> tuple:
        """
        matrix size determination function
        :return: size matrix. tuple(rows, columns)
        """
        rows = len(self.__matrix)
        len_rows = tuple(len(c) for c in self.__matrix)

        if len(set(len_rows)) == 1:
            return rows, max(len_rows)
        else:
            raise ImportError('The input data cannot be converted to a matrix. The lines must be the same length')


def main():
    mtr1 = Matrix([[1, 2, 3],
                   [12, 44, 87],
                   [3, 777, 910],
                   ])
    print(mtr1)
    mtr2 = Matrix([[4, 76, 5],
                   [9, 5, 1],
                  [357, 50, 9],
                   ])
    print(mtr2)

    mtr3 = Matrix([[1, 1, 1],
                   [1, 1, 1],
                   [1, 1, 1],
                   ])
    print(mtr3)

    print(mtr1 + mtr2 + mtr3)


if __name__ == '__main__':
    main()
