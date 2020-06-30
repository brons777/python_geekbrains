list_1 = input('Введите строку: ').split()

for ind, el in enumerate(list_1, 1):
    if len(el) > 10:
        print(ind, ":", el[:10])
    else:
        print(ind, ":", el)

