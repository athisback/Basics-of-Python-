num = int(input('Введите целое положительное число - '))
max = num % 10

while num > 0:
    digit = num % 10 # крайняя цифра
    if digit > max:
        max = digit
        if digit == 9:
            break

    num = num // 10
    print(num)

print(f"Наибольшая цифра в  введенном числе равна {max}")

