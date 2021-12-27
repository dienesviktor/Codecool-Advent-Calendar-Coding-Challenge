def read_map(file="data_files/planet.map"):
    positions = {}
    with open(file, 'r') as map:
        for line_num, line in enumerate(map, start=1):
            for cell_pos, cell in enumerate(line, start=1):
                if cell == "H":
                    positions[(line_num, cell_pos)] = "HEADQUARTER"
                elif cell == "#":
                    positions[(line_num, cell_pos)] = "HOME"
                else:
                    pass
    return positions