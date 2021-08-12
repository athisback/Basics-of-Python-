a, b = int(input('Введите начальное значение -')), int(input('Введите конечное значение -'))
count = 0
while a < b:
    a = a * 1.1
    count += 1
    print(a)
print(f'Спортсмен достиг нужного результата за {count} дней')