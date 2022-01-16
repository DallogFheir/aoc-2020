# Advent of Code 2020
# Day 19

import re
from rules import create_regex_str, parse_input
from pathlib import Path

# input
with open(Path(__file__).parent / "input.txt") as f:
    rules, messages = parse_input(f)

# part 1
# Find how many messages are valid.


def part_1():
    regex = create_regex_str(rules)

    return sum(re.fullmatch(regex, msg) is not None for msg in messages)


print(f"Part 1: {part_1()}")

# part 2
# Find how many messages are valid but with recursive rules.
# 8: 42 | 42 8
# 11: 42 31 | 42 11 31


def part_2():
    max_len = len(max(messages, key=len)) // 2

    regex_42_str = create_regex_str(rules, 42)
    regex_31_str = create_regex_str(rules, 31)

    count = 0
    for msg in messages:
        for i in range(1, max_len + 1):
            regex = re.compile(
                regex_42_str
                + "+"
                + regex_42_str
                + "{"
                + str(i)
                + "}"
                + regex_31_str
                + "{"
                + str(i)
                + "}"
            )

            if re.fullmatch(regex, msg):
                count += 1
                break

    return count


print(f"Part 2: {part_2()}")
