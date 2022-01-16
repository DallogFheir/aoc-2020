# Advent of Code 2020
# Day 20

from tiles import ImageAssembler
from pathlib import Path

# input
with open(Path(__file__).parent / "input.txt") as f:
    image = ImageAssembler(f)

# part 1
# Multiply the IDs of the corner tiles.


def part_1():
    product = 1

    for corner in image.corners:
        product *= corner.id

    return product


print(f"Part 1: {part_1()}")

# part 2
# Find how many # are not a part of a sea monster.


def part_2():
    monsters = image.find_monsters()

    return monsters.roughness


print(f"Part 2: {part_2()}")
