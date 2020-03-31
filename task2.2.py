l_list = []
l_el = int(input('Сколько в списке элементов? '))

i = 0
l = 0

while i < l_el:
    l_list.append(input('Введите значение: '))
    i += 1

for elem in range (int(len(l_list) / 2)):
    l_list[l], l_list[l + 1] = l_list[l + 1], l_list[l]
    l += 2

print(l_list)