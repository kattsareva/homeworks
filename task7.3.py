class Cell:

    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        return self.quantity + other.quantity

    def __sub__(self, other):
        sub = self.quantity - other.quantity
        return {sub} if sub > 0 else 'Клетка исчезла'

    def __truediv__(self, other):
        return self.quantity // other.quantity

    def __mul__(self, other):
        return self.quantity * other.quantity

    def make_order(self, row):
        result = ''
        for i in range(int(self.quantity / row)):
            result += '*' * row + '\n'
        result += '*' * (self.quantity % row) + '\n'
        return result


c = Cell(int(input('Введите: ')))
c_2 = Cell (int(input('Введите ')))
print(c + c_2)
print(c - c_2)
print(c / c_2)
print(c * c_2)
print(c.make_order(3))