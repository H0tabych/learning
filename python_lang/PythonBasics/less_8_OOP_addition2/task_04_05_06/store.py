from office_equipment import Printer, Scanner, Xerox
from department import Department


class Store:
    def __init__(self, name):
        self.name = name
        self.money = 500_000
        self.margin = 0.5
        self.storage = Department('Store storage')
        self.type_equipment = (Printer, Scanner, Xerox)
        self.names_equipment = [equipment.__name__ for equipment in self.type_equipment]
        self.colors_equipment = ['Black', 'White']
        self.manufacturers = ['Cannon', 'HP']
        if not self.storage.equipment:
            self.__buy_all_in()

    def __buy_all_in(self):
        # if the store's warehouse is empty, then the store buys equipment with all the money
        amount = int(self.money / sum([c().price for c in self.type_equipment]) /
                     (len(self.colors_equipment) * len(self.manufacturers)))

        for name in self.names_equipment:
            self.storage.equipment[name] = []
            for color in self.colors_equipment:
                for manufacturer in self.manufacturers:
                    self.__buy_equipment(name, color, manufacturer, amount)

    def __buy_equipment(self, name, color, manufacturer, count):
        equipment = [c for c in self.type_equipment if c.__name__ == name]
        for n in range(count):
            self.storage.equipment[name].append(equipment[0](manufacturer, color))
            self.money -= self.storage.equipment[name][-1].price
            self.storage.equipment[name][-1].price *= (1 + self.margin)

    def sell_equipment(self, name, manufacturer, color, count):
        sell = []
        equipments = list(filter(lambda c: c.manufacturer == manufacturer and c.color == color,
                                 self.storage.equipment[name]))
        for i in equipments[:count]:
            sell.append(self.storage.equipment[name].pop(self.storage.equipment[name].index(i)))
            self.money += sell[-1].price

        self.__buy_equipment(name, color, manufacturer, int(count))

        return sell


def main():
    s = Store('Рога и копыта')


if __name__ == '__main__':
    main()
