# Advent of Code 2020
# Day 23

from cups import *

# input
inp = [int(i) for i in list("598162734")]

# part 1
# Calculate the sequence of cups after 100 moves.


def part_1():
    game = game_of_cups(inp, 100)

    return collect_result(game)


print(f"Part 1: {part_1()}")

# part 2
# Calculate the sequence of 1 000 000 cups after 10 000 000 moves.


def part_2():
    game = hyper_game_of_cups(inp)

    return hyper_collect_result(game)


print(f"Part 2: {part_2()}")
