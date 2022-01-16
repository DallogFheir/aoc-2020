from cups import *

test_input = [int(i) for i in list("389125467")]

# for 10 moves
game = game_of_cups(test_input,10)

assert collect_result(game)=="92658374"

# for 100 moves
game = game_of_cups(test_input,100)

assert collect_result(game)=="67384529"

# for translated 10 000 000 moves
import time
start = time.perf_counter()
game = hyper_game_of_cups(test_input)
end = time.perf_counter()
print(str(end-start))

assert hyper_collect_result(game)==149245887792
