# Блок ввода данных
user_n = str(input("Введите произвольное число n: "))

n1 = user_n
n2 = n1+n1
n3 = n1+n2

summ = int(n1) + int(n2) + int(n3)

# Блок вывода данных
print('Сумма чисел в виде n+nn+nnn равна: ', summ)