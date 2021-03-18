my_file = open("my_file.txt", "r")

user_list = my_file.readlines()

for num, el in enumerate(user_list, 1):
    if el.count(' ') == 0:
        words = "слова"
    else:
        words = "слов"
    print(f"Строка №{num}, состоит из {el.count(' ') + 1} {words}.")

my_file.close()