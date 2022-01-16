import copy
import itertools

class SeatLayout:
    def __init__(self,initial,inf_iter=False,mode=None):
        self.grid = initial
        self.next_layouts_cache = {"part_1" : [self], "part_2" : [self]}
        self.mode = mode
        self.if_iterate_infinitely = inf_iter

    def __getitem__(self,iteration):
        if self.mode is None:
            raise AttributeError("Mode is not set.")
        elif self.mode=="part_1":
            get_neighbors = type(self).get_adjacent_neighbors
            occupied_count = 4
            cache = self.next_layouts_cache["part_1"]
        elif self.mode=="part_2":
            get_neighbors = type(self).get_cardinal_neighbors
            occupied_count = 5
            cache = self.next_layouts_cache["part_2"]

        start = len(cache)-1
        new_layout = cache[start]

        for _ in range(start,iteration):
            orig_grid = copy.deepcopy(new_layout)
            new_grid = copy.deepcopy(orig_grid.grid)

            for i_row, row in enumerate(orig_grid.grid):
                for i_col, el in enumerate(row):
                    neighbor_inds = get_neighbors(orig_grid,i_row,i_col)
                    neighbor_states = orig_grid.get_seat_states(neighbor_inds).values()

                    if el=="L" and "#" not in neighbor_states:
                        new_grid[i_row][i_col] = "#"
                    elif el=="#" and list(neighbor_states).count("#")>=occupied_count:
                        new_grid[i_row][i_col] = "L"
                
            new_layout = type(self)(new_grid)

            if not self.if_iterate_infinitely and new_layout.grid==cache[-1].grid:
                raise IndexError

            cache.append(new_layout)

        return cache[iteration]

    def set_mode(self,mode):
        self.mode = mode

    def set_infinite_iteration(self,boolean):
        self.if_iterate_infinitely = boolean

    @property
    def size(self):
        return (len(self.grid), len(self.grid[0]))

    @property
    def last_iteration(self):
        current_toggle = self.if_iterate_infinitely

        self.set_infinite_iteration(False)

        for i, iteration in enumerate(self):
            pass

        self.set_infinite_iteration(current_toggle)

        return i

    @property
    def final_state(self):
        current_toggle = self.if_iterate_infinitely

        self.set_infinite_iteration(False)

        for iteration in self:
            pass

        self.set_infinite_iteration(current_toggle)

        return iteration

    @property
    def occupied_seats(self):
        return self._count_seats("#")

    @property
    def empty_seats(self):
        return self._count_seats("L")

    @property
    def floor_tiles(self):
        return self._count_seats(".")

    def _count_seats(self,type):
        count = 0
        for row in self.grid:
            count += row.count(type)

        return count

    def get_seat_states(self,seats):
        seat_states = {}

        for seat in seats:
            row, col = seat

            seat_states[seat] = self.grid[row][col]

        return seat_states

    def get_adjacent_neighbors(self,row,col):
        lst_len = len(self.grid)
        row_len = len(self.grid[0])

        adjacent_indices = itertools.product(range(-1,2),repeat=2)

        return [
            (row+i,col+j)
            for i, j in adjacent_indices
            if not (i==0 and j==0)
            and not (row+i<0 or col+j<0)
            and not col+j>=row_len
            and not row+i>=lst_len
        ]

    def get_cardinal_neighbors(self,row,col):
        cardinal_directions = itertools.product(range(-1,2),repeat=2)

        neighbors = []

        for i, j in cardinal_directions:
            if not (i==0 and j==0):
                neighbor = self._traverse_cardinal_direction(row,col,i,j)

                if neighbor is not None:
                    neighbors.append(neighbor)

        return neighbors

    def _traverse_cardinal_direction(self,row,col,dir_hor,dir_vert):
        lst_len = len(self.grid)
        row_len = len(self.grid[0])

        inc_hor = dir_hor
        inc_vert = dir_vert

        while True:
            next_row = row+dir_hor
            next_col = col+dir_vert

            if next_row<0 or next_col<0\
            or next_row>=lst_len\
            or next_col>=row_len:
                return None
            
            next_tile = self.grid[next_row][next_col]

            dir_hor += inc_hor
            dir_vert += inc_vert

            if next_tile!=".":
                return (next_row, next_col)

    @classmethod
    def from_file(cls,fh,inf_iter=False,mode=None):
        initial = [list(line.strip()) for line in fh.readlines()]

        return cls(initial,inf_iter=inf_iter,mode=mode)
