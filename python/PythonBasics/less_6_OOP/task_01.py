"""
1. Создать класс TrafficLight (светофор).
Определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд,
второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов.
При его нарушении выводить соответствующее сообщение и завершать скрипт.
"""

from time import sleep
from itertools import cycle


class TrafficLight:

    def __init__(self):
        self.__color = {'red': 7, 'yellow': 2, 'green': 5}

    def running(self) -> None:
        """
        traffic light cycle start method
        :return: None
        """
        for i in cycle((*self.__color.keys(), *list(self.__color.keys())[1:-1])):
            print(i)
            sleep(self.__color[i])


def main():
    traffic_light = TrafficLight()
    traffic_light.running()


if __name__ == '__main__':
    main()
