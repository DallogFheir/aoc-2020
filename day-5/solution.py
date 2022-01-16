# Advent of Code 2020
# Day 5

from boarding_pass import BoardingPass
from pathlib import Path

# input
with open(Path(__file__).parent / "input.txt") as f:
    inp = BoardingPass.parse_bpasses(f.read())

# part 1
# Find the highest seat ID.


def part_1():
    return max(b_pass.id for b_pass in inp)


print(f"Part 1: {part_1()}")

# part 2
# Find your seat ID (the only missing one not on edges).


def part_2():
    ids = sorted(b_pass.id for b_pass in inp)
    seat_range = range(ids[0], ids[-1] + 1)

    return tuple(set(seat_range) - set(ids))[0]


print(f"Part 2: {part_2()}")
