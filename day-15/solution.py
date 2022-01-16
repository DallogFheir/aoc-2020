# Advent of Code 2020
# Day 15

from memory_game import yield_nums
import itertools

# input
inp = [16, 1, 0, 18, 12, 14, 19]

# part 1
# What will be the 2020th number spoken?


def part_1():
    game = yield_nums(inp)

    return next(itertools.islice(game, 2020 - 1, None))


print(f"Part 1: {part_1()}")

# part 2
# What will be the 30_000_000th number spoken?


def part_2():
    game = yield_nums(inp)

    return next(itertools.islice(game, 30_000_000 - 1, None))


print(f"Part 2: {part_2()}")
