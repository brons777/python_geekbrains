class Worker:
    def __init__(self, worker_name, worker_surname, worker_position, worker_income):
        self.name = worker_name
        self.surname = worker_surname
        self.position = worker_position
        self._income = worker_income


class Position(Worker):
    def get_total_income(self):
        sum = 0
        for value in self._income.values():
            sum += value
        return sum


    def get_full_name(self):
        return self.name + ' ' + self.surname


worker_1 = Position('Ivan', 'Utkin', 'Engineer', {'wage': 15000,  'bonus': 3000})
print(worker_1.get_full_name(), end=': ')
print(worker_1.get_total_income())

