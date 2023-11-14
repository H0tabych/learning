from department import Department


class Company:
    def __init__(self, name):
        self.name = name
        self.money = 500_000
        self.departments = {1: Department('Storage department'),
                            2: Department('Technical department', 20),
                            3: Department('Sales department', 20),
                            }

    def buy_equipment(self, store: object, name: str, manufacturer: str, color: str, count: int) -> None:
        """
        The function of buying equipment in the store
        :param store: object store
        :param name: name equipment
        :param manufacturer: manufacturer equipment
        :param color: color equipment
        :param count: count equipment
        :return: None
        """
        if not self.departments[1].validation_capacity(count):
            return
        self.departments[1].capacity -= count
        equipment = store.sell_equipment(name, manufacturer, color, count)
        if not self.__validation_money(equipment[0].price * count):
            print("ERROR: You don't have enough money to buy")
            return

        self.money -= sum(x.price for x in equipment)
        if not self.departments[1].equipment.get(name):
            self.departments[1].equipment[name] = []
        self.departments[1].equipment[name].extend(equipment)

    def move_equipment(self, department_out: int, what: int, count: int, department_in: int) -> None:
        """
        function of transferring equipment from one department to another
        :param department_out: department from which we pick up equipment
        :param what: equipment
        :param count: count equipment
        :param department_in: department to which we give the equipment
        :return: None
        """
        if not self.departments[department_in].validation_capacity(count):
            return
        self.departments[department_in].capacity -= count
        self.departments[department_out].capacity += count

        param_equipment = self.departments[department_out].storage_dict()[what]
        equipments = list(filter(lambda c: c.manufacturer == param_equipment[1] and c.color == param_equipment[2],
                                 self.departments[department_out].equipment[(name := param_equipment[0])]))
        for i in equipments[:count]:
            if i.manufacturer == param_equipment[1] and i.color == param_equipment[2]:
                if not self.departments[department_in].equipment.get(name):
                    self.departments[department_in].equipment[name] = []
                self.departments[department_in].equipment[name].append(
                    self.departments[department_out].equipment[name].pop(
                        self.departments[department_out].equipment[name].index(i)))

    def __validation_money(self, price: float) -> bool:
        """
        check if you have enough money to buy
        :param price: cost of purchased equipment
        :return: bool
        """
        if self.money - price >= 0:
            return True
        else:
            return False


def main():
    pass


if __name__ == '__main__':
    main()
