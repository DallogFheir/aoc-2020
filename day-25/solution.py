# Advent of Code 2020
# Day 25

from handshake import *

# input
card_key = 8335663
door_key = 8614349

# part 1
# Calculate the encryption key.


def part_1():
    card_loop_size = find_loop_size(card_key)
    door_loop_size = find_loop_size(door_key)

    encryption_key_from_card = create_key(card_loop_size, door_key)
    encryption_key_from_door = create_key(door_loop_size, card_key)

    assert encryption_key_from_card == encryption_key_from_door

    return encryption_key_from_door


print(f"Part 1: {part_1()}")
