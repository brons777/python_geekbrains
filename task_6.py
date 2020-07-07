from itertools import count, cycle

# iterator_1 // печатает значения от 3 до 20 в одну строку

for el in count(3):
    if el <= 20:
        print(el, end=" ")
    else:
        break

# iterator_2 // печатает последовательность от 1 до 5 три раза

print("\n")
my_list = [el for el in range(1, 6)]
step = 0
pass_cycle = 0
for el in cycle(my_list):
    print(el, end=" ")
    step += 1
    if step == len(my_list):
        pass_cycle += 1
        step = 0
        print("\n")
    if pass_cycle == 3:
        break


