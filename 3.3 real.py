def my_func(arg_1, arg_2, arg_3):
    my_list = [arg_1, arg_2, arg_3]
    return sum(sorted(my_list)[1:])
print(my_func(20, 1000, -123))
