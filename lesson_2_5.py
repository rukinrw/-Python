my_list = [7, 5, 3, 3, 2]

print(f'Приветствую! Наш рейтинг выглядит так:\n{my_list}')

num = int(input('Введите число для добавления его в рейтинг: '))

element = 0
pos = 0
i = 0

while i < len(my_list):
    element = my_list[i]
    if num > element:
        break
        pos = 0
    if num == element:
        break
        pos = i
    else:
        pos = i + 1
    i += 1

my_list.insert(pos, num)
print(f'Ваше число добавлено в рейтинг!\n{my_list}')