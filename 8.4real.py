class Sklad:
    def __init__(self):
        self._dict = {}

    def add_to(self, equipment):
        self._dict.setdefault(equipment.name, []).append(equipment)

    def extract(self, name):
        if self._dict[name]:
            self._dict.setdefault(name).pop(0)


class Equipment:
    def __init__(self, name, make, year):
        self.name = name
        self.make = make
        self.year = year

    def __repr__(self):
        return f'{self.name}-{self.make}-{self.year}'


class Printer(Equipment):
    def __init__(self, series, name, make, year):
        super().__init__(name, make, year)
        self.series = series

    def action(self):
        return 'Печатает'


class Scaner(Equipment):
    def __init__(self, name, make, year):
        super().__init__(name, make, year)

    def action(self):
        return 'Сканирует'


class Xerox(Equipment):
    def __init__(self, name, make, year):
        super().__init__(name, make, year)

    def action(self):
        return 'Копирует'


sklad = Sklad()

scaner = Scaner('hp', '120', 78)
sklad.add_to(scaner)
scaner = Scaner('hp', '23MAX', 65)
sklad.add_to(scaner)
scaner = Scaner('hp', '30', 94)
sklad.add_to(scaner)
print(sklad._dict)
sklad.extract('hp')
print(sklad._dict)