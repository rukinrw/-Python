from sys import argv

name, work_time, hour_money, bonus = argv

print("Отработано часов - ", work_time)
print("Ставка в час - ", hour_money, "р.")
print("Премия - ", bonus, "р.")
print("Зарплата - ", (int(work_time) * int(hour_money)) + int(bonus), "р.")