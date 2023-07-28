# Advent of Code 2020
# Day 6

from customs import CustomsForm
from pathlib import Path

# input
with open(Path(__file__).parent / "input.txt") as f:
    inp = CustomsForm.parse_forms(f)

# part 1
# Find how many questions were answered in total.


def part_1():
    return sum(len(form.questions_anyone_answered) for form in inp)


print(f"Part 1: {part_1()}")

# part 2
# Find how many questions were answered by everyone in group.


def part_2():
    return sum(len(form.questions_everyone_answered) for form in inp)


print(f"Part 2: {part_2()}")
