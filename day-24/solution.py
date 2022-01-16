# Advent of Code 2020
# Day 24

from tile_flipper import TileFlipper
from pathlib import Path

# input
with open(Path(__file__).parent / "input.txt") as f:
    flipper = TileFlipper.from_file(f)

# part 1
# How many tiles are black after executing instructions?


def part_1():
    return len(flipper.flip())


print(f"Part 1: {part_1()}")

# part 2
# How many tiles are black after 100 days of switching?


def part_2():
    floor = flipper.switch_tiles()

    for _ in range(101):
        res = next(floor)

    return len(res)


print(f"Part 2: {part_2()}")
