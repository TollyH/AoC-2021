import os

from PIL import Image

with open("input.txt") as file:
    puzzle_input = file.read().strip().splitlines()

if not os.path.isdir("output_part_two"):
    os.mkdir("output_part_two")

COLORS = [
    (71, 19, 240),
    (100, 60, 230),
    (108, 90, 230),
    (73, 150, 227),
    (104, 163, 222),
    (196, 222, 104),
    (211, 230, 147),
    (224, 220, 155),
    (230, 226, 170),
    (242, 240, 216)
]

octopuses = [[int(x) for x in y] for y in puzzle_input]
octopuses_count = len(puzzle_input) * len(puzzle_input[0])


def save_octo_image(octopus_map, step_counter):
    img = Image.new("RGB", (len(octopus_map[0]) * 50, len(octopus_map) * 50))
    for img_y, octo_row in enumerate(octopus_map):
        for img_x, octo in enumerate(octo_row):
            for ix in range(50):
                for iy in range(50):
                    img.putpixel(
                        (img_x * 50 + ix, img_y * 50 + iy), COLORS[octo]
                    )
    img.save(f"output_part_two/{step_counter:04d}.png")


def flash(x_coord, y_coord):
    octopuses[y_coord][x_coord] = 0
    if (x_coord, y_coord) in already_flashed:
        return
    already_flashed.append((x_coord, y_coord))
    adjacent = []
    if y_coord >= 1:
        adjacent.append((x_coord, y_coord - 1))
    if y_coord < len(octopuses) - 1:
        adjacent.append((x_coord, y_coord + 1))
    if x_coord >= 1:
        adjacent.append((x_coord - 1, y_coord))
    if x_coord < len(octopuses[y_coord]) - 1:
        adjacent.append((x_coord + 1, y_coord))
    if y_coord >= 1 and x_coord >= 1:
        adjacent.append((x_coord - 1, y_coord - 1))
    if y_coord < len(octopuses) - 1 and x_coord < len(octopuses) - 1:
        adjacent.append((x_coord + 1, y_coord + 1))
    if x_coord >= 1 and y_coord < len(octopuses) - 1:
        adjacent.append((x_coord - 1, y_coord + 1))
    if x_coord < len(octopuses[y_coord]) - 1 and y_coord >= 1:
        adjacent.append((x_coord + 1, y_coord - 1))
    for coords in adjacent:
        octopuses[coords[1]][coords[0]] += 1
        if octopuses[coords[1]][coords[0]] == 10:
            flash(*coords)


i = 0
already_flashed = []
while len(already_flashed) != octopuses_count:
    already_flashed = []
    for y, row in enumerate(octopuses):
        for x, octopus in enumerate(row):
            octopuses[y][x] += 1
            if octopuses[y][x] == 10:
                flash(x, y)
    for x, y in already_flashed:
        octopuses[y][x] = 0
    i += 1
    save_octo_image(octopuses, i)

os.system(
    "ffmpeg -f image2 -framerate 10 -i output_part_two/%04d.png part_two.gif"
)

print(i)
