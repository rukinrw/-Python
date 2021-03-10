ost = int()
res = int()
stop = bool()

def f_stop():
    n = a.split()
    i = 0
    while i < len(n):
        if n[i] == 'СТОП':
            stop = True
            break
        else:
            stop = False
        i = i + 1
    return stop

def my_sum():
    n = a.split()
    summa = int()
    i = 0
    while i < len(n) and stop == False:
        summa = summa + int(n[i])
        i = i + 1
    return summa

def my_ost():
    n = a.split("СТОП")
    m = n[0].split()
    ost = 0
    i = 0
    while i < len(n) and m[i] != 'СТОП':
        ost = ost + int(m[i])
        i = i + 1
    return ost

while stop != True:
    a = input('Введите числа через пробел, "СТОП" прерывает операции: ')
    stop = f_stop()
    if stop == False:
        res = res + my_sum()
    else:
        res = res + my_ost()
    print(f'Сумма чисел равна: {res}')