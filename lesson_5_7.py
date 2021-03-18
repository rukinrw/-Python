import json

with open('firms.txt', mode='r', encoding='utf-8') as firms:

    marg_l = [] #Список расчета прибыли
    plus_d = {} #Словарь прибыли
    firm_l = [] #Список для всех словарей
    minus_d = {} #Словарь убытков
    aver_d = {} #Словарь средней прибыли

    for num, line in enumerate(firms, 1):
        margin = int(line.split(" ")[2]) - int(line.split(" ")[3])
        if margin > 0: #если прибыль
            marg_l.append(margin)
            plus_d[line.split(" ")[0]] = margin
        if margin < 0: #если убыток
            minus_d[line.split(" ")[0]] = margin
        print(line.split("\n")[0])

    av_margin = margin
    aver_d["av_margin"] = (sum(marg_l) / len(marg_l))
    firm_l.append(plus_d)
    firm_l.append(aver_d)
    firm_l.append(minus_d)
    print(f'\nСредняя прибыль равна {sum(marg_l) / len(marg_l)}\n')
    print('Итоговый список: (Прибыль - Среднее - Убыток)')
    print(firm_l)
    with open('firms.json', 'w') as firms_j:
        json.dump(firm_l, firms_j)
        print('\nИтоговый список записан в файл "firms.json"')