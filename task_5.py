class Stationery:
    def __init__(self, stationery_title):
        self.title = stationery_title

    def draw(self):
        print("Запуск отрисовки...")


class Pen(Stationery):
    def draw(self):
        print("Рисуем ручкой")


class Pencil(Stationery):
    def draw(self):
        print("Рисуем карандашом")


class Handle(Stationery):
    def draw(self):
        print("Рисуем маркером")


my_stationery = Stationery('Все принадлежности')
my_pen = Pen('Ручка')
my_pencil = Pencil('Карандаш')
my_handle = Handle('Маркер')


my_stationery.draw()
my_pen.draw()
my_pencil.draw()
my_handle.draw()

