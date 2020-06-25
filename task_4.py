number = int(input('Введите целое число: '))
max = 0
while number // 10 != 0:
    temp_max = number % 10
    if temp_max > max:
        max = temp_max
    number = number // 10

print('Максимальная цифра в числе: ', max)

