# Advent of Code 2020
# Day 14

import re
from collections import namedtuple
from itertools import product
from pathlib import Path

# input
with open(Path(__file__).parent / "input.txt") as f:
    inp = [line.strip() for line in f.readlines()]

mask_pattern = re.compile(r"mask = (.*)")
cmd_pattern = re.compile(r"mem\[(\d+)\] = (\d+)")

instructions = {}
cmd = namedtuple("command", ["address", "value"])
for ins in inp:
    mask_match = mask_pattern.match(ins)
    if mask_match:
        mask = mask_match.group(1)
        instructions[mask] = []

    cmd_match = cmd_pattern.match(ins)
    if cmd_match:
        address, value = cmd_match.groups()
        instructions[mask].append(cmd(int(address), int(value)))

# part 1
# Sum all the values in memory after the program executes.


def part_1():
    memory = {}

    for mask, cmds in instructions.items():
        for cmd in cmds:
            # turn decimal integer to binary 36-bit integer
            bin_value = bin(cmd.value)[2:].zfill(36)

            masked_value = ""
            for mask_digit, value_digit in zip(mask, bin_value):
                # digit from mask if not X
                # if X digit from value
                masked_value += value_digit if mask_digit == "X" else mask_digit

            memory[cmd.address] = int(masked_value, 2)

    # sums values from memory
    return sum(memory.values())


print(f"Part 1: {part_1()}")

# part 2
# Same but the bitmask masks the memory address.


def part_2():
    memory = {}

    for mask, cmds in instructions.items():
        for cmd in cmds:
            # turns address to binary 36-bit integer
            bin_address = bin(cmd.address)[2:].zfill(36)

            masked_address = ""
            for mask_digit, address_digit in zip(mask, bin_address):
                # digit from address if mask digit is 0
                # else 1 from mask digit or floating X
                masked_address += address_digit if mask_digit == "0" else mask_digit

            # creates all possible combos of 0/1s
            floating_digits = masked_address.count("X")
            combos = product((0, 1), repeat=floating_digits)

            for combo in combos:
                address = masked_address
                # replaces all X with 0/1s
                for digit in combo:
                    address = address.replace("X", str(digit), 1)

                address_int = int(address)

                memory[address_int] = cmd.value

    # sums values from memory
    return sum(memory.values())


print(f"Part 2: {part_2()}")
