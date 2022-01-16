def yield_nums(starting_nums):
    already_spoken = {}
    turn = 1

    for num in starting_nums:
        already_spoken[num] = turn
        turn += 1
        yield num

    prev = 0
    yield 0

    while True:
        new_prev = turn - already_spoken[prev] if prev in already_spoken else 0
        already_spoken[prev] = turn
        prev = new_prev
        turn += 1

        yield prev

# test
if __name__=="__main__":
    import itertools

    game = yield_nums([0,3,6])
    nums = [0,3,6,0,3,3,1,0,4,0]
    for num in nums:
        assert next(game)==num

    game = yield_nums([0,3,6])
    assert next(itertools.islice(game,2020-1,None))==436

    nums = {
        (0,3,6) : 175594,
        (1,3,2) : 2578,
        (2,1,3) : 3544142,
        (1,2,3) : 261214,
        (2,3,1) : 6895259,
        (3,2,1) : 18,
        (3,1,2) : 362
    }
    for num, res in nums.items():
        game = yield_nums(num)
        assert next(itertools.islice(game,30_000_000-1,None))==res
