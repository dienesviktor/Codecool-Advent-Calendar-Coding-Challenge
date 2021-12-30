import time
import os


def clear(s):
    time.sleep(s)
    os.system("cls||clear")


def write_file(planet, file):
    with open(file, "w") as file:
        for i in range(len(planet)):
            file.write(planet[i])


def delivery_gifts(coordinates, input="data_files/planet.map", output="data_files/challenge-3.frames"):
    with open(input, "r") as display_planet:
        display_planet = display_planet.readlines()
        planet = []
        for lines in display_planet:
            line = []
            for pos in lines:
                line.append(pos)
            planet.append(line)
    for line_num, line in enumerate(display_planet):
        for pos_num, pos in enumerate(line):
            if pos == "H":
                index = (line_num, pos_num)
    for coord in coordinates:
        if coord >= index:
            line, pos = coord
            if planet[line][pos] == "H":
                planet[line][pos] = "O"
                display_planet = "".join(j for i in planet for j in i)
                write_file(display_planet, output)
                print(*display_planet, sep="")
                clear(0.3)
                planet[line][pos] = "H"
                display_planet = "".join(j for i in planet for j in i)
                write_file(display_planet, output)
            if planet[line][pos] == "#":
                planet[line][pos] = "O"
                display_planet = "".join(j for i in planet for j in i)
                write_file(display_planet, output)
                print(*display_planet, sep="")
                clear(0.3)
                planet[line][pos] = "#"
                display_planet = "".join(j for i in planet for j in i)
                write_file(display_planet, output)
            if planet[line][pos] == " ":
                planet[line][pos] = "O"
                display_planet = "".join(j for i in planet for j in i)
                write_file(display_planet, output)
                print(*display_planet, sep="")
                clear(0.1)
                planet[line][pos] = "*"
                display_planet = "".join(j for i in planet for j in i)
                write_file(display_planet, output)
    for coord in coordinates:
        if coord <= index:
            line, pos = coord
            if planet[line][pos] == "H":
                planet[line][pos] = "O"
                display_planet = "".join(j for i in planet for j in i)
                write_file(display_planet, output)
                print(*display_planet, sep="")
                clear(0.3)
                planet[line][pos] = "H"
                display_planet = "".join(j for i in planet for j in i)
                write_file(display_planet, output)
            if planet[line][pos] == "#":
                planet[line][pos] = "O"
                display_planet = "".join(j for i in planet for j in i)
                write_file(display_planet, output)
                print(*display_planet, sep="")
                clear(0.3)
                planet[line][pos] = "#"
                display_planet = "".join(j for i in planet for j in i)
                write_file(display_planet, output)
            if planet[line][pos] == " ":
                planet[line][pos] = "O"
                display_planet = "".join(j for i in planet for j in i)
                write_file(display_planet, output)
                print(*display_planet, sep="")
                clear(0.1)
                planet[line][pos] = "*"
                display_planet = "".join(j for i in planet for j in i)
                write_file(display_planet, output)
    print(*display_planet, sep="")
