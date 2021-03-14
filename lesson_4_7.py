n = int(input('Введите число: '))

def fact(n):
    i = 1
    for num in range(1, n + 1):
        i = i * num
        print(f"Число {num}")
        yield i

for el in fact(n):
    print(f'Факториал равен {el}')