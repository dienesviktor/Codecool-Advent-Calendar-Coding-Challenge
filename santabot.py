from divide_actions import divide_actions
from return_data import return_data
from save_data import save_data
from unwrapping_gifts import unwrapping_gifts
from select_gifts import select_gifts
from save_data2 import save_data2

actions = divide_actions()
challenge_1 = return_data(actions)
save_data(challenge_1)

gifts = unwrapping_gifts()
challenge_2 = select_gifts(gifts)
save_data2(challenge_2)
