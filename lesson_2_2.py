list_len = int(input("Задайте длинну вашего списка от 2 до 10: "))
user_list = list()
print(f"Вы создали список из {list_len} элементов, теперь заполните его!")

while list_len > len(user_list):
    value = input(f"Введите значение элемента {len(user_list)}: ")
    user_list.append(f'{value}')

print("Поздравляем! Ваш список готов!")
print(user_list)

i = 0
while (i + 1) < len(user_list):
    user_list[i], user_list[i + 1] = user_list[i + 1], user_list[i]
    i = i + 2

print("А вот и поменяли местами соседние элементы!")
print(user_list)