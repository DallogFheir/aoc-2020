# The boarding agent has called final boarding for your flight, but for some reason, they won't just take you at your word regarding your seat number.

# You'll have to produce a boarding pass if you want to get on the plane. There's a shady character in the terminal who has offered to print you a "totally legit" looking one, if you can provide them with your boarding pass string.

# Given your seat ID, provide the boarding pass string.

from boarding_pass import BoardingPass

# test from here
# https://www.reddit.com/r/adventofcode/comments/k72oom/2020_day_5_part_3_boarding_pass_generator/geoj8s0/?utm_source=reddit&utm_medium=web2x&context=3
def boarding_from_id(seat_id):
    as_bin = f"{seat_id:010b}"
    return as_bin[:7].replace("1", "B").replace("0", "F") + as_bin[7:].replace(
        "1", "R"
    ).replace("0", "L")


#

id = 532
my_solution = BoardingPass(id).bpass_string
test_solution = boarding_from_id(id)
assert my_solution == test_solution

print(f"Extra: {my_solution}")
