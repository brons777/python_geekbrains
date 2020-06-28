print('Решение с помощью списка')

month = int(input('Введите номер месяца: '))

list_1 = []
for i in range(12):
    list_1.append(i+1)

if month in list_1[2:5]:
    print('Весна')
elif month in list_1[5:8]:
    print('Лето')
elif month in list_1[8:11]:
    print('Осень')
else:
    print('Зима')

print('Решение с помощью словаря')

month = int(input('Введите номер месяца: '))

dict_month = {'Лето': [6, 7, 8], 'Осень': [9, 10, 11], 'Зима': [12, 1, 2], 'Весна': [3, 4, 5]}

for key, el in dict_month.items():
    if month in el:
        print(key)

