# Advent of Code 2020
# Day 11

from seats import SeatLayout
from pathlib import Path

# input
with open(Path(__file__).parent / "input.txt") as f:
    inp = SeatLayout.from_file(f)

# part 1
# Find the number of occupied seats when the chaos stabilizes.


def part_1():
    inp.set_mode("part_1")
    return inp.final_state.occupied_seats


print(f"Part 1: {part_1()}")

# part 2
# Same but with different rules.


def part_2():
    inp.set_mode("part_2")
    return inp.final_state.occupied_seats


print(f"Part 2: {part_2()}")
