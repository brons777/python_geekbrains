from abc import ABC, abstractmethod


class MyAbstractClassCoat(ABC):
    @abstractmethod
    def __init__(self, size):
        pass


class MyAbstractClassSuit(ABC):
    @abstractmethod
    def __init__(self, height):
        pass


class MyAbstractClassClothes(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def total(self):
        pass

    @abstractmethod
    def add_clothes(self, name, param):
        pass


class Coat(MyAbstractClassCoat):
    def __init__(self, total):
        self.total = total / 6.5 + 0.5


class Suit(MyAbstractClassSuit):
    def __init__(self, total):
        self.total = 2 * total + 0.3


class Clothes(MyAbstractClassClothes):
    def __init__(self):
        self.clothes = []

    def add_clothes(self, name, param):
        if name == 'coat':
            self.clothes.append(Coat(param))
            print(f'Успешно добавлен экземпляр {name} с параметром {param}')
        elif name == 'suit':
            self.clothes.append(Suit(param))
            print(f'Успешно добавлен экземпляр {name} с параметром {param}')
        else:
            print("Такой одежды нет")

    @property
    def total(self):
        total = 0
        for el in self.clothes:
            total += el.total
        return total


my_clothes = Clothes()
my_clothes.add_clothes('suit', 1)
my_clothes.add_clothes('coat', 6.5)
my_clothes.add_clothes('c', 6.5)
print("Итого ткани: ", my_clothes.total)

