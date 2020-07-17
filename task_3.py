class Cell:
    def __init__(self, total_cell):
        self.total = total_cell

    def __add__(self, other):
        return Cell(self.total + other.total)

    def __sub__(self, other):
        return Cell(
            self.total - other.total if self.total - other.total > 0 else print("Вычитание клеток выполнить нельзя"))

    def __mul__(self, other):
        return Cell(self.total * other.total)

    def __truediv__(self, other):
        return Cell(self.total / other.total)

    def make_order(self, count_in_a_row):
        itog = ''
        for i in range(1, self.total + 1 + self.total // count_in_a_row):
            if i % (count_in_a_row + 1) != 0:
                itog += '*'
            elif i != self.total + self.total // count_in_a_row:
                itog += r'\n'
        return str(itog.rstrip())


class Iterator(Cell):
    def __init__(self, total_cell, start, count_in_a_row):
        self.total = total_cell
        self.i = start
        self.count = count_in_a_row

    def __next__(self):
        self.i += 1
        if self.i <= self.total + self.total // self.count:
            if self.i % (self.count + 1) != 0:
                return '*'
            elif self.i != self.total + self.total // self.count:
                return r'\n'
            else:
                return ''
        else:
            raise StopIteration


class IterObj:
    def __init__(self, start=0):
        self.start = start

    def __iter__(self):
        return Iterator((my_cell_1 + my_cell_2).total, self.start, 5)


my_cell_1 = Cell(22)
my_cell_2 = Cell(10)

print((my_cell_1 + my_cell_2).total)
print((my_cell_1 - my_cell_2).total)
print((my_cell_1 * my_cell_2).total)
print((my_cell_1 / my_cell_2).total)

print("Способ 1 вывода на экран количества клеток (через метод make_order)")

print(my_cell_1.make_order(5))
print(my_cell_2.make_order(5))

print("Способ 2 вывода на экран количества клеток (через объект итератор): my_cell_1 + my_cell_2")

obj = IterObj(0)
for el in obj:
    print(el, end='')