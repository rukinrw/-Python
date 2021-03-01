# Блок ввода данных
user_time = int(input("Введите время в секундах для расчета: "))

# Блок расчета
hour = user_time // 3600
minutes = (user_time % 3600) // 60
seconds = (user_time % 3600) % 60

# Вывод готового результата в виде чч:мм:сс
print(f'Ваше время составляет: {hour:02d}:{minutes:02d}:{seconds:02d}')