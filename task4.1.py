def calc():
    h = float(input('Количество отработанных часов: '))
    w = float(input('Оплата работы в час: '))
    b = float(input('Размер премии: '))
    pay = h * w
    return pay + b

print(f'Размер зарплаты: {calc()}')