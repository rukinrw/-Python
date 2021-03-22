from time import sleep

class TrafficLight:

    __color = 'красный'

    def running(self):
        run = 1

        while run == 1:
            print(f'{self.__color.upper()} - будет гореть 7 секунд')
            sleep(7)
            self.__color = 'желтый'
            print(f'{self.__color.upper()} - будет гореть 2 секунды')
            sleep(2)
            self.__color = 'зеленый'
            print(f'{self.__color.upper()} - будет гореть 10 секунд')
            sleep(10)
            self.__color = 'красный'
            run = int(input('Светофор выключился, для включения введите "1" '))

light = TrafficLight()
light.running()