# Advent of Code 2020
# Day 3

import colorama
from termcolor import colored
from typing import List
from pathlib import Path

colorama.init()

# input
with open(Path(__file__).parent / "input.txt") as f:
    inp = [line.strip() for line in f.readlines()]

# generalized
def count_trees(slope: tuple, roadmap: List[str]) -> int:
    """
    Counts trees on path with slope (x,y) on given map.
    """
    PRINT_OUTPUT = True

    x, y = slope

    # prints starting row
    if PRINT_OUTPUT:
        print(f"SLOPE: {slope}")
        print(roadmap[0])

    row_len = len(roadmap[0])
    count = 0
    step = 0
    for i, row in enumerate(roadmap[1:], start=1):
        # line is skipped if it's not divisible by y-slope
        if i % y != 0:
            if PRINT_OUTPUT:
                print(row)
        else:
            step += x
            spot = step % row_len

            if PRINT_OUTPUT:
                print(row[:spot], colored(row[spot], "red"), row[spot + 1 :], sep="")

            count += row[spot] == "#"

    if PRINT_OUTPUT:
        print()
    return count


# part 1
# Find how many trees (#) are on the path 3 to the right, 1 down.


def part_1():
    return count_trees((3, 1), inp)


print(f"Part 1: {part_1()}")

# part 2
# Find how many trees are on slopes 1:1, 3:1, 5:1, 7:1, 1:2. Multiply them together.


def part_2():
    return (
        count_trees((1, 1), inp)
        * count_trees((3, 1), inp)
        * count_trees((5, 1), inp)
        * count_trees((7, 1), inp)
        * count_trees((1, 2), inp)
    )


print(f"Part 2: {part_2()}")
