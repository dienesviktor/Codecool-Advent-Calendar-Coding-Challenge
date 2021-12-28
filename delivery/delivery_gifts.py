import time
import os


def clear(s):
    time.sleep(s)
    os.system("cls||clear")


def delivery_gifts(map):
    with open("data_files/challenge-3.frames", "w") as file:
        for i in range(len(map)):
            file.write(map[i])



    # for i in range(x, len(map)):
    #     if map[i] == "H":
    #         map[i] = "O"
    #         clear(0.1)
    #         print(*map, sep=" ")
    #         clear(0.5)
    #         map[i] = "H"
    #         clear(0.1)
    #         print(*map, sep=" ")
    #     if map[i] == "#":
    #         map[i] = "O"
    #         clear(0.1)
    #         print(*map, sep=" ")
    #         clear(0.5)
    #         map[i] = "#"
    #         clear(0.1)
    #         print(*map, sep=" ")
    #     if map[i] == " ":
    #         map[i] = "O"
    #         clear(0.1)
    #         print(*map, sep=" ")
    #         map[i] = "*"
    #         clear(0.1)
    #         print(*map, sep=" ")


    # for i in range(0, x):
    #     if map[i] == "H":
    #         map[i] = "O"
    #         clear(0.1)
    #         print(*map, sep=" ")
    #         clear(0.5)
    #         map[i] = "H"
    #         clear(0.1)
    #         print(*map, sep=" ")
    #     if map[i] == "#":
    #         map[i] = "O"
    #         clear(0.1)
    #         print(*map, sep=" ")
    #         clear(0.5)
    #         map[i] = "#"
    #         clear(0.1)
    #         print(*map, sep=" ")
    #     if map[i] == " ":
    #         map[i] = "O"
    #         clear(0.1)
    #         print(*map, sep=" ")
    #         map[i] = "*"
    #         clear(0.1)
    #         print(*map, sep=" ")