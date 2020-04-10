a = input('Файл: ')
b = open("a", "w")
while True:
    s = input()
    if s == '': break
    b.write(s+'\n')
b.close()