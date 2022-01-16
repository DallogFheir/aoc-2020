from PIL import Image
import os
from seats import SeatLayout
import itertools
import random
from datetime import datetime

def visualize(path,mode):
    tile_to_color = {
    "L" : (0,255,0),
    "#" : (255,0,0),
    "." : (255,255,255)
    }

    with open(f"{path}/input.txt") as f:
        seats = SeatLayout.from_file(f)

    height, width = seats.size
    multiplier = min(1028//height, 1920//width)

    output = Image.new("RGB",tuple(multiplier*dimension for dimension in seats.size))

    seats.set_mode(mode)
    print(f"Iterations: {seats.last_iteration}.")

    for iteration, layout in enumerate(seats):
        for i, row in enumerate(layout.grid):
            for j, el in enumerate(row):
                color = tile_to_color[el]
                pixel_range = itertools.product(range(multiplier),repeat=2)

                for hor, vert in pixel_range:
                    output.putpixel((multiplier*i+hor,multiplier*j+vert),color)

        print(f"Iteration {iteration}.")

        save_path = f"{path}/{mode}/imgs"

        if not os.path.exists(save_path):
            os.makedirs(save_path)
        
        output.save(f"{save_path}/{iteration}.png")

def random_visualize(size):
    tiles = [".", "L"]

    name = datetime.now().timestamp()
    path = f"visualizations/{name}"
    os.makedirs(path,exist_ok=True)

    height, width = size
    lines = []
    for _ in range(height):
        st = ""
        for _ in range(width):
            st += random.choice(tiles)

        st += "\n"
        lines.append(st)

    lines[-1] = lines[-1].strip()

    with open(f"{path}/input.txt", "w+") as f:
        f.writelines(lines)

    for mode in ("part_1", "part_2"):
        visualize(path,mode)

###
if __name__=="__main__":
    visualize("visualizations/half","part_1")
    visualize("visualizations/half","part_2")
