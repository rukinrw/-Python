class Road:

    def mass(self, lenght, width):
        _lenght = lenght
        _width = width
        depth = int(input("Введите толщину полотна: "))
        res = _lenght * _width * 25 * depth
        print(f'Масса асфальта: {res/1000} т')

result = Road()
result.mass(20, 5000)
