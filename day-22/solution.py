# Advent of Code 2020
# Day 22

from combat import Combat, RecursiveCombat
from pathlib import Path

# input
with open(Path(__file__).parent / "input.txt") as f:
    game = Combat.parse_from_file(f)
    f.seek(0)
    recursive_game = RecursiveCombat.parse_from_file(f)

# part 1
# Calculate the winning player's score.


def part_1():
    end = game.play()

    return end.score


print(f"Part 1: {part_1()}")

# part 2
# Calculate the winning player's score in a recursive game.


def part_2():
    end = recursive_game.play()

    return end.score


print(f"Part 2: {part_2()}")
