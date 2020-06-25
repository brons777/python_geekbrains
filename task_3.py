number = int(input('Введите число от 1 до 9:'))

print(f"{number} + {number}{number} + {number}{number}{number} =", number + int(str(f'{number}'+f'{number}')) + int(str(f'{number}'+f'{number}') + f'{number}'))