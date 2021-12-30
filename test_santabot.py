from santabot import divide_actions, return_data, save_data, unwrapping_gifts, select_gifts, save_data2, read_map, delivery_gifts


def test_divide_actions():
    assert divide_actions("test_files/test_karma.csv") == {'nice': ['helped a friend', 'takes good care of their pet', 'did volunteer work', 'gave money to a charity', 'helped a stranger', 'loves their family', 'planted a tree', 'helped a grandma to cross the street', 'listened to their partner', 'brought food to their friends', 'kept their home clean', 'used renewable energies', "respected others' opinions", 'bought Christmas presents for orphans', 'donated money to Wikipedia'], 'naughty': ['stole money', 'threw garbage on the street', 'smoked in a restaurant toilet', "didn't silence the cellphone in a cinema", 'lied to a friend', 'likes hawaii pizza', 'got too drunk', 'cut the line', "didn't pay for the public transportation", 'swears a lot', "doesn't respect their parents", "doesn't give tips", "ate someone else's office food from the fridge", 'is always late', 'pees outside the bowl']}


def test_return_data():
    actions = divide_actions("test_files/test_karma.csv")
    assert return_data(actions, file="test_files/test_profiles.csv")[0] == ['Olivia Johnson', "doesn't respect their parents,takes good care of their pet,did volunteer work,didn't pay for the public transportation,lied to a friend,swears a lot,loves their family,is always late,listened to their partner,stole money,cut the line,got too drunk,smoked in a restaurant toilet,respected others' opinions,used renewable energies", -3, 'pets,electronic devices']


def test_save_data():
    actions = divide_actions("test_files/test_karma.csv")
    challenge_1 = return_data(actions, file="test_files/test_profiles.csv")
    save_data(challenge_1, file="test_files/test_challenge-1.csv")
    with open("test_files/test_challenge-1.csv", "r") as file:
        content = file.readlines()
        assert content[1] == "Olivia Johnson;doesn't respect their parents,takes good care of their pet,did volunteer work,didn't pay for the public transportation,lied to a friend,swears a lot,loves their family,is always late,listened to their partner,stole money,cut the line,got too drunk,smoked in a restaurant toilet,respected others' opinions,used renewable energies;-3;pets,electronic devices\n"


def test_unwrapping_gifts():
    assert unwrapping_gifts("test_files/test_presents.csv")[0] == ['sports', 'basket ball,sneakers,dumbbells,fit ball,bicycle,sports bag']


def test_select_gifts():
    gifts = unwrapping_gifts("test_files/test_presents.csv")
    assert select_gifts(gifts, file="data_files/challenge-1.csv")[0] == ['Olivia Johnson', "doesn't respect their parents,takes good care of their pet,did volunteer work,didn't pay for the public transportation,lied to a friend,swears a lot,loves their family,is always late,listened to their partner,stole money,cut the line,got too drunk,smoked in a restaurant toilet,respected others' opinions,used renewable energies", '-3', 'pets,electronic devices', 'one pieace of coal']


def test_save_data_2():
    gifts = unwrapping_gifts("test_files/test_presents.csv")
    challenge_2 = select_gifts(gifts, file="data_files/challenge-1.csv")
    save_data2(challenge_2, file="test_files/test_challenge-2.csv")
    with open("test_files/test_challenge-2.csv", "r") as file:
        content = file.readlines()
        assert content[1] == "Olivia Johnson;doesn't respect their parents,takes good care of their pet,did volunteer work,didn't pay for the public transportation,lied to a friend,swears a lot,loves their family,is always late,listened to their partner,stole money,cut the line,got too drunk,smoked in a restaurant toilet,respected others' opinions,used renewable energies;-3;pets,electronic devices;one pieace of coal\n"


def test_read_map():
    assert read_map(file="test_files/test_planet-small.map") == [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (2, 10), (2, 11), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 10), (3, 11), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (4, 10), (4, 11), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11), (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8), (6, 9), (6, 10), (6, 11), (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (7, 10), (7, 11), (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8), (8, 9), (8, 10), (8, 11), (9, 0), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (9, 10), (9, 11), (10, 0), (10, 1), (10, 2), (10, 3), (10, 4), (10, 5), (10, 6), (10, 7), (10, 8), (10, 9), (10, 10)]


def test_delivery_gifts():
    coordinates = read_map("test_files/test_planet-small.map")
    delivery_gifts(coordinates, "test_files/test_planet-small.map", "test_files/test_challenge-3.frames")
    with open("test_files/test_challenge-3.frames", "r") as file:
        content = file.readlines()
        assert content == ['#****#*****\n', '********#**\n', '***#*******\n', '*#*****#***\n', '*********#*\n', '*#***H*****\n', '******#***#\n', '**#*****#**\n', '****#**#***\n', '*#*******#*\n', '***#***#***']
