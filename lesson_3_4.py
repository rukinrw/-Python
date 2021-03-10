def my_func(x, y):
    c = x ** y
    print(f'Решение №1\n"А" в степени "B" = {c}')

def my_func_cycle(x, y):
    i = x
    while y < -1:
        i = i * x
        y += 1
    c = 1 / i
    print(f'Решение №2\n"А" в степени "B" = {c}')

a, b = 0, 0

while a == 0 or a < 0:
    a = float(input('Введите число "A" (действительное положительное): '))

while b == 0 or b > 0:
    b = int(input('Введите число "B" (целое отрицательное): '))

my_func(a, b)
my_func_cycle(a, b)