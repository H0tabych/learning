from tables import Table


class ConsoleManager:
    def __init__(self, company, store):
        self.company = company
        self.store = store
        self.out = False

    def run(self) -> None:
        """
        The main cycle of the program
        :return: None
        """
        while not self.out:
            self.__main_menu()

    def __main_menu(self) -> None:
        """
        The function that forms the main menu of the program
        :return: None
        """
        print('=' * 100)
        head_main_menu = ('No', '')
        main_menu = {1: ['List of equipment on balance'],
                     2: ['Move equipment'],
                     3: ['Buy equipment'],
                     4: ['Exit']
                     }
        main_menu_vs_functions = {1: self.__all_equipment_on_balance,
                                  2: self.__move_equipment,
                                  3: self.__price_list,
                                  4: self.__exit,
                                  }
        table_main_menu = Table(main_menu, head_main_menu)
        print(f'OOO "{self.company.name}"\n'
              f'Money on balance: {self.company.money}')
        print(table_main_menu.table)
        n = input('Enter menu item number: ')
        if self.__validation_input(n, tuple(main_menu.keys())[0], tuple(main_menu.keys())[-1]):
            n = int(n)
        else:
            return
        main_menu_vs_functions[n]()

    def __price_list(self) -> None:
        """
        Equipment purchase menu function
        :return: None
        """
        print('=' * 100)
        print(f'Welcome to the "{self.store.name}" store')
        print('Price list:')
        price_dict = self.store.storage.storage_dict()
        head = ('No', 'Name', 'Manufacturer', 'Color', 'Unit price', 'Count')
        print(Table(price_dict, head).table)
        print(f'Your money: {self.company.money}')
        num = input('Enter the item number to purchase: ')
        if self.__validation_input(num, tuple(price_dict.keys())[0], tuple(price_dict.keys())[-1]):
            num = int(num)
        else:
            return
        count = input('Enter the quantity of the item you want to buy: ')
        if self.__validation_input(count, 0, int(tuple(price_dict[num])[-1])):
            count = int(count)
        else:
            return
        if not self.__validation_count(price_dict[num][-1], count):
            return

        self.company.buy_equipment(self.store, *price_dict[num][:-2], count)

    def __all_equipment_on_balance(self) -> None:
        """
        The function of displaying all equipment on the balance sheet of the company
        :return: None
        """
        head = ('No', 'Name', 'Manufacturer', 'Color', 'Unit price', 'Count')

        print('=' * 100)
        print(f'Equipment on the balance sheet of {self.company.name}:')
        for i in self.company.departments.keys():
            print(self.company.departments[i].name + ':')
            table_equipment = Table(self.company.departments[i].storage_dict(), head)
            print(table_equipment.table)

        input('Press any key to return to the menu: ')

    def __equipment_on_balance_in_department(self, num_department: int) -> dict:
        """
        The function of displaying equipment on the balance sheet of the selected department of the company
        :param num_department: department number
        :return: Dictionary of objects on the balance sheet of the department
        """
        head = ('No', 'Name', 'Manufacturer', 'Color', 'Unit price', 'Count')

        print('=' * 100)
        print(f'Equipment on the balance of {self.company.departments[num_department].name}:')
        equipment = self.company.departments[num_department].storage_dict()
        table_equipment = Table(self.company.departments[num_department].storage_dict(), head)
        print(table_equipment.table)
        return equipment

    def __move_equipment(self) -> None:
        """
        The function of transferring equipment from one department of the company to another
        :return: None
        """
        head = ('No', 'Department', 'Capacity')
        departments = {i: [n.name, n.capacity] for i, n in self.company.departments.items()}
        table_departments = Table(departments, head)
        print('=' * 100)
        print(table_departments.table)

        department_out = input('Enter the number of the department from which you want to move the equipment: ')
        if self.__validation_input(department_out, tuple(departments.keys())[0], tuple(departments.keys())[-1]):
            department_out = int(department_out)
        else:
            return

        equipment = self.__equipment_on_balance_in_department(department_out)
        num = input('Enter the number of the equipment you want to move: ')
        if self.__validation_input(num, tuple(equipment.keys())[0], tuple(equipment.keys())[-1]):
            num = int(num)
        else:
            return

        count = input('Enter the amount of equipment you want to move: ')
        if self.__validation_input(count, 0, int(tuple(equipment[num])[-1])):
            count = int(count)
        else:
            return

        departments = {i: j for i, j in departments.items() if i != department_out}
        table_departments = Table(departments, head)
        print(table_departments.table)
        department_in = input('Enter the number of the department to which you want to move the equipment: ')
        if self.__validation_input(department_in, tuple(departments.keys())[0], tuple(departments.keys())[-1]):
            department_in = int(department_in)
        else:
            return

        self.company.move_equipment(department_out, num, count, department_in)

    def __exit(self):
        self.out = True

    @staticmethod
    def __validation_input(n: str, min_num: int, num_max: int) -> bool:
        """
        Validation of the value entered by the user
        :param n: input number
        :param min_num: minimum number
        :param num_max: maximum number
        :return: Bool
        """
        if n.isdigit() and min_num <= int(n) <= num_max:
            return True
        else:
            print('ERROR: Invalid number entered')
            return False

    @staticmethod
    def __validation_count(sell_count_object: int, count: int) -> bool:
        """
        Checking the amount of equipment
        :param sell_count_object: quantity in stock
        :param count: input count
        :return: bool
        """
        if sell_count_object - count < 0:
            print("ERROR: The store doesn't have that much equipment.")
            return False
        else:
            return True


def main():
    pass


if __name__ == '__main__':
    main()
