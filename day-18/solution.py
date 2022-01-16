# Advent of Code 2020
# Day 18

from tree import Tree
from pathlib import Path

# input
with open(Path(__file__).parent / "input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

    inp_standard = [Tree(line, mode="standard") for line in lines]
    inp_advanced = [Tree(line, mode="advanced") for line in lines]

# part 1
# Calculate the sum of all expressions with rules: left to right.


def part_1():
    return sum(inp_standard)


print(f"Part 1: {part_1()}")

# part 2
# Calculate the sum of all expressions with rules: + before *.


def part_2():
    return sum(inp_advanced)


print(f"Part 2: {part_2()}")
