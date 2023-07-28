# Advent of Code 2020
# Day 7

import functools
import re
from pathlib import Path

# input
container_template = re.compile(r"(.*?) bags contain")
content_template = re.compile(r" (\d+) (.*?) bag(?:s)?[,.]")


def parse_bag_rules(fh):
    rules_dict = {}

    for line in fh:
        container = re.match(container_template, line).group(1)

        contents = re.findall(content_template, line)

        rules_dict[container] = [(int(num), bag) for num, bag in contents]

    return rules_dict


with open(Path(__file__).parent / "input.txt") as f:
    inp = parse_bag_rules(f)

inp_bags_only = {k: [tup[1] for tup in v] for k, v in inp.items()}

# part 1
# Find how many bags can contain a shiny gold bag.

# check if bag can contain
@functools.lru_cache
def check_if_bag_can_contain(container, target):
    if target in inp_bags_only[container]:
        return True

    for bag in inp_bags_only[container]:
        if check_if_bag_can_contain(bag, target):
            return True

    return False


def part_1():
    return sum(check_if_bag_can_contain(bag, "shiny gold") for bag in inp_bags_only)


print(f"Part 1: {part_1()}")

# part 2
# Find how many bags a shiny gold bag has to contain.

# check how many bags a bag has to contain
def check_how_many_bags_in_a_bag(container):
    content = inp[container]

    if not content:
        return 0

    count = sum(int(num) for num, bag in content)

    for num, bag in content:
        count += num * check_how_many_bags_in_a_bag(bag)

    return count


def part_2():
    return check_how_many_bags_in_a_bag("shiny gold")


print(f"Part 2: {part_2()}")
