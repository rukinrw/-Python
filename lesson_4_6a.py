from itertools import count
my_list = []

start = int(input('Введите начальное число: '))
stop = int(input('Введите конечное число: '))

for el in count(start):
    if el > stop:
        break
    else:
        print(el)