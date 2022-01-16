# Advent of Code 2020
# Day 1

from pathlib import Path

# input
with open(Path(__file__).parent / "input.txt") as f:
    inp = [int(n) for n in f.readlines()]

# part 1
# Find 2 numbers that sum up to 2020 and return their product.


def part_1():
    for i, m in enumerate(inp):
        n = 2020 - m

        if n in inp[i + 1 :]:
            return m * n


print(f"Part 1: {part_1()}")

# part 2
# Find 3 numbers that sum up to 2020 and return their product.


def part_2():
    for i, m in enumerate(inp):
        for j, n in enumerate(inp[i + 1 :]):
            k = 2020 - m - n

            if k in inp[i + j + 2 :]:
                return m * n * k


print(f"Part 2: {part_2()}")