karma = {}

with open("karma.csv", "r") as file:
    lines = file.read().splitlines()
    splitted = [lines[i].split(";") for i in range(1, len(lines))]
    
    for key in splitted:
        type = key[0]
        action = key[1]
        if type not in karma:
            karma[type] = [action]
        else:
            karma[type].append(action)