# Advent of Code 2020
# Day 16

from ticket_parser import *
from functools import reduce
from pathlib import Path

# input
with open(Path(__file__).parent / "input.txt") as f:
    rules, your_ticket, nearby_tickets = parse_tickets(f)

# part 1
# Find values in nearby tickets that do not satisfy any rule.


def part_1():
    return sum(find_invalid_values(rules, nearby_tickets))


print(f"Part 1: {part_1()}")

# part 2
# Determine which field is which, and multiply the 6 values in the fields starting with the word "departure".


def part_2():
    tickets = translate_tickets_to_excluded_fields(
        rules, [your_ticket] + sieve_out_invalid_tickets(rules, nearby_tickets)
    )

    fields = find_fields(rules, tickets)

    return reduce(
        lambda x, y: x * y,
        (
            your_ticket[i]
            for i, field in enumerate(fields)
            if field.startswith("departure")
        ),
    )


print(f"Part 2: {part_2()}")
