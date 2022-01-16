# Advent of Code 2020
# Day 13

from collections import namedtuple
from pathlib import Path


Bus = namedtuple("Bus", ["id", "wait_time"])


def yield_depart_times(id):
    start = 0

    while True:
        yield start
        start += id


# input
with open(Path(__file__).parent / "input.txt") as f:
    timestamp = int(f.readline().strip())

    buses = [
        Bus(int(id), waittime)
        for waittime, id in enumerate(f.readline().strip().split(","))
        if id != "x"
    ]

# part 1
# Find the bus that departs the soonest.


def part_1():
    depart_times = {}

    for bus in buses:
        bus_depart_times = yield_depart_times(bus.id)

        for bus_depart_time in bus_depart_times:
            if bus_depart_time >= timestamp:
                depart_times[bus.id] = bus_depart_time - timestamp
                break

    depart_times = {
        k: depart_times[k] for k in sorted(depart_times, key=lambda k: depart_times[k])
    }

    soonest_id = list(depart_times.keys())[0]
    soonest_time = depart_times[soonest_id]

    return soonest_id * soonest_time


print(f"Part 1: {part_1()}")

# part 2
# Find the earliest timestamp where bus at index 0 departs, bus at index 1 departs 1 minute after, bus at index 2 departs 2 minutes after, etc.


def part_2():
    # Chinese reminder theorem
    # for bus 7 departing at 0, bus 13 departing at 1, etc.
    # if
    # x ≡ ((7 - 0 mod 7) mod 7) mod 7
    # x ≡ ((13 - 1 mod 13) mod 13) mod 13
    # x ≡ ((id - waittime % id) % id) mod id
    # therefore x%id == ((id - waittime % id) % id)
    # etc.
    # then x ≡ y (mod 7*13*...)
    # so solution is in range 7*13*...

    Congruence = namedtuple("Congruence", ["remainder", "mod"])

    bus_lst = [
        Congruence((bus.id - bus.wait_time % bus.id) % bus.id, bus.id) for bus in buses
    ]
    prev = bus_lst.pop(0)
    i = 0

    while True:
        # how it works:
        # https://www.reddit.com/r/adventofcode/comments/kcl7d2/2020_day_13_part_2_buses_in_a_slot_machine/
        if (
            i % prev.mod == prev.remainder
            and i % bus_lst[0].mod == bus_lst[0].remainder
        ):
            new_mod = prev.mod * bus_lst.pop(0).mod

            if not bus_lst:
                return i

            prev = Congruence(i % new_mod, new_mod)

        i += prev.mod


print(f"Part 2: {part_2()}")
