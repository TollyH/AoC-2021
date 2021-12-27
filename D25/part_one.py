import os

from PIL import Image

with open("input.txt") as file:
    puzzle_input = file.read().splitlines()

if not os.path.isdir("output"):
    os.mkdir("output")


def save_cucumber_image(cucumber_grid, move_counter):
    img = Image.new(
        "RGB", (len(cucumber_grid[0]) * 8, len(cucumber_grid) * 8), "#bf6730"
    )
    for y, y_cucumbers in enumerate(cucumber_grid):
        for x, cucumber_pixel in enumerate(y_cucumbers):
            if cucumber_pixel != ".":
                for ix in range(8):
                    for iy in range(8):
                        img.putpixel(
                            ((x * 8) + ix, (y * 8) + iy),
                            (207, 40, 31)
                            if cucumber_pixel == ">"
                            else (31, 90, 207)
                        )
    img.save(f"output/{move_counter:04d}.png")


cucumbers = [list(x) for x in puzzle_input]
new_cucumbers = None

save_cucumber_image(cucumbers, 0)

counter = 0
performed_move = True
while performed_move:
    new_cucumbers = [x.copy() for x in cucumbers]
    performed_move = False
    for row_index, row in enumerate(cucumbers):
        for index, cucumber in enumerate(row):
            if cucumber == ">" and row[(index + 1) % len(row)] == ".":
                new_cucumbers[row_index][index] = "."
                new_cucumbers[row_index][(index + 1) % len(row)] = ">"
                performed_move = True
    cucumbers = [x.copy() for x in new_cucumbers]
    for row_index, row in enumerate(cucumbers):
        for index, cucumber in enumerate(row):
            if (cucumber == "v"
                    and cucumbers[(row_index + 1) % len(cucumbers)][index]
                    == "."):
                new_cucumbers[row_index][index] = "."
                new_cucumbers[(row_index + 1) % len(cucumbers)][index] = "v"
                performed_move = True
    cucumbers = [x.copy() for x in new_cucumbers]
    counter += 1
    save_cucumber_image(cucumbers, counter)

os.system(
    "ffmpeg -f image2 -framerate 25 -i output/%04d.png output.gif"
)

print(counter)
