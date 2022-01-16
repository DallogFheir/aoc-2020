from collections import Counter
import functools

class JoltChain:
    charging_outlet = 0

    def __init__(self,adapters):
        adapters.sort()
        self.device_joltage = adapters[-1]+3
        self.adapter_sequence = [0, *adapters, self.device_joltage]

        self.joltage_diff_sequence = [
            self.adapter_sequence[i]-self.adapter_sequence[i-1]
            for i in range(1,len(self.adapter_sequence))
            ]

        self.joltage_diffs = dict(Counter(self.joltage_diff_sequence))

    def calculate_combinations(self):
        return self.calculate_sequence(tuple(self.adapter_sequence))

    @functools.lru_cache
    def calculate_sequence(self,tup):
        # tuple to be able to use cache
        # the ways to reach last item =
        # the ways to reach last 3 items if they're less than 3 distance from last item
        previous = tup[-4:-1]

        if len(previous) in (0,1):
            return 1
        else:
            sum_ = 0

            for i, e in enumerate(previous,start=-len(previous)):
                sum_ += 0 if e+3<tup[-1] else self.calculate_sequence(tup[:i])

            return sum_
    
    @classmethod
    def from_file(cls,f):
        adapters = [int(line) for line in f.readlines()]

        return cls(adapters)
