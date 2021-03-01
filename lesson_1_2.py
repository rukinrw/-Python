# Блок ввода данных
user_time = int(input("Введите время в секундах для расчета: "))

# Блок расчета
hour = user_time // 3600
minutes = (user_time % 3600) // 60
seconds = (user_time % 3600) % 60

# Вывод готового результата в виде чч:мм:сс
print('Ваше время составляет: ', hour, ':', minutes, ':', seconds)