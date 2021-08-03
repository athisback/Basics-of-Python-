time = int(input('Введите время в секундах'))
hours = time // 3600
minutes = time // 60 - hours * 60
secs = time - hours * 3600 - minutes * 60
print(f'time - {hours}:{minutes}:{secs}')