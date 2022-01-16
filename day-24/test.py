from tile_flipper import TileFlipper

with open("test_input.txt") as f:
    flipper = TileFlipper.from_file(f)

res = flipper.flip()
assert len(res)==10

switching_floor = flipper.switch_tiles()
ten_days = [10, 15, 12, 25, 14, 23, 28, 41, 37, 49, 37]
for i in range(11):
    assert ten_days[i]==len(next(switching_floor))

switching_floor = flipper.switch_tiles()
dict_100_days = {20: 132, 30: 259, 40: 406, 50: 566, 60: 788, 70: 1106, 80: 1373, 90: 1844, 100: 2208}
res_100_days = [next(switching_floor) for _ in range(101)]
for day, expected_res in dict_100_days.items():
    assert len(res_100_days[day])==expected_res
