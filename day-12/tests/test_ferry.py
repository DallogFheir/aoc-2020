import unittest
from ferry import Ferry, DirectionalFerry, WaypointFerry

class TestFerry(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open("tests/test_input.txt") as f:
            cls.input = Ferry.from_file(f)

    def test_add_coords(self):
        self.assertEqual(
            Ferry.add_coords((1,0),(1,1)),
            (2,1)
        )
        self.assertEqual(
            Ferry.add_coords((33,20),(-15,-1)),
            (18,19)
        )
        self.assertEqual(
            Ferry.add_coords((-2,0),(-10,-10)),
            (-12,-10)
        )

class TestDirectionalFerry(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open("tests/test_input.txt") as f:
            cls.input = DirectionalFerry.from_file(f)

    def test_change_dir(self):
        self.input.cur_dir = "E"

        self.input.change_dir(90)
        self.assertEqual(self.input.cur_dir, "S")

        self.input.change_dir(90)
        self.assertEqual(self.input.cur_dir, "W")

        self.input.change_dir(90)
        self.assertEqual(self.input.cur_dir, "N")

        self.input.change_dir(90)
        self.assertEqual(self.input.cur_dir, "E")

        self.input.change_dir(-90)
        self.assertEqual(self.input.cur_dir, "N")

        self.input.change_dir(180)
        self.assertEqual(self.input.cur_dir, "S")

        self.input.cur_dir = "E"

    def test_move_ferry(self):
        self.input.move_ferry()

        self.assertEqual(
            self.input.path,
            [(0,0), (10,0), (10,3), (17,3), (17,-8)]
        )

    def test_manhattan_dst(self):
        self.input.move_ferry()
        
        self.assertEqual(self.input.manhattan_dst, 25)

    def test_map_size(self):
        self.input.move_ferry()
        
        self.assertEqual(self.input.map_size, (17,11))

class TestWaypointFerry(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open("tests/test_input.txt") as f:
            cls.input = WaypointFerry.from_file(f)

    def test_move_ferry(self):
        self.input.move_ferry()

        self.assertEqual(
            self.input.path,
            [
                ((0,0), (10,1)),
                ((100,10), (10,1)),
                ((100,10), (10,4)),
                ((170,38), (10,4)),
                ((170,38), (4,-10)),
                ((214,-72), (4,-10))
            ]
        )

    def test_rotate_waypoint(self):
        self.assertEqual(
            WaypointFerry.rotate_waypoint((10,4),90,"clockwise"),
            (4,-10)
        )

        self.assertEqual(
            WaypointFerry.rotate_waypoint((10,4),180,"clockwise"),
            (-10,-4)
        )

        self.assertEqual(
            WaypointFerry.rotate_waypoint((2,3),270,"counterclockwise"),
            (3,-2)
        )

    def test_manhattan_dst(self):
        self.input.move_ferry()
        
        self.assertEqual(self.input.manhattan_dst, 286)

    def test_map_size(self):
        self.input.move_ferry()

        self.assertEqual(self.input.map_size, (214,110))
