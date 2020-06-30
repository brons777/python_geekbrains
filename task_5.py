my_list = [7, 5, 3, 3, 2]


while True:
    try:
        new_el = int(input("Введите новый элемент: "))
        if new_el in my_list:
            my_list.insert(my_list.index(new_el)+my_list.count(new_el), new_el)
            print(my_list)
        else:
            my_list.append(new_el)
            my_list = sorted(my_list, reverse=True)
            print(my_list)
    except:
        print("Введены неверные данные")
        break

print("итоговый список: ", my_list)