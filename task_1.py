with open('task_1.txt', 'w') as f:
    while True:
        text = input("Введите текст: ")
        if text == "":
            break
        f.write(text + '\n')
