def select_gifts(gifts, file="data_files/challenge-1.csv"):
    data = []
    with open(file, "r") as file:
        lines = file.read().splitlines()
        splitted = [lines[i].split(";") for i in range(1, len(lines))]
        for person in splitted:
            name = person[0]
            actions = person[1]
            karma = person[2]
            ideal_present_categories = person[3]
            categories = ideal_present_categories.split(",")
            presents = [gifts[i][1].split(",") for i in range(0, len(gifts)-1) if categories[0] == gifts[i][0] or categories[1] == gifts[i][0]]
            for i in range(1):
                if int(karma) < 0:
                    data.append([name, actions, karma, ideal_present_categories, "one pieace of coal"])
                    break
                elif int(karma) >= 0 and int(karma) < 7:
                    for i in range(1):
                        data.append([name, actions, karma, ideal_present_categories, presents[0][0]])
                        break
                else:
                    for i in range(1):
                        pres = [presents[0][0], presents[1][0]]
                        presents = ",".join(pres)
                        data.append([name, actions, karma, ideal_present_categories, presents])
                        break
    return data
