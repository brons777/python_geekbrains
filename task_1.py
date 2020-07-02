number_1 = int(input("Введите 1 число: "))
number_2 = int(input("Введите 2 число: "))

def division(num_1, num_2):
    try:
        print(num_1/num_2)
    except:
        print("Деление на ноль")

division(number_1, number_2)

