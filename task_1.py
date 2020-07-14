import itertools
import time


class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def running(self):
        for i in itertools.cycle(self.__color):
            print(i)
            if i == 'red':
                time.sleep(7)
            elif i == 'yellow':
                time.sleep(2)
            else:
                time.sleep(8)


color = ['red', 'yellow', 'green']

my_trLight = TrafficLight(color)
my_trLight.running()
