def evaluate_actions(file):
    """Divide the actions into nice and naughty categories, and returns them in a dictionary."""
    rated_actions = {}
    with open(file, "r") as file:
        lines = file.read().splitlines()
        splitted = [lines[i].split(";") for i in range(1, len(lines))]
        for i in splitted:
            type = i[0]
            action = i[1]
            if type not in rated_actions:
                rated_actions[type] = [action]
            else:
                rated_actions[type].append(action)
    return rated_actions


def calculate_personal_information(file, rated_actions):
    """Return all person's name, personal actions, karma number, and ideal gift categories in a nested list."""
    people = {}
    with open(file, "r") as file:
        lines = file.read().splitlines()
        splitted = [lines[i].split(";") for i in range(1, len(lines))]
        for i in splitted:
            name = i[0]
            actions = i[1].split(",")
            gift = i[2]
            if name not in people:
                people[name] = [actions]
            else:
                people[name].append(actions)
    nice_actions = rated_actions["nice"]
    naughty_actions = rated_actions["naughty"]
    all_data = []
    for name, actions in people.items():
        karma = 0
        for personal_actions in actions:
            for action in personal_actions:
                if action in nice_actions:
                    karma += 1
                elif action in naughty_actions:
                    karma -= 1
            personal_data = [name, personal_actions, karma, gift.split(",")]
            all_data.append(personal_data)
    return all_data


def main():
    rated_actions = evaluate_actions("karma.csv")
    personal_datas = calculate_personal_information("profiles.csv", rated_actions)


if __name__ == "__main__":
    main()
