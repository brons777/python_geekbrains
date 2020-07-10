with open('task_4.txt') as f:
    line = f.readlines()

my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('task_4_new.txt', 'w', encoding="utf-8") as f:
    for el in line:
        if el.split()[0] in my_dict.keys():
            new_line = el.split()[0].replace(el.split()[0], my_dict.get(el.split()[0])) + ' - ' + el.split().pop() + '\n'
            f.write(new_line)