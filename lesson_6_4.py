class Car():

    def __init__(self, speed, color, name, is_police):
        self.speed = int(speed)
        self.color = color
        self.name = name

    def go(self):
        if self.speed > 0:
            print('Машина едет')


    def stop(self):
        if self.speed == 0:
            print('Машина стоит')

    def turn(self, direction):
        if direction == "лево":
            print('Машина повернула налево')
        else:
            if direction == "право":
                print('Машина повернула направо')
            else:
                if direction == "назад":
                    print('Машина развернулась')
                else:
                    print('Машина не меняла направления')

    def show_speed(self):
        print(f"Скорость автомобиля равна {self.speed} км\ч.")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Скорость автомобиля равна {self.speed} км\ч.\nГородская машина превышает скорость!")

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        self.name = name
        print(f'{self.name}')
        self.speed = speed
        self.color = color

class WorkCar(Car):
    def show_speed(self):
        print(f'{self.name}')
        if self.speed > 40:
            print(f"Скорость автомобиля равна {self.speed} км\ч.\nРабочая машина превышает скорость!")

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        print(f'{name} - полицейская машина')
        self.is_police = True
        self.speed = speed
        self.color = color

print("-" * 70)
police = PoliceCar(100, "Синий", "Уаз Бобик", True)
police.go()
police.stop()
police.turn("назад")
police.show_speed()

print("-" * 70)
sport = SportCar(360, "Красный", "Mazeratti", False)
sport.go()
sport.stop()
sport.turn("лево")
sport.show_speed()
print("-" * 70)

work = WorkCar(90, "Черный", "Мусоровоз", False)
work.go()
work.stop()
work.turn("право")
work.show_speed()
print("-" * 70)