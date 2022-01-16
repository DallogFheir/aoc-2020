# Advent of Code 2020
# Day 12

from ferry import Ferry
from pathlib import Path

# input
with open(Path(__file__).parent / "input.txt") as f:
    inp = Ferry.from_file(f)

# part 1
# Find the Manhattan distance of the end point of the ferry.


def part_1():
    inp_1 = inp.to_directional()
    inp_1.move_ferry()
    return inp_1.manhattan_dst


print(f"Part 1: {part_1()}")

# part 2
# Same but with new rules.


def part_2():
    inp_2 = inp.to_waypoint()
    inp_2.move_ferry()
    return inp_2.manhattan_dst


print(f"Part 2: {part_2()}")
