def my_func (a, b, c):
    if a >= b & c >= b:
        return a + c
    if a >= c & b >= c:
        return a + b
    else:
        return b + c

print(f'Ответ: {my_func(int(input("a: ")), int(input("b: ")), int(input("c: ")))}')