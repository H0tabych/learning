"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class Complex:

    def __init__(self, re: float = 0, im: float = 0):
        self.re = re
        self.im = im

    def __str__(self):
        return f'{self.re}' + (f' + i{abs(self.im)}' if self.im >= 0 else f' - i{abs(self.im)}')

    def __add__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            other = Complex(re=other)

        return Complex(self.re + other.re, self.im + other.im)

    def __mul__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            other = Complex(re=other)

        return Complex(self.re * other.re - self.im * other.im,
                       self.re * other.im + self.im * other.re)


def main():
    num1 = Complex(3, -2)
    num2 = Complex(-5, 3)
    print(num1 + num2)
    print(num1 * num2)
    print(num1 + 12)
    print(num2 * -5)
    print(num1 * 0)


if __name__ == '__main__':
    main()
