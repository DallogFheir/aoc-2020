# Advent of Code 2020
# Day 8

from handheld_console import HandheldConsole
from pathlib import Path

# input
with open(Path(__file__).parent / "input.txt") as f:
    inp = HandheldConsole.from_file(f)

# part 1
# Find the value of accumulator before any instruction is repeated.


def part_1():
    inp.execute()
    return inp.accumulator


print(f"Part 1: {part_1()}")

# part 2
# Fix the console by replacing one JMP command with NOP or vice versa.


def part_2():
    inp.fix()
    return inp.accumulator


print(f"Part 2: {part_2()}")
