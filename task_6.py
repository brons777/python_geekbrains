final_string = ''
def int_func(text):
    result = text.title() + ' '
    return result

string = list(input("введите строку текста: ").split())

for word in string:
    final_string += int_func(word)

print("Итоговая строка:", final_string.strip())