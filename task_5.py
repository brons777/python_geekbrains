import random

sum = 0
with open('task_5.txt', 'w') as f:
    for i in range(1, random.randint(5, 10)):
        f.write(str(random.randint(1, 100)) + ' ')
temp = ''
with open('task_5.txt', 'r') as f:
    line = f.readline()
    for el in line:
        if el != ' ':
            temp += el
        else:
            sum += int(temp)
            temp = ''
print("Сумма чисел в файле:", sum)