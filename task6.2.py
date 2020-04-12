class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weigth = 25
        self.height = 5

    def asphalt(self):
        asphalt = self._length * self._width * self.weigth * self.height / 1000
        print(f'Для покрытия дороги необходимо {round(asphalt)} тонн асфальта')

k = Road(5000, 20)
k.asphalt()