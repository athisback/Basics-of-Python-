class Road:
    def __init__(self, l, w):
        self._length = l
        self._width = w

    def formula(self, mass = 30, ch = 3 ):

        return f'{self._length} m * {self._width} m * {mass} kg * {ch} sm = ' \
               f'{self._length * self._width * mass * ch} kg'

road = Road(1000, 23)
print(road.formula())