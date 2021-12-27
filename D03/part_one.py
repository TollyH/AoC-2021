import os

from PIL import Image

with open("input.txt") as file:
    puzzle_input = file.read().strip().splitlines()

if not os.path.isdir("output_part_one"):
    os.mkdir("output_part_one")

img = Image.new('1', (len(puzzle_input[0]) * 42, len(puzzle_input)))
for y, bin_str in enumerate(puzzle_input):
    for x, digit in enumerate(bin_str):
        for i in range(42):
            img.putpixel(((x * 42) + i, y), int(digit))
img.save("output_part_one/0000.png")

gamma_rate_str = ''
epsilon_rate_str = ''

for column in range(len(puzzle_input[0])):
    all_bits = [x[column] for x in puzzle_input]
    gamma_rate_str += max(('0', '1'), key=all_bits.count)
    epsilon_rate_str += min(('0', '1'), key=all_bits.count)
    for x in range(42):
        for y in range(len(puzzle_input)):
            img.putpixel((x + (column * 42), y), int(gamma_rate_str[-1]))
    img.save(f"output_part_one/{column + 1:04d}.png")

os.system(
    "ffmpeg -f image2 -framerate 1 -i output_part_one/%04d.png part_one.gif"
)

gamma_rate = int(gamma_rate_str, 2)
epsilon_rate = int(epsilon_rate_str, 2)

print(gamma_rate * epsilon_rate)
