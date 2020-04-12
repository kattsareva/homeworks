class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Зарисовка началась.')

class Pen(Stationery):
    def draw(self):
        print(f'Зарисовка началась {self.title}.')

class Pencil(Stationery):
    def draw(self):
        print(f'Зарисовка началась {self.title}.')

class Handle(Stationery):
    def draw(self):
        print(f'Зарисовка началась {self.title}.')


pen = Pen('ручкой')
print(pen.draw())
pencil = Pencil('карандашом')
print(pencil.draw())
handle = Handle('маркером')
print(handle.draw())