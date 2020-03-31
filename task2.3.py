seasons_l = ['winter', 'spring', 'summer', 'autumn']
seasons_d = {1 : 'winter', 2 : 'spring', 3 : 'summer', 4 : 'autumn'}
a = int(input('Введите номер месяца: '))

if a == 1 or a == 2 or a == 12:
    print(seasons_d.get(1))
    print(seasons_l[0])
elif a == 3 or a == 4 or a == 5:
    print(seasons_d.get(2))
    print(seasons_l[1])
elif a == 6 or a == 7 or a == 8:
    print(seasons_d.get(3))
    print(seasons_l[2])
elif a == 9 or a == 10 or a == 11:
    print(seasons_d.get(4))
    print(seasons_l[3])
else:
    print(input('Такого месяца нет.'))

