def unpack(value):
    num = ''
    for el in value:
        if el.isdigit():
            num = num + el
        else:
            if num != '':
                value_l.append(int(num))
                num = ''
    if num != '':
        value_l.append(int(num))
    summ = sum(value_l)
    return summ

learn_d = {}

with open('learn.txt', mode='r', encoding='utf-8') as learn:
    for line in learn:
        key = line.split(':')[0]
        value = str(line.split(':')[1].split("\n")[0])
        value_l = []
        learn_d[key] = unpack(value)
    print(learn_d)