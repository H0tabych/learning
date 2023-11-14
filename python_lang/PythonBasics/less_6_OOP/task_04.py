"""
4. Реализуйте базовый класс Car.
У класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.
"""
from random import choices
from numpy.random import poisson


class Car:

    def __init__(self, speed=40, color='black', name='No name'):
        self.police_car = None
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False
        self._allowed_speed = 80
        self._wanted = False

    def show_speed(self):
        """
        method shows the speed of the car. if the speed limit is exceeded, call the police
        :return: None
        """
        print(f'current vehicle speed {self.speed} km/h')
        if self.speed > self._allowed_speed:
            if self._wanted is False:
                self._wanted = True
                self.police_car = PoliceCar(name='Ford')
                print(f'Attention! The speed of the {self.color} {self.name} '
                      f'exceeds the permitted speed({self._allowed_speed} km/h). wanted car')
            else:
                print(f'Attention! The speed of the car is higher than allowed({self._allowed_speed} km/h).')

    def go(self, distance):
        """
        the method starts a trip for a given distance
        :param distance: float
        :return: None
        """
        print(f'{self.color} {self.name} car started moving at a speed of {self.speed} km/h')
        print('-' * 50)

        for x in range(0, distance, 10):
            self.turn()
            if self._wanted is True:
                self.police_car.pursuit(self.speed)
            print('-' * 50)
        self.stop()
        print('=' * 100)

    def stop(self):
        """
        method stops the car
        :return: None
        """
        self.speed = 0

        print(f'{self.color} {self.name} car stopped')
        self.show_speed()

    def turn(self):
        """
        method determines the direction of movement and speed
        :return: None
        """
        moves = {'forward': 10, 'right': 3, 'left': 3, 'back': 1}
        move = choices(tuple(moves.keys()), weights=tuple(moves.values()), k=1)[0]
        self.speed = int(poisson(self.speed, 1))

        print(f'{self.color} {self.name} moving to the {move}')
        self.show_speed()


class TownCar(Car):

    def __init__(self, speed=40, color='black', name='No name'):
        super().__init__(speed, color, name)
        self._allowed_speed = 60


class SportCar(Car):
    pass


class WorkCar(Car):
    def __init__(self, speed=40, color='black', name='No name'):
        super().__init__(speed, color, name)
        self._allowed_speed = 40


class PoliceCar(Car):

    def __init__(self, speed=40, color='black', name='No name'):
        super().__init__(speed, color, name)
        self.is_police = True
        del self._allowed_speed

    def show_speed(self):
        print(f'The current speed of the police car {self.speed} km/h')

    def pursuit(self, speed_pursued_car):
        moves = {'forward': 10, 'right': 3, 'left': 3, 'back': 1}

        move = choices(tuple(moves.keys()), weights=tuple(moves.values()), k=1)[0]
        self.speed = int(poisson(speed_pursued_car * 1.5, 1))

        print(f'{self.color} police car {self.name} pursues and moving to the {move} at a speed of {self.speed} km/h')


def main():
    town_car = TownCar(speed=55, name='Audi', color='black')
    town_car.go(distance=100)

    work_car = WorkCar(speed=40, name='Lada', color='white')
    work_car.go(distance=100)

    sport_car = SportCar(speed=120, name='Lamborghini', color='orange')
    sport_car.go(500)

    police_car = PoliceCar(speed=40, name='UAZ', color='blue-white')
    police_car.go(300)


if __name__ == '__main__':
    main()
