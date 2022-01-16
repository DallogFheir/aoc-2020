from itertools import product

def parse_initial_state(inp,dimensions):
    initial_state = []

    for y, row in enumerate(inp):
        for x, cube in enumerate(row):
            if cube=="#":
                initial_state.append(
                    (x,y) + (0,)*(dimensions-2)
                    )

    return initial_state

def get_neighbors(state,dimensions):
    possible_neighbors = [
        tuple(coord for coord in coords)
        for coords in product((-1,0,1),repeat=dimensions)
        if not all(coord==0 for coord in coords)]
    neighbors = {}

    for cube in state:
        for add_coords in possible_neighbors:
            coords = tuple(
                cube_coord+add_coord
                for cube_coord, add_coord in zip(cube,add_coords)
            )

            if coords in neighbors:
                neighbors[coords] += 1
            else:
                neighbors[coords] = 1

    return neighbors

def get_next_state(state,dimensions):
    neighbors = get_neighbors(state,dimensions)
    new_state = []

    for cube, num_of_neighbors in neighbors.items():
        # if cube is active, it stays active if 2 or 3 of its neighbors are active
        if cube in state and num_of_neighbors in (2,3):
            new_state.append(cube)

        # if cube is inactive, it becomes active if exactly 3 of its neighbors are active
        elif cube not in state and num_of_neighbors==3:
            new_state.append(cube)

    return new_state

def cycle(inp,dimensions,num_of_cycles):
    cycle = parse_initial_state(inp,dimensions)

    for _ in range(num_of_cycles):
        cycle = get_next_state(cycle,dimensions)

    return cycle
