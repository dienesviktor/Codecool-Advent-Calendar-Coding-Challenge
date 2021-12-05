def main():
    from divide_actions import divide_actions as actions
    from return_data import return_data as data
    from save_data import save_data

    actions = actions()
    data = data(actions)
    save_data(data)


if __name__ == "__main__":
    main()
