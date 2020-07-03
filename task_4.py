while True:
    try:
        x = int(input("Введите положительное число: "))
        y = int(input("Введите отрицательное число: "))
        break
    except:
        print("Неверные данные")

# Method_1

def my_func(x, y):
    result = x ** y
    return result

print("x^y =", my_func(x, y))

# Method_2

def my_func_1(x, y):
    temp = x
    for i in range(abs(y)-1):
        temp *= x
    result = 1 / temp
    return result

print("x^y =", my_func_1(x, y))