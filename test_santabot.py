from santabot import divide_actions, return_data, save_data


def test_divide_actions():
    assert divide_actions("test_files/test_karma.csv") == {"nice": ["helped a friend"], "naughty": ["is always late"]}


def test_return_data():
    actions = divide_actions("test_files/test_karma.csv")
    assert return_data(actions, file="test_files/test_profiles.csv") == [['Olivia', ['helped a friend'], 1, ['wellness']], ['Liam', ['is always late'], -1, ['wellness']]]


def test_save_data():
    actions = divide_actions("test_files/test_karma.csv")
    data = return_data(actions, file="test_files/test_profiles.csv")
    save_data(data, file="test_files/test_challenge-1.csv")
    with open("test_files/test_challenge-1.csv", "r") as file:
        content = file.readlines()
        assert content == ["Olivia, ['helped a friend'], 1, ['wellness']\n", "Liam, ['is always late'], -1, ['wellness']\n"]
