class Car:
    def __init__(self, car_speed, car_color, car_name, car_is_police):
        self.speed = car_speed
        self.color = car_color
        self.name = car_name
        self.is_police = car_is_police

    def go(self):
        print("Car is drive")

    def stop(self):
        print("Car is stopped")

    def turn(self, direction):
        print(f"Car is turned on {direction}")

    def show_speed(self):
        print(f"Speed of {self.name}:{self.speed} km/h")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"Speed of {self.name} greater than 60 km/h")
        else:
            print(f"Speed of {self.name}:{self.speed} km/h")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Speed of {self.name} greater than 40 km/h")
        else:
            print(f"Speed of {self.name}:{self.speed} km/h")


class PoliceCar(Car):
    def police(self):
        if self.is_police:
            print("Pogonya")


my_town_car = TownCar(50, 'white', 'Kia', False)
my_sport_car = SportCar(100, 'grey', 'Mazda', False)
my_work_car = WorkCar(50, 'black', 'GAZ', False)
my_police_car = PoliceCar(80, 'blue', 'Mercedes', True)

print(my_town_car.color)
print(my_sport_car.name)
print(my_police_car.is_police, '\n')

my_sport_car.go()
my_sport_car.turn("right")
my_sport_car.stop()

my_sport_car.show_speed()
my_police_car.show_speed()
my_town_car.show_speed()
my_work_car.show_speed()
my_police_car.police()

