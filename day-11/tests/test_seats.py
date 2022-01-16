import unittest
import inspect
from seats import SeatLayout

class TestSeatIterator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open("tests/test_data/part_1/iteration_0.txt") as f:
            cls.input = SeatLayout.from_file(f)

    def test_get_adjacent_neighbors(self):
        # top left
        self.assertEqual(
            self.input.get_adjacent_neighbors(0,0),
            [(0,1), (1,0), (1,1)]
        )
        # top
        self.assertEqual(
            self.input.get_adjacent_neighbors(0,4),
            [(0,3), (0,5), (1,3), (1,4), (1,5)]
        )
        # top right
        self.assertEqual(
            self.input.get_adjacent_neighbors(0,9),
            [(0,8), (1,8), (1,9)]
        )
        # left
        self.assertEqual(
            self.input.get_adjacent_neighbors(7,0),
            [(6,0), (6,1), (7,1), (8,0), (8,1)]
        )
        # bottom left
        self.assertEqual(
            self.input.get_adjacent_neighbors(9,0),
            [(8,0), (8,1), (9,1)]
        )
        # bottom
        self.assertEqual(
            self.input.get_adjacent_neighbors(9,4),
            [(8,3), (8,4), (8,5), (9,3), (9,5)]
        )
        # bottom right
        self.assertEqual(
            self.input.get_adjacent_neighbors(9,9),
            [(8,8), (8,9), (9,8)]
        )
        # right
        self.assertEqual(
            self.input.get_adjacent_neighbors(6,9),
            [(5,8), (5,9), (6,8), (7,8), (7,9)]
        )
        # center
        self.assertEqual(
            self.input.get_adjacent_neighbors(5,5),
            [(4,4), (4,5), (4,6), (5,4), (5,6), (6,4), (6,5), (6,6)]
        )

    def test_get_cardinal_neighbors(self):
        # top left
        self.assertEqual(
            self.input.get_cardinal_neighbors(0,0),
            [(0,2), (1,0), (1,1)]
        )
        # top
        self.assertEqual(
            self.input.get_cardinal_neighbors(0,4),
            [(0,3), (0,5), (1,3), (1,4), (1,5)]
        )
        # top right
        self.assertEqual(
            self.input.get_cardinal_neighbors(0,9),
            [(0,8), (1,8), (1,9)]
        )
        # left
        self.assertEqual(
            self.input.get_cardinal_neighbors(7,0),
            [(5,0), (5,2), (7,1), (8,0), (9,2)]
        )
        # bottom left
        self.assertEqual(
            self.input.get_cardinal_neighbors(9,0),
            [(8,0), (7,2), (9,2)]
        )
        # bottom
        self.assertEqual(
            self.input.get_cardinal_neighbors(9,4),
            [(8,3), (8,4), (8,5), (9,3), (9,5)]
        )
        # bottom right
        self.assertEqual(
            self.input.get_cardinal_neighbors(9,9),
            [(7,7), (8,9), (9,8)]
        )
        # right
        self.assertEqual(
            self.input.get_cardinal_neighbors(6,9),
            [(5,8), (5,9), (6,4), (7,8), (7,9)]
        )
        # center
        self.assertEqual(
            self.input.get_cardinal_neighbors(5,5),
            [(3,3), (4,5), (4,6), (5,4), (5,6), (6,4), (7,5), (7,7)]
        )

    def test_get_seat_states(self):
        # top left
        self.assertEqual(
            self.input.get_seat_states([(0,1), (1,0), (1,1)]),
            {(0,1) : ".", (1,0) : "L", (1,1) : "L"}
        )
        # top
        self.assertEqual(
            self.input.get_seat_states([(0,3), (0,5), (1,3), (1,4), (1,5)]),
            {(0,3) : "L", (0,5) : "L", (1,3) : "L", (1,4) : "L", (1,5) : "L"}
        )
        # top right
        self.assertEqual(
            self.input.get_seat_states([(0,8), (1,8), (1,9)]),
            {(0,8) : "L", (1,8) : "L", (1,9) : "L"}
        )
        # left
        self.assertEqual(
            self.input.get_seat_states([(6,0), (6,1), (7,1), (8,0), (8,1)]),
            {(6,0) : ".", (6,1) : ".", (7,1) : "L", (8,0) : "L", (8,1) : "."}
        )
        # bottom left
        self.assertEqual(
            self.input.get_seat_states([(8,0), (8,1), (9,1)]),
            {(8,0) : "L", (8,1) : ".", (9,1) : "."}
        )
        # bottom
        self.assertEqual(
            self.input.get_seat_states([(8,3), (8,4), (8,5), (9,3), (9,5)]),
            {(8,3) : "L", (8,4) : "L", (8,5) : "L", (9,3) : "L", (9,5) : "L"}
        )
        # bottom right
        self.assertEqual(
            self.input.get_seat_states([(8,8), (8,9), (9,8)]),
            {(8,8) : ".", (8,9) : "L", (9,8) : "L"}
        )
        # right
        self.assertEqual(
            self.input.get_seat_states([(5,8), (5,9), (6,8), (7,8), (7,9)]),
            {(5,8) : "L", (5,9) : "L", (6,8) : ".", (7,8) : "L", (7,9) : "L"}
        )
        # center
        self.assertEqual(
            self.input.get_seat_states([(4,4), (4,5), (4,6), (5,4), (5,6), (6,4), (6,5), (6,6)]),
            {(4,4) : ".", (4,5) : "L", (4,6) : "L", (5,4) : "L", (5,6) : "L", (6,4) : "L", (6,5) : ".", (6,6) : "."}
        )

    def test_iteration(self):
        self.input.set_mode("part_1")
        for i, layout in enumerate(self.input):
            if i==0:
                continue

            if i==6:
                break

            with open(f"tests/test_data/part_1/iteration_{i}.txt") as f:
                test_layout = SeatLayout.from_file(f)

                self.assertEqual(layout.grid, test_layout.grid, msg=f"Part 1. Iteration {i}.")

        self.input.set_mode("part_2")
        for i, layout in enumerate(self.input):
            if i==0:
                continue

            if i==7:
                break

            with open(f"tests/test_data/part_2/iteration_{i}.txt") as f:
                test_layout = SeatLayout.from_file(f)

                self.assertEqual(layout.grid, test_layout.grid, msg=f"Part 2. Iteration {i}.")

    def _test_tiles(self,tile):
        # get caller function's name, removes "test_"
        func_name = inspect.stack()[1][3].removeprefix("test_")

        for mode, limit in [("part_1", 6), ("part_2", 7)]:
            self.input.set_mode(mode)
            for i, layout in enumerate(self.input):
                if i==limit:
                    break

                with open(f"tests/test_data/{mode}/iteration_{i}.txt") as f:
                    seat_count = f.read().count(tile)

                    self.assertEqual(getattr(layout,func_name), seat_count)

    def test_empty_seats(self):
        self._test_tiles("L")

    def test_occupied_seats(self):
        self._test_tiles("#")

    def test_floor_tiles(self):
        self._test_tiles(".")

    def test_final_state(self):
        with open("tests/test_data/part_1/iteration_5.txt") as f:
            final_state_1 = SeatLayout.from_file(f)

        self.input.set_mode("part_1")

        self.assertEqual(self.input.final_state.grid, final_state_1.grid)
        self.assertEqual(self.input.final_state.occupied_seats,37)

        with open("tests/test_data/part_2/iteration_6.txt") as f:
            final_state_2= SeatLayout.from_file(f)

        self.input.set_mode("part_2")

        self.assertEqual(self.input.final_state.grid, final_state_2.grid)
        self.assertEqual(self.input.final_state.occupied_seats,26)

    def test_last_iteration(self):
        self.input.set_mode("part_1")
        self.assertEqual(self.input.last_iteration,5)
        self.input.set_mode("part_2")
        self.assertEqual(self.input.last_iteration,6)

    def test_size(self):
        self.assertEqual(self.input.size, (10,10))
