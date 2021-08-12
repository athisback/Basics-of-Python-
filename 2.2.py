
u_list = input('Введите числа с пробелами - ').split()

for i in range(1, len(u_list), 2):
    u_list.insert(i - 1, u_list.pop(i))
print(u_list)

