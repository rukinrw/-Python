class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):

    def get_full_name(self):
        print(f'Полное имя сотрудника: {self.name} {self.surname}')

    def get_total_income(self):
        income = int(self._income.get("wage")) + int(self._income.get("bonus"))
        print(f'Доход состаляет {income}р.')

f_name = Position("Вася", "Пупкин", "ДИРЕКТОР", 10000, 5000)
f_name.get_full_name()
f_name.get_total_income()