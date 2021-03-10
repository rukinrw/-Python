def my_func(a, b, c):
    sum = a + b + c - min(a, b, c)
    print(f'a = {a}, b = {b}, c = {c}.\nСумма двух наибольших аргументов = {sum}')

my_func(5, 2, 6)