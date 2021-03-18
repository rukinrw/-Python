with open("workers.txt") as my_file:
    i = 0
    file = my_file.readlines()
    print(f"Сотрудники с окладом ниже 20000:")
    average = 0
    while i < len(file):
        line = file[i]
        line = line.split('\n')[0]
        line = line.split(" ")
        average = average + int(line[1])
        name = line[0]
        if int(line[1]) < 20000:
            print(f"{name}, оклад: {int(line[1])}")
        i += 1
    print(f"Средняя зарплата всех сотрудников - {average / len(file)}р.")