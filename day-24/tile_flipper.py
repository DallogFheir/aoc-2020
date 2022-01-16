import re

class TileFlipper:
    cmd_trans = {
            "e" : (1,0),
            "se" : (0,-1),
            "ne" : (1,1),
            "w" : (-1,0),
            "sw" : (-1,-1),
            "nw" : (0,1)
        }
    
    def __init__(self,instructions):
        self.instructions = instructions

    def flip(self):
        tiles = set()

        for ins in self.instructions:
            start_point = [0,0]
            for cmd in ins:
                move = self.cmd_trans[cmd]
                start_point[0] += move[0]
                start_point[1] += move[1]
            
            end_point = tuple(start_point)

            if end_point in tiles:
                tiles.remove(end_point)
            else:
                tiles.add(end_point)

        return tiles

    def switch_tiles(self):
        black_tiles = self.flip()

        while True:
            yield black_tiles.copy()

            # make a dict of tiles that have black neighbors
            black_neighbors = {}
            for tile in black_tiles:
                tile_neighbors = [
                    (tile[0]+x, tile[1]+y)
                    for x, y in self.cmd_trans.values()
                ]

                for n in tile_neighbors:
                    if n in black_neighbors:
                        black_neighbors[n] += 1
                    else:
                        black_neighbors[n] = 1

            # switch tiles that have black neighbors
            for tile, num_of_neighbors in black_neighbors.items():
                if tile in black_tiles and num_of_neighbors>2:
                    black_tiles.remove(tile)
                elif tile not in black_tiles and num_of_neighbors==2:
                    black_tiles.add(tile)

            # remove black tiles that have no black neighbors
            tiles_without_neighbors = black_tiles - set(black_neighbors.keys())

            black_tiles.difference_update(tiles_without_neighbors)

    @classmethod
    def from_file(cls,fh):
        ins_pattern = re.compile(r"((?:s|n)?(?:w|e))")

        instructions = []
        for line in fh:
            cmds = re.findall(ins_pattern,line)
            instructions.append(cmds)

        return cls(instructions)
