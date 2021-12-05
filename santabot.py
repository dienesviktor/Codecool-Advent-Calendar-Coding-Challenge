def evaluate_actions(file):
    rated_actions = {}
    with open(file, "r") as file:
        lines = file.read().splitlines()
        splitted = [lines[i].split(";") for i in range(1, len(lines))]
        for key in splitted:
            type = key[0]
            action = key[1]
            if type not in rated_actions:
                rated_actions[type] = [action]
            else:
                rated_actions[type].append(action)
    return rated_actions

print(evaluate_actions("karma.csv"))