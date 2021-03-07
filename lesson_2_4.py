text = input('Введите пожалуйста несколько слов через пробел: ')

for num, element in enumerate(text.split(), 1):
    print(num, element[0:10])