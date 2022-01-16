import unittest
from jolt_chain import JoltChain

class TestJoltChain(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        inputs = []
        for i in range(1,3):
            with open(f"tests/test_input_{i}.txt") as f:
                inputs.append(JoltChain.from_file(f))

        cls.inputs = inputs

    def test_device_joltage(self):
        self.assertEqual(self.inputs[0].device_joltage,
        22)

    def test_adapter_sequence(self):
        self.assertEqual(self.inputs[0].adapter_sequence,
        [0, 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, 22])

    def test_joltage_diff_sequence(self):
        self.assertEqual(self.inputs[0].joltage_diff_sequence,
        [1, 3, 1, 1, 1, 3, 1, 1, 3, 1, 3, 3])

    def test_joltage_diffs(self):
        self.assertEqual(self.inputs[0].joltage_diffs,
        {1 : 7, 3: 5})

        self.assertEqual(self.inputs[1].joltage_diffs,
        {1 : 22, 3 : 10})

    def test_charging_outlet(self):
        self.assertEqual(self.inputs[0].charging_outlet,
        0)

        self.assertEqual(self.inputs[1].charging_outlet,
        0)

    def test_calculate_combinations(self):
        self.assertEqual(self.inputs[0].calculate_combinations(),
        8)

        self.assertEqual(self.inputs[1].calculate_combinations(),
        19208)