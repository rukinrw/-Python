my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(f'Начальный список - {my_list}')

new_list = [el for el in my_list if my_list.count(el) == 1]

print(f'Числа не имеющие повторений - {new_list}')