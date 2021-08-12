my_list = [(-10 + 5j), 1023, -78.345, TypeError, False, 'str',
           (5, 6, 6.5), frozenset(), {'car': 'AMG MERS', 'name': 'Mike'}, {9, 10},
           frozenset(), range(1234), (b'one'), bytearray(b'twenty'),
           (16, 17), ('a', 'b')]

for i, item in enumerate(my_list, 1):
    print(f"{i}) {item} - {type(item)}")