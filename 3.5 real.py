def sum_num():
    sm = 0
    while True:
        sum_list = input('Введите число или Q для выхода: ').split()
        for num in sum_list:
            if num == 'q' or num == 'Q':
                return print(sm)
            else:
                try:
                    sm+= int(num)
                except ValueError:
                    print('Чтобы выйти из программы нажмите q - ')

        print(f'Сумма чисел = {sm}')

sum_num()