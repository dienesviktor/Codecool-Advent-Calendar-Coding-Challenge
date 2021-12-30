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
            for position in lines:
                line.append(position)
            planet.append(line)
    for line_num, line in enumerate(display_planet):
        for pos_num, position in enumerate(line):
            if position == "H":
                index = (line_num, pos_num)
    for coordinate in coordinates:
        if coordinate >= index:
            line, position = coordinate
            if planet[line][position] == "H":
                planet[line][position] = "O"
                display_planet = "".join(cell for line in planet for cell in line)
                write_file(display_planet, output)
                print(*display_planet, sep="")
                clear(0.3)
                planet[line][position] = "H"
                display_planet = "".join(cell for line in planet for cell in line)
                write_file(display_planet, output)
            if planet[line][position] == "#":
                planet[line][position] = "O"
                display_planet = "".join(cell for line in planet for cell in line)
                write_file(display_planet, output)
                print(*display_planet, sep="")
                clear(0.3)
                planet[line][position] = "#"
                display_planet = "".join(cell for line in planet for cell in line)
                write_file(display_planet, output)
            if planet[line][position] == " ":
                planet[line][position] = "O"
                display_planet = "".join(cell for line in planet for cell in line)
                write_file(display_planet, output)
                print(*display_planet, sep="")
                clear(0.1)
                planet[line][position] = "*"
                display_planet = "".join(cell for line in planet for cell in line)
                write_file(display_planet, output)
    for coordinate in coordinates:
        if coordinate <= index:
            line, position = coordinate
            if planet[line][position] == "H":
                planet[line][position] = "O"
                display_planet = "".join(cell for line in planet for cell in line)
                write_file(display_planet, output)
                print(*display_planet, sep="")
                clear(0.3)
                planet[line][position] = "H"
                display_planet = "".join(cell for line in planet for cell in line)
                write_file(display_planet, output)
            if planet[line][position] == "#":
                planet[line][position] = "O"
                display_planet = "".join(cell for line in planet for cell in line)
                write_file(display_planet, output)
                print(*display_planet, sep="")
                clear(0.3)
                planet[line][position] = "#"
                display_planet = "".join(cell for line in planet for cell in line)
                write_file(display_planet, output)
            if planet[line][position] == " ":
                planet[line][position] = "O"
                display_planet = "".join(cell for line in planet for cell in line)
                write_file(display_planet, output)
                print(*display_planet, sep="")
                clear(0.1)
                planet[line][position] = "*"
                display_planet = "".join(cell for line in planet for cell in line)
                write_file(display_planet, output)
    print(*display_planet, sep="")
