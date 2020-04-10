a = open("text.txt", "r")
line = 0

for i in a:
    line += 1

    flag = 0
    word = 0

    for j in i:
        if j != ' ' and flag == 0:
            word += 1
            flag = 1
        elif j == ' ':
            flag = 0
    print(i, len(i), 'символов', word, 'слов')

print(line, 'строк(и)')
a.close()