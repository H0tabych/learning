from prettytable import PrettyTable


class Table:

    def __init__(self, data: dict, head: tuple):
        self.len = len(data.keys())
        self.table = PrettyTable()
        self.table.field_names = head
        self.table.add_rows([[i, *data[i]] for i in data.keys()])
        self.table.align = 'l'
