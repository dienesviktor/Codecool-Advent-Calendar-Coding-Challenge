def read_map(file="data_files/planet-small.map"):
    with open(file, 'r') as map:
        return [cell for line in map for cell in line]