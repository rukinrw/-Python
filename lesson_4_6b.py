from itertools import cycle
my_list = [24, 33, 2, 7, 243, 1000, 4487, 44, 3, 245, 10, 777, 4, 11]

stop = int(input('Сколько элементов вывести? '))

i = 1
for el in cycle(my_list):
    if i > stop:
        break
    else:
        print(el)
        i += 1