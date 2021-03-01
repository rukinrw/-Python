a = int(input('Сколько километров  Вы пробежали в первый день: '))
b = int(input('Сколько километров в день Вы хотите пробегать: '))

day_num = 1

while a <= b:
    print(day_num, '-й день: {:.2f} км'.format(a))
    a = a + a  * 0.1
    day_num = day_num + 1
print(day_num, '-й день: {:.2f} км'.format(a))

print('Ответ: на', day_num, '-й день: спортсмен достиг результата - не менее {:.0f} км'.format(a))