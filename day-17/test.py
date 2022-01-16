from cubes import *

test_input = [
    ".#.",
    "..#",
    "###"
]

# parse initial state
initial_state_3 = parse_initial_state(test_input,3)
initial_state_4 = parse_initial_state(test_input,4)

assert sorted(initial_state_3)==sorted(
    [(0,2,0), (1,0,0), (1,2,0), (2,1,0), (2,2,0)])
assert sorted(initial_state_4)==sorted(
    [(0,2,0,0), (1,0,0,0), (1,2,0,0), (2,1,0,0), (2,2,0,0)])

# cycle 1
first_cycle = get_next_state(initial_state_3,3)

assert sorted(first_cycle)==sorted([
    (0,1,0), (1,2,0), (1,3,0), (2,1,0), (2,2,0), (0,1,-1), (1,3,-1), (2,2,-1), (0,1,1), (1,3,1), (2,2,1)
])

# active after 6 cycles
cycle_3 = cycle(test_input,3,6)
cycle_4 = cycle(test_input,4,6)

assert len(cycle_3)==112
assert len(cycle_4)==848
