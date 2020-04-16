from abc import ABC, abstractmethod

class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    @property
    def consumption(self):
        return (f'Необходимо ткани: {self.param / 6.5 + 0.5 + 2 * self.param + 0.3 :.2f}')

    @abstractmethod
    def abstract(self):
        return 'S'

class Costume(Clothes):

    def consumption(self):
        return f'Для костюма надо {2 * self.param + 0.3 :.2f} ткани'

    def abstract(self):
        pass

class Coat(Clothes):

    def consumption(self):
        return f'Для пальто надо {self.param / 6.5 + 0.5 :2f} ткани'

    def abstract(self):
        pass

a = Coat(int(input('Введите размер')))
b = Costume(int(input('Введите рост:')))
print(b.consumption())
print(b.abstract())
print(a.consumption())