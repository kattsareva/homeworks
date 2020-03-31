p = input('Пишите ')
word = []

num = 1

for elem in range(p.count(' ') + 1):
    word = p.split()
    if len(str(word)) <= 10:
        print(f' {num} {word [elem]}')
        num += 1
    else:
        print(f' {num} {word [elem] [0:10]}')
        num += 1
