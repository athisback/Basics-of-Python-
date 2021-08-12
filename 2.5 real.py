rating = [7, 5, 3, 3, 2]
i = 0
user_rating = int(input('Enter u rating - '))
for rt in rating:
    if user_rating <= rt:
        i += 1
    else:
        break
rating.insert(i, float(user_rating))
print(rating)
