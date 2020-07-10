import json

with open('task_7.txt') as f:
    line = f.readlines()

finish_list =[]
temp_dict = {}
temp_avrg = 0
for el in line:
    plus = float(el.split()[2]) - float(el.split()[3])
    temp_dict[el.split()[0]] = plus
    if plus > 0:
        temp_avrg += plus

finish_list.append(temp_dict)
temp_dict = {}
temp_dict['average_profit'] = temp_avrg / len(line)
finish_list.append(temp_dict)
temp_dict = {}

print(finish_list)

with open('task_7.json', 'w') as f:
    json.dump(finish_list, f)

