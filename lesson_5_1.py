my_file = open("my_file.txt", "w")

user_text = input("Добавьте ваш текст, оставьте поле пустым, чтобы выйти: ")
while user_text != "":
    my_file.writelines(f"{user_text}\n")
    user_text = input("Добавьте ваш текст, оставьте поле пустым, чтобы выйти: ")
else:
    print('Всего доброго!')

my_file.close()