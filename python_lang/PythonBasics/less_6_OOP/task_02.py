"""
2. Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом,
толщиной в 1 см*число см толщины полотна;
проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т.
"""


class Road:

    def __init__(self, length: float, width: float):
        self.__length = length
        self.__width = width
        self.__mass_sq_meters = 25000
        self.__depth = 5

    def mass_road(self) -> float:
        """
        method for calculating the mass of the road
        :return: mass road. type - float
        """
        mass = self.__length * self.__width * self.__mass_sq_meters * self.__depth
        return mass


def main():
    road = Road(5000, 20)
    print(f'Mass of road: {road.mass_road() / 10**6} tons')


if __name__ == '__main__':
    main()
