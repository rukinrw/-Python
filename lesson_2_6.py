print('Добро пожаловать в Ваш интернет магазин! Добавьте Ваши товары!')

store = []
add = 1
num = int(1)
param = {}
prod = ()
list_name = []
list_price = []
list_volume = []
list_ed = []
key = ['name', 'price', 'volume', 'ed']

while add == 1:
    name = input('Название: ')
    price = input('Цена единицы: ')
    volume = input('Количество: ')
    ed = input('Единица измерения: ')
    add = int(input('Добавить еще товар? ДА = "1", НЕТ = "0": '))
    param = {
        'name': name,
        'price': price,
        'volume': volume,
        'ed': ed
    }
    list_name.append(name)
    list_price.append(price)
    list_volume.append(volume)
    list_ed.append(ed)
    prod = (num, param)
    store.append(prod)
    num += 1

# store = [(1, {"name": "компьютер", "price": 20000, "volume": 5, "ed": "шт"}),
#         (2, {"name": "планшет", "price": 10000, "volume": 12, "ed": "шт"}),
#         (3, {"name": "сканер", "price": 5000, "volume": 10, "ed": "шт"})
#         ]"""

print("Поздравляем! Ваш магазин заполнен!")
for el in store:
    print(el)

print(f"Аналитика по магазину:")

value = [list_name, list_price, list_volume, list(set(list_ed))]

i = 0

while len(key) > i:
    print(f'{key[i]} : {value[i]}')
    i += 1
