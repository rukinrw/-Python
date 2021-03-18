def translate (n):
    strings = {
        1: "Один",
        2: "Два",
        3: "Три",
        4: "Четыре"
    }
    new_value = strings.get(int(n))
    return new_value

with open("en_str.txt") as my_file:
    for line in my_file:
        line = line.split("\n")[0]
        line = line.split(" - ")[1]
        print(f"{translate(line)} - {line}")
        new_file = open("ru_str.txt", "a")
        new_file.write(f"{translate(line)} - {line}\n")
        new_file.close()