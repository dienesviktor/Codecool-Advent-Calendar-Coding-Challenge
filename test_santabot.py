from santabot import divide_actions, return_data, save_data, unwrapping_gifts, select_gifts, save_data2


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
