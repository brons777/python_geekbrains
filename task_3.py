def my_func(a, b, c):
    result = max(a + b, a + c, b + c)
    return result

result = my_func(10, 20, 30)
print(f"Сумма наибольших двух аргументов: {result}")

my_func = lambda a, b, c: max(a + b, a + c, b + c)
print("Сумма наибольших двух аргументов:", my_func(30, 10, 20))

