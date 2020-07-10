with open('task_3.txt') as f:
    line = f.readlines()

print("Оклад меньше 20000 имеют:")
avrg = 0
for el in line:
    if float(el.split()[1]) <= 20000:
        print(el.split()[0])
    avrg += float(el.split()[1])

print("Средний оклад:", '{:.2f}'.format(avrg/int(len(line))))
