# Advent of Code 2020
# Day 17

from cubes import cycle

# input
inp = """.#######
#######.
###.###.
#....###
.#..##..
#.#.###.
###..###
.#.#.##.
""".split(
    "\n"
)

# part 1
# Find how many active cubes there are after 6 cycles.


def part_1():
    return len(cycle(inp, 3, 6))


print(f"Part 1: {part_1()}")

# part 2
# Find how many active cubes there are after 6 cycles in 4 dimensions.


def part_2():
    return len(cycle(inp, 4, 6))


print(f"Part 2: {part_2()}")
