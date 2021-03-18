user_list = input("Введите числа через пробел: ")

numbers = open("numbers.txt", "w")
numbers.write(f'{user_list}')
numbers.close()

summ_f = open("numbers.txt", "r")
get_list = summ_f.readline().split(" ")
summ = 0
for el in get_list:
    summ = summ + int(el)
print(f"Сумма чисел равна: {summ}")
summ_f.close()