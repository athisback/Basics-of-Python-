class Worker:
    def __init__(self, n, sn, pos, wage, bonus):
        self.name = n
        self.surname = sn
        self.position = pos
        self._income = {"wage": wage,"bonus": bonus }


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def full_income(self):
        return f'{sum(self._income.values())}'


pos = Position('Aziz', 'Amanov', 'Junior  software engineer', 1000, 500 )
print(pos.get_full_name())
print(pos.full_income())
