# Advent of Code 2020
# Day 4

from passport import Passport
from pathlib import Path

# input
with open(Path(__file__).parent / "input.txt") as f:
    inp = Passport.parse_passports(f.read())

# part 1
# Check how many passports contain all required fields.


def part_1():
    return sum(passport.validate_fields() for passport in inp)


print(f"Part 1: {part_1()}")

# part 2
# Check how many passports contain all required fields with valid data.


def part_2():
    return sum(passport.validate() for passport in inp)


print(f"Part 2: {part_2()}")
