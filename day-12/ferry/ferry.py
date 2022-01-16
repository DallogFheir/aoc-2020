class Ferry:
    def __init__(self,instructions):
        self.dirs = "NESW"
        self.instructions = instructions

        self.cmd_trans = {
            "N" : lambda cur_coord, param : self.add_coords(cur_coord,(0,1*param)),
            "E" : lambda cur_coord, param : self.add_coords(cur_coord,(1*param,0)),
            "S" : lambda cur_coord, param : self.add_coords(cur_coord,(0,-1*param)),
            "W" : lambda cur_coord, param : self.add_coords(cur_coord,(-1*param,0))
        }

    def to_directional(self):
        return DirectionalFerry(self.instructions)

    def to_waypoint(self):
        return WaypointFerry(self.instructions)

    @property
    def path(self):
        if hasattr(self,"_path"):
            return self._path

        raise AttributeError("Ferry hasn't moved yet!")

    @staticmethod
    def add_coords(coords,increment):
        return tuple(x+y for x, y in zip(coords,increment))

    @classmethod
    def from_file(cls,fh):
        return cls([
            (line[0], int(line[1:].strip()))
            for line in fh.readlines()
        ])

class DirectionalFerry(Ferry):
    def __init__(self,instructions):
        super().__init__(instructions)

        self.cmd_trans.update({
            "L" : lambda cur_coord, param : self.change_dir(-param),
            "R" : lambda cur_coord, param : self.change_dir(param),
            "F" : lambda cur_coord, param : self.cmd_trans[self.cur_dir](cur_coord,param)
        })

    def move_ferry(self):
        self.cur_dir = "E"
        start_point = (0,0)

        path = [start_point]
        cur_coord = start_point

        for cmd, param in self.instructions:
            res = self.cmd_trans[cmd](cur_coord,param)

            if res is not None:
                cur_coord = res
                path.append(res)

        self._path = path

    def change_dir(self,degrees):
        cur_dir_index = self.dirs.index(self.cur_dir)
        change = degrees // 90

        self.cur_dir = self.dirs[(cur_dir_index+change)%4]

    @property
    def map_size(self):
        x_coords = [coords[0] for coords in self.path]
        y_coords = [coords[1] for coords in self.path]

        return (
            abs(max(x_coords)-min(x_coords)),
            abs(max(y_coords)-min(y_coords))
        )

    @property
    def manhattan_dst(self):
        x, y = self.path[-1]
        return abs(x) + abs(y)

class WaypointFerry(Ferry):
    def __init__(self,instructions):
        super().__init__(instructions)

        self.cmd_trans.update({
            "L" : lambda cur_coord, param : self.rotate_waypoint(cur_coord,param,"counterclockwise"),
            "R" : lambda cur_coord, param : self.rotate_waypoint(cur_coord,param,"clockwise"),
            "F" : lambda cur_coord, param : self.add_coords(cur_coord,param)
        })

    def move_ferry(self):
        start_point = (0,0)
        start_waypoint = (10,1)

        path = [(start_point, start_waypoint)]
        cur_coord = start_point
        cur_waypoint = start_waypoint

        for cmd, param in self.instructions:
            if cmd=="F":
                x, y = cur_waypoint

                cur_coord = self.cmd_trans[cmd](cur_coord,(x*param, y*param))
            else:
                cur_waypoint = self.cmd_trans[cmd](cur_waypoint,param)

            path.append((cur_coord, cur_waypoint))

        self._path = path

    @staticmethod
    def rotate_waypoint(waypoint,degrees,mode):
        change = degrees // 90
        index = 1 if mode=="clockwise" else 0

        for _ in range(change):
            waypoint = list(reversed(waypoint))
            waypoint[index] = -waypoint[index]

        return tuple(waypoint)

    @property
    def manhattan_dst(self):
        coord, waypoint = self.path[-1]

        x, y = coord

        return abs(x) + abs(y)

    @property
    def map_size(self):
        x_coords = [coords[0][0] for coords in self.path]
        y_coords = [coords[0][1] for coords in self.path]
        
        return (
            abs(max(x_coords)-min(x_coords)),
            abs(max(y_coords)-min(y_coords))
        )
