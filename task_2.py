with open('task_2.txt') as f:
    line = f.readlines()

print("Количество строк в файле:", len(line))

for ind, el in enumerate(line, 1):
    print(f"В {ind}-й строке {len(el.split())} слов(а)")

