class Car:
    def __init__(self, c, n, is_p = False, i = 0):
        self.color = c
        self.name = n
        self.is_police = is_p
        self.index = i
        print(f'New car {n} has a {c} color \nIs it a police car? {is_p}')



    def go(self):
        self.i = 1
        return f'{self.name} is being driving now'


    def stop(self):
        self.i = 2
        return f'{self.name} has been stopped'


    def show_speed(self, speed):
        if self.i == 2:
            print('Speed is zero')
        else:
            print(f'Speed is {speed}')


    def turn_direction(self, direction):
        if self.i == 2:
            f'{self.name} is still stopped'
        elif self.i == 1:
            return f'{self.name} turned {direction}'


class TownCar(Car):
    def show_speed(self, speed):
        return f'{self.name} -  Its speed is {speed}. Over speed!' if speed > 60 else super().show_speed()


class WorkCar(Car):
    def show_speed(self, speed):
        return f'{self.name} -  Its speed is {speed}. Over speed!' if speed > 40 else super().show_speed()


class SportCar(Car):
    """SportCar"""



class PoliceCar(Car):
     """Police car"""
     def __init__(self, c, n, is_p = True):
         super().__init__( c, n, is_p)




car = Car('Space Gray', 'Mersedes AMG')
towny = TownCar('Yellow', 'Lancer')
worky = WorkCar('Black', 'Mersedes S class')
sporty = SportCar('Purple','Porsche 911')
policy = PoliceCar('White', 'Niva')
print(car.stop())
print(car.show_speed(100))
print()
print()
print()


cars_list = [car, towny, worky, sporty, policy]
for cars in cars_list:
    print(cars.go())
    print(cars.show_speed(100))
    print(cars.turn_direction('Left'))
    print(cars.stop())
    print()





