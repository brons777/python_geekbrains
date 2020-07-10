with open('task_6.txt') as f:
    line = f.readlines()

print(line)
my_dict = {}
sum = 0
for el in line:
    key = el[:el.index(':')]
    print(key)
    for elem in el.split():
        if '(' in elem:
            sum += int(elem[:elem.index('(')])
    my_dict[key] = sum
    sum =0

print(my_dict)