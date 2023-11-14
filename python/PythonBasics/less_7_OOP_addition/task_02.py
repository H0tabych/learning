"""
2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


class Clothes(ABC):

    all_clothes = []

    def __init__(self, size: float) -> None:
        self.size = size
        self.all_clothes.append(self)

    @abstractmethod
    def fabric_consumption(self):
        """
        function for determining the consumption of fabric for 1 unit of clothing
        """
        pass

    @abstractmethod
    def total_consumption_this_clothes(self):
        """
        function for determining the consumption of fabric for all clothes of a given type
        """
        pass

    @property
    def total_consumption(self) -> float:
        """
        function for determining the consumption of fabric for all clothes
        :return: float
        """
        return sum([self.all_clothes[i].fabric_consumption for i in range(len(self.all_clothes))])


class Coat(Clothes):

    this_clothes = []

    def __init__(self, height):
        super().__init__(height)
        self.this_clothes.append(self)

    @property
    def fabric_consumption(self) -> float:
        """
        function for determining the consumption of fabric for 1 unit of coat
        :return: float
        """
        return self.size/6.5 + 0.5

    @property
    def total_consumption_this_clothes(self):
        """
        function for determining the consumption of fabric for all coat
        :return:
        """
        return sum([self.this_clothes[i].fabric_consumption for i in range(len(self.this_clothes))])

    @property
    def height(self):
        return self.size

    @height.setter
    def height(self, height):
        self.size = height


class Costume(Clothes):

    this_clothes = []

    def __init__(self, dimension):
        super().__init__(dimension)
        self.this_clothes.append(self)

    @property
    def fabric_consumption(self) -> float:
        """
        function for determining the consumption of fabric for 1 unit of costume
        :return: float
        """
        return 2 * self.size + 0.3

    @property
    def total_consumption_this_clothes(self):
        """
        function for determining the consumption of fabric for all costume
        :return: float
        """
        return sum([self.this_clothes[i].fabric_consumption for i in range(len(self.this_clothes))])

    @property
    def dimension(self):
        return self.size

    @dimension.setter
    def dimension(self, dimension):
        self.size = dimension


def main():

    coat1 = Coat(50)
    print(coat1.fabric_consumption)

    coat2 = Coat(188)
    print(coat2.fabric_consumption)

    costume = Costume(171)
    print(costume.fabric_consumption)

    print(coat1.total_consumption_this_clothes)
    print(costume.total_consumption_this_clothes)
    print(costume.total_consumption)


if __name__ == '__main__':
    main()
