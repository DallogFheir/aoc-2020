# Advent of Code 2020
# Day 21

import allergens
from pathlib import Path

# input
with open(Path(__file__).parent / "input.txt") as f:
    foods_lst, ing_set = allergens.parse_foods(f)
algs = allergens.map_allergens_to_ingredients(foods_lst)

# part 1
# Find how many ingredients can't possibly contain any allergen.


def part_1():
    ings_wo_algrs = allergens.find_ingredients_without_allergens(algs, ing_set)

    return allergens.count_ingredients(foods_lst, ings_wo_algrs)


print(f"Part 1: {part_1()}")

# part 2
# Make a list of ingredients with allergens sorted alphabetically by allergen.


def part_2():
    alg_map = allergens.determine_allergens(algs)

    return allergens.make_canonical_ingredient_list(alg_map)


print(f"Part 2: {part_2()}")
