from sys import argv


def salary_func():
    try:
        work_hour, bid_hour, premium = map(int, argv[1:])
        salary = (work_hour * bid_hour) + premium
        return (f'Your salary is - {salary}')
    except ValueError:
        print('U have a ValueError hahahah!')


print(salary_func())