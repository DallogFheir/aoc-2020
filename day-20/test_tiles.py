from tiles import ImageAssembler, Layout, Tile
import numpy as np
import unittest

class TestImageAssembler(unittest.TestCase):
    def setUp(self):
        with open("test_data/input.txt") as f:
            self.image = ImageAssembler(f)

    def test_parse_file(self):
        expected_first_tile = np.array([
            [".", ".", "#", "#", ".", "#", ".", ".", "#", "." ],
            ["#", "#", ".", ".", "#", ".", ".", ".", ".", "." ],
            ["#", ".", ".", ".", "#", "#", ".", ".", "#", "." ],
            ["#", "#", "#", "#", ".", "#", ".", ".", ".", "#" ],
            ["#", "#", ".", "#", "#", ".", "#", "#", "#", "." ],
            ["#", "#", ".", ".", ".", "#", ".", "#", "#", "#" ],
            [".", "#", ".", "#", ".", "#", ".", ".", "#", "#" ],
            [".", ".", "#", ".", ".", ".", ".", "#", ".", "." ],
            ["#", "#", "#", ".", ".", ".", "#", ".", "#", "." ],
            [".", ".", "#", "#", "#", ".", ".", "#", "#", "#" ]
        ])
        expected_ids = sorted([2311, 1951, 1427, 1171, 1489, 2971, 2729, 3079, 2473])

        with open("test_data/input.txt") as f:
            tile_lst = ImageAssembler._parse_file(None,f)
        actual_first_tile = tile_lst[0].layouts[3].layout
        actual_ids = sorted([tile.id for tile in tile_lst])

        res = np.array_equal(expected_first_tile,actual_first_tile)

        self.assertTrue(res)
        self.assertEqual(expected_ids,actual_ids)

    def test_check_how_many_fits(self):
        tile_dict = self.image._check_how_many_fits()
        id_dict = {tile.id:count for tile, count in tile_dict.items()}

        expected_dict = {
            1951 : 2,
            2311 : 3,
            3079 : 2,
            2729 : 3,
            1427 : 4,
            2473 : 3,
            2971 : 2,
            1489 : 3,
            1171 : 2
        }

        self.assertEqual(id_dict,expected_dict)

    def test_get_corners(self):
        _corners = self.image._get_corners()
        corners = [tile.id for tile in _corners]

        self.assertEqual(
            sorted(corners),
            [1171, 1951, 2971, 3079]
        )

    def test_remove_edges(self):
        inp = np.array([
            [1,2,3,4,5,6],
            [7,8,9,10,11,12],
            [13,14,15,16,17,18],
            [19,20,21,22,23,24]
        ])
        expected_output = np.array([
            [8,9,10,11],
            [14,15,16,17]
        ])

        actual_output = ImageAssembler._remove_edges(None,inp)

        res = np.array_equal(expected_output,actual_output)

        self.assertTrue(res)

    def test_assemble(self):
        image = self.image.assemble().eval()

        corners = [
            image[0][0],
            image[len(image)-1][0],
            image[0][len(image[0])-1],
            image[len(image)-1][len(image[0])-1]
        ]

        product = 1
        for corner in corners:
            product *= corner.id

        self.assertEqual(product,20899048083289)

    def test_find_monsters(self):
        sea = self.image.find_monsters()

        self.assertEqual(sea.monster_count,2)
        self.assertEqual(sea.roughness,273)

class TestLayout(unittest.TestCase):
    def test_get_edges(self):
        tile_array = np.array([
            [".", ".", "#", "#", ".", "#", ".", ".", "#", "." ],
            ["#", "#", ".", ".", "#", ".", ".", ".", ".", "." ],
            ["#", ".", ".", ".", "#", "#", ".", ".", "#", "." ],
            ["#", "#", "#", "#", ".", "#", ".", ".", ".", "#" ],
            ["#", "#", ".", "#", "#", ".", "#", "#", "#", "." ],
            ["#", "#", ".", ".", ".", "#", ".", "#", "#", "#" ],
            [".", "#", ".", "#", ".", "#", ".", ".", "#", "#" ],
            [".", ".", "#", ".", ".", ".", ".", "#", ".", "." ],
            ["#", "#", "#", ".", ".", ".", "#", ".", "#", "." ],
            [".", ".", "#", "#", "#", ".", ".", "#", "#", "#" ]
        ])
        top = np.array([".", ".", "#", "#", ".", "#", ".", ".", "#", "." ])
        right = np.array([".", ".", ".", "#", ".", "#", "#", ".", ".", "#"])
        bottom = np.array([".", ".", "#", "#", "#", ".", ".", "#", "#", "#" ])
        left = np.array([".", "#", "#", "#", "#", "#", ".", ".", "#", "."])
        expected_output = [top, right, bottom, left]

        actual_output = Layout._get_edges(None,tile_array)

        res = np.array_equal(expected_output,actual_output)

        self.assertTrue(res)

class TestTile(unittest.TestCase):
    def test_convert_tile_text_to_array(self):
        tile_text = "..##.#..#.\n##..#.....\n#...##..#.\n####.#...#\n##.##.###.\n##...#.###\n.#.#.#..##\n..#....#..\n###...#.#.\n..###..###"
        expected_output = np.array([
            [".", ".", "#", "#", ".", "#", ".", ".", "#", "." ],
            ["#", "#", ".", ".", "#", ".", ".", ".", ".", "." ],
            ["#", ".", ".", ".", "#", "#", ".", ".", "#", "." ],
            ["#", "#", "#", "#", ".", "#", ".", ".", ".", "#" ],
            ["#", "#", ".", "#", "#", ".", "#", "#", "#", "." ],
            ["#", "#", ".", ".", ".", "#", ".", "#", "#", "#" ],
            [".", "#", ".", "#", ".", "#", ".", ".", "#", "#" ],
            [".", ".", "#", ".", ".", ".", ".", "#", ".", "." ],
            ["#", "#", "#", ".", ".", ".", "#", ".", "#", "." ],
            [".", ".", "#", "#", "#", ".", ".", "#", "#", "#" ]
        ])
        actual_output = Tile._convert_tile_text_to_array(None,tile_text)

        res = np.array_equal(expected_output,actual_output)
        self.assertTrue(res)

    def test_generate_possible_layouts(self):
        with open("test_data/layouts.txt") as f:
            tiles = f.read().split("\n\n")
            expected_output = np.array([
                [
                    list(row.strip())
                    for row in tile.split("\n")
                ]
                for tile in tiles
                ])
        tile_array = np.array([
            [".", ".", "#", "#", ".", "#", ".", ".", "#", "." ],
            ["#", "#", ".", ".", "#", ".", ".", ".", ".", "." ],
            ["#", ".", ".", ".", "#", "#", ".", ".", "#", "." ],
            ["#", "#", "#", "#", ".", "#", ".", ".", ".", "#" ],
            ["#", "#", ".", "#", "#", ".", "#", "#", "#", "." ],
            ["#", "#", ".", ".", ".", "#", ".", "#", "#", "#" ],
            [".", "#", ".", "#", ".", "#", ".", ".", "#", "#" ],
            [".", ".", "#", ".", ".", ".", ".", "#", ".", "." ],
            ["#", "#", "#", ".", ".", ".", "#", ".", "#", "." ],
            [".", ".", "#", "#", "#", ".", ".", "#", "#", "#" ]
        ])
        actual_output = [
            layout.layout
            for layout in Tile._generate_possible_layouts(None,tile_array)]

        self.assertEqual(
            sorted(expected_output.tolist()),
            sorted(np.array(actual_output).tolist())
        )

    def test_fits(self):
        tile_text_1 = "..##.#..#.\n##..#.....\n#...##..#.\n####.#...#\n##.##.###.\n##...#.###\n.#.#.#..##\n..#....#..\n###...#.#.\n..###..###"
        tile_text_2 = "###.##.#..\n.#..#.##..\n.#.##.#..#\n#.#.#.##.#\n....#...##\n...##..##.\n...#.#####\n.#.####.#.\n..#..###.#\n..##.#..#."
        tile_1 = Tile(1,tile_text_1)
        tile_2 = Tile(2,tile_text_2)
        tile_array_1 = np.array([
            [".", ".", "#", "#", ".", "#", ".", ".", "#", "."], 
            ["#", "#", ".", ".", "#", ".", ".", ".", ".", "."], 
            ["#", ".", ".", ".", "#", "#", ".", ".", "#", "."], 
            ["#", "#", "#", "#", ".", "#", ".", ".", ".", "#"], 
            ["#", "#", ".", "#", "#", ".", "#", "#", "#", "."], 
            ["#", "#", ".", ".", ".", "#", ".", "#", "#", "#"], 
            [".", "#", ".", "#", ".", "#", ".", ".", "#", "#"], 
            [".", ".", "#", ".", ".", ".", ".", "#", ".", "."], 
            ["#", "#", "#", ".", ".", ".", "#", ".", "#", "."], 
            [".", ".", "#", "#", "#", ".", ".", "#", "#", "#"] 
        ])
        tile_array_2 = np.array([
            ["#", "#", "#", ".", "#", "#", ".", "#", ".", "."],
            [".", "#", ".", ".", "#", ".", "#", "#", ".", "."],
            [".", "#", ".", "#", "#", ".", "#", ".", ".", "#"],
            ["#", ".", "#", ".", "#", ".", "#", "#", ".", "#"],
            [".", ".", ".", ".", "#", ".", ".", ".", "#", "#"],
            [".", ".", ".", "#", "#", ".", ".", "#", "#", "."],
            [".", ".", ".", "#", ".", "#", "#", "#", "#", "#"],
            [".", "#", ".", "#", "#", "#", "#", ".", "#", "."],
            [".", ".", "#", ".", ".", "#", "#", "#", ".", "#"],
            [".", ".", "#", "#", ".", "#", ".", ".", "#", "."],
        ])
        
        self.assertTrue(tile_1.fits(tile_2,"top"))
        self.assertFalse(tile_1.fits(tile_2,"bottom"))
        self.assertFalse(tile_1.fits(tile_2,"left"))
        self.assertFalse(tile_1.fits(tile_2,"right"))

        res = np.array_equal(tile_2.current_orientation.layout,tile_array_2)
        self.assertTrue(res)

        self.assertTrue(tile_2.fits(tile_1,"bottom"))
        self.assertFalse(tile_2.fits(tile_1,"top"))
        self.assertFalse(tile_2.fits(tile_1,"left"))
        self.assertFalse(tile_2.fits(tile_1,"right"))

        res = np.array_equal(tile_1.current_orientation.layout,tile_array_1)
        self.assertTrue(res)

if __name__=="__main__":
    unittest.main()
