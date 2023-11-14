class Department:
    def __init__(self, name, capacity=500):
        self.name = name
        self.capacity = capacity
        self.equipment = {}

    def storage_dict(self) -> dict:
        """
        Dictionary for forming the equipment table
        :return: dict
        """
        storage_tmp = {}
        storage = {}
        n = 1
        for list_object in self.equipment.values():
            for o in list_object:
                s = f'{o.name}_{o.manufacturer}_{o.color}_{o.price}'
                if s not in storage_tmp.values():
                    storage_tmp[n] = s
                    storage[n] = [*s.split('_'), 1]
                    n += 1
                else:
                    storage[list(storage_tmp.values()).index(s)+1][-1] += 1
        return storage

    def validation_capacity(self, count) -> bool:
        """
        Checking if there is enough free space in the storage
        :param count: quantity to be placed in storage
        :return: bool
        """
        if self.capacity - count >= 0:
            return True
        else:
            print('ERROR: Not enough storage space')
            return False


def main():
    pass


if __name__ == '__main__':
    main()
