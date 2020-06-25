plus = int(input('Введите значение выручки: '))
minus = int(input('Введите значение издержек: '))

if plus > minus:
    print('Фирма работает на прибыль')
    print('Рентабельность выручки:', (plus - minus) / plus)
    persons = int(input('введите кол-во сотрудников:'))
    print('Прибыль на одного сотрудника:', (plus - minus) / persons)
else:
    print('Фирма работает в убыток')