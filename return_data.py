def return_data(actions, file="data_files/profiles.csv"):
    """Return all person's name, personal actions, karma number, and ideal gift categories in a nested list."""
    people = {}
    nice_actions = actions["nice"]
    naughty_actions = actions["naughty"]
    data = []
    with open(file, "r") as file:
        lines = file.read().splitlines()
        splitted = [lines[i].split(";") for i in range(1, len(lines))]
        for i in splitted:
            name = i[0]
            actions = i[1].split(",")
            gift = i[2].split(",")
            if name not in people:
                people[name] = [actions]
            else:
                people[name].append(actions)
    for name, actions in people.items():
        karma = 0
        for personal_actions in actions:
            for action in personal_actions:
                if action in nice_actions:
                    karma += 1
                elif action in naughty_actions:
                    karma -= 1
        
        personal_actions_string = ",".join(personal_actions)
        gift_string = ",".join(gift)
        personal_data = [name, personal_actions_string, karma, gift_string]
        data.append(personal_data)
    return data
