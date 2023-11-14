"""
3. Реализовать базовый класс Worker (работник).
определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
дохода с учётом премии (get_total_income);
проверить работу примера на реальных данных:
создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.
"""


class Worker:

    def __init__(self, name='No name', surname='No surname', position='No position', wage=0):
        self.name = name.capitalize()
        self.surname = surname.capitalize()
        self.position = position.capitalize()
        self.wage = wage
        self.__income = {'wage': self.wage, 'bonus': self.wage * 1.4}


class Position(Worker):

    def get_full_name(self) -> str:
        """
        The method that generates the full name of the worker
        :return: full name. type - string
        """
        return ' '.join((self.name, self.surname))

    def get_total_income(self) -> float:
        """
        The method of calculating the total income of an employee
        :return: total income. type - float
        """
        return sum(self._Worker__income.values())


def main():
    worker1 = Position('Vasya', 'Petrov', 'cleaner', 13500)
    worker2 = Position('Okakiy', 'Monte-Kristo', 'Director', 135000)
    print(f'{worker1.get_full_name()} total income: {worker1.get_total_income()} c.u.')
    print(f'{worker2.get_full_name()} total income: {worker2.get_total_income()} c.u.')


if __name__ == '__main__':
    main()
