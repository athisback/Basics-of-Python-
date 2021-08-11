
def personal_inf(**kwargs):
    return ' '.join(kwargs.values())


name = input('Введите name - ')
surname = input('Введите surname - ')
birthday = input('Введите birthday - ')
city = input('Введите city - ')
email = input('Введите email - ')
phone = input('Введите phone - ')

print(personal_inf(name=name, surname=surname, birthday=birthday, city=city, email=email, phone=phone))


