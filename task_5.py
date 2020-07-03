sum_numbers = 0
flag = False

def sum_of_numbers(data):
    global sum_numbers, flag
    for elem in data:
        if elem.isdigit():
            sum_numbers += int(elem)
        else:
            flag = True
            break
    return sum_numbers, flag


while True:
    data = list(input("введите последовательность чисел: ").split())
    sum_of_numbers(data)
    print("текущая сумма:", sum_numbers)
    if flag:
        break

print("итоговая сумма:", sum_numbers)

