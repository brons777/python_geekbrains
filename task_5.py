from functools import reduce

my_list = [el for el in range(100, 1001) if el % 2 == 0]


def my_func(prev, curr):
    return prev * curr


print(reduce(my_func, my_list))

