my_list = [9, 7, 5, 3, 2, 1]
a = int(input('Введите число '))

for elem in range(len(my_list)):
    if my_list[elem] == a:
        my_list.insert(elem + 1, a)
        break
    elif my_list[elem] < a:
        my_list.insert(0, a)
        break
    elif my_list[elem] > a and my_list[elem + 1] < a:
        my_list.insert(elem + 1, a)
        break
    elif my_list[-1] > a:
        my_list.append(a)
        break

print(my_list)