def save_data(data, file="data_files/challenge-1.csv"):
    """Save personal datas into a CSV file."""
    with open(file, "w") as file:
        file.write("name;actions;karma;ideal present categories"+"\n")
        for person in data:
            line = f"{person[0]};{person[1]};{person[2]};{person[3]}"
            file.writelines(line+"\n")
