from abc import ABC


class OfficeEquipment(ABC):

    def __init__(self, manufacturer: str, color: str):

        self.name = type(self).__name__
        self.manufacturer = manufacturer
        self.color = color
        self.price = 1000


class Printer(OfficeEquipment):

    def __init__(self, manufacturer: str = 'HP', color: str = 'Black'):
        super().__init__(manufacturer, color)
        self.price = 2000


class Scanner(OfficeEquipment):

    def __init__(self, manufacturer: str = 'HP', color: str = 'Black'):
        super().__init__(manufacturer, color)
        self.price = 2500


class Xerox(OfficeEquipment):

    def __init__(self, manufacturer: str = 'HP', color: str = 'Black'):
        super().__init__(manufacturer, color)
        self.price = 3000
