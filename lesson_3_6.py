def int_func(text):
    my_list = list(text)
    my_list[0] = (str(my_list[0])).upper()
    text = ''.join(my_list)
    return text

text = str(input('Введите слово в нижнем регистре: '))
print(int_func(text))

text = str(input('Введите несколько слов в нижнем регистре: '))
user_list = text.split(" ")
i = 0
while i < len(user_list):
    word = str(user_list[i])
    user_list[i] = int_func(word)
    i += 1
text = ' '.join(user_list)
print(text)


