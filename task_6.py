my_list =[]
keys_list = []
temp_list = []
finish_dict = {}
i = 1
while i < 3:
    name = input('введите название товара: ')
    price = int(input('введите цену товара: '))
    sum = int(input('введите количество товара: '))
    unit = input('введите единицу товара: ')
    tuple_temp = (i, {"Название: ": name, "Цена:": price, "Количество:": sum, "ед: ": unit})

    my_list.append(tuple_temp)
    i += 1

print("Товары:")
for el in my_list:
    print(el)

for el in my_list[0][1].keys():
    keys_list.append(el)

for key in keys_list:
    for el in my_list:
        temp_list.append(el[1].get(key))
    finish_dict[key] = temp_list
    temp_list = []

print("Итог:")
for el in finish_dict:
    print(el, finish_dict[el])


