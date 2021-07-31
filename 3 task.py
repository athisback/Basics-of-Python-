a = input("Введите положительное число - ")

while int(a) <= 0:
    a = input("Внимательнее, введите положительное число - ")

print(f"{a} + {a + a} + {a + a + a} = {int(a) + int(a + a) + int(a + a + a)}")

