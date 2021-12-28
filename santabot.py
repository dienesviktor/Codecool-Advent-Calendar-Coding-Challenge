from karma.divide_actions import divide_actions
from karma.return_data import return_data
from karma.save_data import save_data
from ideal_present.unwrapping_gifts import unwrapping_gifts
from ideal_present.select_gifts import select_gifts
from ideal_present.save_data2 import save_data2
from delivery.read_map import read_map
from delivery.delivery_gifts import delivery_gifts


actions = divide_actions()
challenge_1 = return_data(actions)
save_data(challenge_1)

gifts = unwrapping_gifts()
challenge_2 = select_gifts(gifts)
save_data2(challenge_2)

map = read_map()
delivery_gifts(map)
