from collections import namedtuple
import numpy as np
import re

Sea = namedtuple("Sea", ["monster_count", "roughness"])

Edge = namedtuple("Edge", ["top", "right", "bottom", "left"])

class Node:
    def __init__(self,arr,remaining):
        self.array = arr
        self.children = self._get_children(arr,remaining)

    def _get_children(self,arr,remaining):
        if np.all(arr):
            return True

        # find first not-None element
        checking = True
        for i, row in enumerate(arr):
            if not checking:
                break

            for j, el in enumerate(row):
                if el is None:
                    y = i
                    x = j
                    checking = False
                    break

        # if element is first in row, match it to element above
        # else match it to the right
        if x==0:
            tile = arr[y-1][0]
            side = "bottom"
        else:
            tile = arr[y][x-1]
            side = "right"

        fitting = []
        for other in remaining:
            if tile.fits(other,side):
                fitting.append(other)

        if len(fitting)==0:
            return False
        elif len(fitting)==1:
            arr[y][x] = fitting[0]
            remaining.remove(fitting[0])
            children = self._get_children(arr,remaining)
        else:
            children = []
            for fit in fitting:
                arr_arg = np.array(arr)
                arr_arg[y][x] = fit
                rem_arg = remaining.copy()

                children.append(type(self)(arr_arg,rem_arg))

        return children

    def eval(self):
        if self.children is True:
            return self.array
        if self.children is False:
            return False
        
        for child in self.children:
            res = child.eval()

            if res is True:
                return child.array

class Layout:
    def __init__(self,layout_array):
        top, right, bottom, left = self._get_edges(layout_array)

        self.layout = layout_array
        self.edges = Edge(top, right, bottom, left)

    def _get_edges(self,layout_array):
        return [
            row := layout_array[0], # top
            layout_array[:,len(row)-1], # right
            layout_array[len(layout_array)-1], # bottom
            layout_array[:,0] # left
        ]

class Tile:
    def __init__(self,id,tile_as_text):
        self.id = id

        tile_array = self._convert_tile_text_to_array(tile_as_text)
        self.layouts = self._generate_possible_layouts(tile_array)

        self.current_orientation = Layout(tile_array)

    def __repr__(self):
        id = self.id
        return f"({id})"

    def _convert_tile_text_to_array(self,tile_as_text):
        rows = tile_as_text.split("\n")

        for row, st in enumerate(rows):
            rows[row] = list(st.strip())

        return np.array(rows)

    def _generate_possible_layouts(self,tile_array):
        layouts = []
        rotated = tile_array
        for _ in range(2):
            for _ in range(4):
                rotated = np.rot90(rotated)

                layouts.append(Layout(rotated))

            rotated = np.fliplr(tile_array)

        return layouts

    def fits(self,other,self_side):
        _sides = {"top" : "bottom", "left" : "right"}
        sides = _sides | {v:k for k, v in _sides.items()}

        other_side = sides[self_side]

        for i, layout in enumerate(other.layouts):
            if np.array_equal(
                getattr(self.current_orientation.edges,self_side),
                getattr(layout.edges,other_side)
            ):
                other.current_orientation = other.layouts[i]
                return True

        return False

class ImageAssembler:
    def __init__(self,fh):
        self.tiles = self._parse_file(fh)
        self.corners = self._get_corners()

    def _parse_file(self,fh):
        tiles = fh.read().split("\n\n")

        output = []
        for tile in tiles:
            tile_info = tile.split(":\n")
            tile_id, tile_text = tile_info

            id = int(re.match(r"Tile (\d+)",tile_id).group(1))

            output.append(Tile(id,tile_text))

        return output

    def _check_how_many_fits(self):
        tile_dict = {}
        tiles = set(self.tiles)

        for tile in tiles:
            count = 0

            for other_tile in tiles - {tile}:
                for side in ("top", "bottom", "left", "right"):
                    if tile.fits(other_tile,side):
                        count += 1
                        break
            
            tile_dict[tile] = count

        return tile_dict

    def _get_corners(self):
        neighbor_dict = self._check_how_many_fits()

        return [
            tile
            for tile, count in neighbor_dict.items()
            if count==2
        ]

    def _remove_edges(self,arr):
        output = np.delete(arr,0,0)
        output = np.delete(output,0,1)
        output = np.delete(output,len(output)-1,0)
        output = np.delete(output,len(output[0])-1,1)

        return output

    def assemble(self):
        corner = self.corners[0]
        size = int(len(self.tiles)**0.5)

        remaining = self.tiles.copy()
        remaining.remove(corner)

        # find first corner edge that has a match to the right and to bottom
        for layout in corner.layouts:
            found_right = False
            found_bottom = False

            corner.current_orientation = layout

            for other in remaining:
                if corner.fits(other,"bottom"):
                    found_bottom = True
                    continue
                if corner.fits(other,"right"):
                    found_right = True
                    continue

            if found_bottom and found_right:
                break

        arr = np.empty((size,size),dtype=Tile)
        arr[0][0] = corner

        image = Node(arr,remaining)
        return image

    def find_monsters(self):
        image = self.assemble().eval()

        # remove edges
        for i, row in enumerate(image):
            for j, el in enumerate(row):
                image[i][j] = self._remove_edges(el.current_orientation.layout)

        # create image array
        decoded_image = []
        for row in image:
            for i in range(len(row[0])):
                image_row = []

                for j in range(len(row)):
                    image_row.extend(row[j][i])

                decoded_image.append(image_row)
        decoded_image = np.array(decoded_image)

        monster_coords = [
            (0, 18),
            (1, 0),
            (1, 5),
            (1, 6),
            (1, 11),
            (1, 12),
            (1, 17),
            (1, 18),
            (1, 19),
            (2, 1),
            (2, 4),
            (2, 7),
            (2, 10),
            (2, 13),
            (2, 16)
        ]

        # find sea monsters
        for _ in range(2):
            for _ in range(4):
                monster_count = 0

                for i in range(len(decoded_image)-2):
                    for j in range(len(decoded_image[0])-19):
                        if all(
                            decoded_image[i+y][j+x]=="#"
                            for y,x in monster_coords
                        ):
                            monster_count += 1

                if monster_count!=0:
                    # count # that are not part of sea monster
                    hash_count = 0
                    for row in decoded_image:
                        for el in row:
                            if el=="#":
                                hash_count += 1

                    roughness = hash_count - 15 * monster_count

                    output = Sea(monster_count,roughness)

                    return output

                decoded_image = np.rot90(decoded_image)

            decoded_image = np.fliplr(decoded_image)
