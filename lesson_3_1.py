def my_func(arg_1, arg_2):
    a_b = arg_1 / arg_2
    b_a = arg_2 / arg_1
    print(f'A = {arg_1}, B = {arg_2}')
    print(f'A / B = {a_b:.2f}')
    print(f'B / A = {b_a:.2f}')

a, b = 0, 0

while a == 0:
    a = int(input('Введите число "A" отличное от нуля: '))

while b == 0:
    b = int(input('Введите число "B" отличное от нуля: '))

my_func(a, b)