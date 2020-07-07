import math


def fuct(n):
    for el in range(1, n+1):
        yield math.factorial(el)


n = int(input("Введите целое положительное число: "))

for ind, el in enumerate(fuct(n), 1):
    print(f'{ind}! =', el)