seconds = int(input('Введите количество секунд:'))

hours = seconds // 3600 % 24
minutes_1 = seconds // 60 % 60 // 10
minutes_2 = seconds // 60 % 60 % 10
seconds_1 = seconds % 3600 % 60 // 10
seconds_2 = seconds % 3600 % 60 % 10

if hours <= 9:
    print(f"0{hours}:{minutes_1}{minutes_2}:{seconds_1}{seconds_2}")
else:
    print(f"{hours}:{minutes_1}{minutes_2}:{seconds_1}{seconds_2}")