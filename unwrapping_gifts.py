def unwrapping_gifts(file="data_files/presents.csv"):
    with open(file, "r") as file:
        lines = file.read().splitlines()
        gifts = [lines[i].split(";") for i in range(1, len(lines))]
    return gifts