# Advent of Code 2020
# Day 2

from pathlib import Path

# input
with open(Path(__file__).parent / "input.txt") as f:
    inp = f.readlines()

# part 1
# Find how many passwords are valid according to the policy of at_least-at_most char : password.
import re


def part_1():
    count = 0
    for pwd_policy in inp:
        min_, max_, char, pwd = re.match(
            r"(\d+)-(\d+) ([a-z]): (.*)", pwd_policy
        ).groups()

        if int(min_) <= pwd.count(char) <= int(max_):
            count += 1

    return count


print(f"Part 1: {part_1()}")

# part 2
# Find how many passwords are valid according to the policy of index_1-index_2 char : password (passwords have to have the given character at index_1 or index_2, but not both or neither; index is first-based).


def part_2():
    count = 0
    for pwd_policy in inp:
        index_1, index_2, char, pwd = re.match(
            r"(\d+)-(\d+) ([a-z]): (.*)", pwd_policy
        ).groups()

        count += (pwd[int(index_1) - 1] == char) != (pwd[int(index_2) - 1] == char)

    return count


print(f"Part 2: {part_2()}")
