from sys import argv


def salary(hours, price_per_our, reward):
    return (int(hours) * float(price_per_our)) + float(reward)


_, hour, price, bonus = argv
print(salary(hour, price, bonus))


# Вызов (exaple): python task_1.py 1 2 3