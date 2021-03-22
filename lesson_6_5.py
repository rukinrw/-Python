class Stationery:

    def __init__(self):
        self.title = "Название"

    def draw(self):
        print("Запуск отрисовки.")

class Pen(Stationery):
    def draw(self):
        print(f"Пишем {self.title} ручкой")

class Pencil(Stationery):
    def draw(self):
        print(f"Пишем {self.title} карандашом")

class Handle(Stationery):
    def draw(self):
        print(f"Пишем {self.title} маркером")

print("_" * 50)
result = Stationery()
result.draw()
print("_" * 50)
Pen().draw()
print("_" * 50)
Pencil().draw()
print("_" * 50)
Handle().draw()
