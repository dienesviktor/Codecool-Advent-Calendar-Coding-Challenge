import time
import os


def clear(s):
    time.sleep(s)
    os.system("cls||clear")


def write_file(map, file):
    with open(file, "w") as file:
        for i in range(len(map)):
            file.write(map[i])


def delivery_gifts(map, file="data_files/challenge-3.frames"):
    index = map.index("H")
    for i in range(index, len(map)):
        if map[i] == "H":
            map[i] = "O"
            write_file(map, file)
            print(*map, sep="")
            clear(0.3)
            map[i] = "H"
            write_file(map, file)
        if map[i] == "#":
            map[i] = "O"
            write_file(map, file)
            print(*map, sep="")
            clear(0.3)
            map[i] = "#"
            write_file(map, file)
        if map[i] == " ":
            map[i] = "O"
            write_file(map, file)
            print(*map, sep="")
            clear(0.1)
            map[i] = "*"
            write_file(map, file)
    for i in range(0, index):
        if map[i] == "H":
            map[i] = "O"
            write_file(map, file)
            print(*map, sep="")
            clear(0.3)
            map[i] = "H"
            write_file(map, file)
        if map[i] == "#":
            map[i] = "O"
            write_file(map, file)
            print(*map, sep="")
            clear(0.3)
            map[i] = "#"
            write_file(map, file)
        if map[i] == " ":
            map[i] = "O"
            write_file(map, file)
            print(*map, sep="")
            clear(0.1)
            map[i] = "*"
            write_file(map, file)
    print(*map, sep="")
