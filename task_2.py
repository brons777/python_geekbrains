list_1 = list(map(int, input('введите элементы списка через пробел: ').split()))

print(f'Неизмененный список: {list_1}')

if len(list_1) % 2 == 0:
    for i in range(0, len(list_1), 2):
        temp = list_1[i]
        list_1[i] = list_1[i+1]
        list_1[i+1] = temp
else:
    for i in range(0, len(list_1)-1, 2):
        temp = list_1[i]
        list_1[i] = list_1[i+1]
        list_1[i+1] = temp

print(f'Измененный список: {list_1}')

