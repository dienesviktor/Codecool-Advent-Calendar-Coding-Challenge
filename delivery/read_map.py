def read_map(file="data_files/planet.map"):
    with open(file, 'r') as map:
        coordinates = []
        for line_num, line in enumerate(map):
            for pos_num, pos in enumerate(line):
                coordinates.append((line_num, pos_num))
        return coordinates
