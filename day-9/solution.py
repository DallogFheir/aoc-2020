# Advent of Code 2020
# Day 9

from pathlib import Path

# input
with open(Path(__file__).parent / "input.txt") as f:
    inp = [int(line.strip()) for line in f.readlines()]

# part 1
# Find the first number that is not the sum of 2 of the previous 25 numbers.


def part_1():
    cache = []

    # get sum from first 25 numbers
    preamble = inp[:25]
    for i, v in enumerate(preamble):
        sum_lst = [v + e for e in preamble[i + 1 :]]
        cache.append(sum_lst)

    for i, v in enumerate(inp[25:], start=25):
        # add next number to each previous sum list
        # check if current number is a sum anywhere in cache
        is_sum = False

        for ind, sum_lst in enumerate(cache):
            if v in sum_lst:
                is_sum = True

            sum_lst.append(inp[i - 25 + ind] + v)

        # breaks if number is not a sum
        if not is_sum:
            return v

        del cache[0]
        cache.append([])


print(f"Part 1: {part_1()}")

# part 2
# Find a contiguous set of numbers from input that add up to solution from part 1. Add the smallest and largest numbers in that set.


def part_2():
    solution = part_1()

    for i in range(len(inp)):
        for j in range(1, len(inp[i:])):
            subrange = inp[i : i + j]

            # only positive numbers
            # if sum gets bigger than solution, stop loop
            if sum(subrange) > solution:
                break

            if sum(subrange) == solution:
                return min(subrange) + max(subrange)


print(f"Part 2: {part_2()}")
