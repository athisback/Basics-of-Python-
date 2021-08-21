my_list = [num for num in range(100, 1001, 2)]
count = 1
for i in my_list:
    count *= i

print(f'My final list: \n{my_list} \nПроизведение всех чисел из списка: \n{count}')
