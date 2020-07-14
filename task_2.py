class Road:
    def __init__(self, width, length):
        self._width = width
        self._length = length


    def mass(self):
        return self._width * self._length * 25 * 5


my_road = Road(100, 100)
print("Масса асфальта:", my_road.mass())


