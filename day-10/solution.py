# Advent of Code 2020
# Day 10

from jolt_chain import JoltChain
from pathlib import Path

# input
with open(Path(__file__).parent / "input.txt") as f:
    inp = JoltChain.from_file(f)

# part 1
# Find the product of differences of 3 jolts * difference of 1 jolt.


def part_1():
    return inp.joltage_diffs[1] * inp.joltage_diffs[3]


print(f"Part 1: {part_1()}")

# part 2
# Find all possible sequences of adapters.


def part_2():
    return inp.calculate_combinations()


print(f"Part 2: {part_2()}")
