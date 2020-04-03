def my_func(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])

print(my_func(surname='Tsareva', name='Katya', year='1998', city='Moscow', email='katheryn.tsareva@yandex.ru',
              telephone='123456789'))