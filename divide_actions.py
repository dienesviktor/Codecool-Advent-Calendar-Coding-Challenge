def divide_actions(file="karma.csv"):
    """Divide the actions into nice and naughty categories, and returns them in a dictionary."""
    actions = {}
    with open(file, "r") as file:
        lines = file.read().splitlines()
        splitted = [lines[i].split(";") for i in range(1, len(lines))]
        for i in splitted:
            type = i[0]
            action = i[1]
            if type not in actions:
                actions[type] = [action]
            else:
                actions[type].append(action)
    return actions
