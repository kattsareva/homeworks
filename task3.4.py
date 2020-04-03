def my_func(x, y):
    if y > 0 or x < 0:
        return 'NO'
    else:
        return x ** y

print(f'Ответ: {my_func(int(input("x: ")), int(input("y: ")))}')