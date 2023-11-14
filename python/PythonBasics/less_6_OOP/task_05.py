"""
5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Start rendering {self.title}')


class Pen(Stationery):

    def draw(self):
        print(f'pen writes {self.title}')


class Pencil(Stationery):

    def draw(self):
        print(f'pencil drawing {self.title}')


class Handle(Stationery):

    def draw(self):
        print('nobody needs a marker')


def main():
    pen = Pen('zxcvbm')
    pen.draw()

    pencil = Pencil('lkvc')
    pencil.draw()

    handle = Handle('No-no-no')
    handle.draw()


if __name__ == '__main__':
    main()
