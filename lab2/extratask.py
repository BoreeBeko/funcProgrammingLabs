from functools import reduce


def sum(mY_tuple):
    return reduce(lambda x, y: x + y, mY_tuple)


my_tuple = (1, 2, 3, 5)
print(sum(my_tuple))


