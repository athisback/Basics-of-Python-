snt = input('Введите набор слов -').split()
for i, word in enumerate(snt, 1):
    print(f'{i}) {word[:10]}')

