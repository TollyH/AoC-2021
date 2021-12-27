import os

from PIL import Image

with open("input.txt") as file:
    puzzle_input = file.read().strip().splitlines()

if not os.path.isdir("output_part_two"):
    os.mkdir("output_part_two")

img = Image.new('1', (len(puzzle_input[0]) * 42, len(puzzle_input)))
for y, bin_str in enumerate(puzzle_input):
    for x, digit in enumerate(bin_str):
        for i in range(42):
            img.putpixel(((x * 42) + i, y), int(digit))
img.save("output_part_two/0000.png")

oxygen_gen_rate_list = puzzle_input.copy()
c02_scrub_rate_list = puzzle_input.copy()

for column in range(len(puzzle_input[0])):
    oxygen_bits = [x[column] for x in oxygen_gen_rate_list]
    c02_bits = [x[column] for x in c02_scrub_rate_list]

    if oxygen_bits.count('1') != len(oxygen_bits) / 2:
        most_common = max(('0', '1'), key=oxygen_bits.count)
    else:
        most_common = '1'

    if c02_bits.count('0') != len(c02_bits) / 2:
        least_common = min(('0', '1'), key=c02_bits.count)
    else:
        least_common = '0'

    if len(oxygen_gen_rate_list) != 1:
        oxygen_gen_rate_list = [
            x for x in oxygen_gen_rate_list if x[column] == most_common
        ]
    if len(c02_scrub_rate_list) != 1:
        c02_scrub_rate_list = [
            x for x in c02_scrub_rate_list if x[column] == least_common
        ]
    img = Image.new('1', (len(puzzle_input[0]) * 42, len(puzzle_input)), 1)
    for y, bin_str in enumerate(oxygen_gen_rate_list):
        for x, digit in enumerate(bin_str):
            for i in range(42):
                img.putpixel(
                    (
                        (x * 42) + i,
                        (
                            len(puzzle_input) // 2 -
                            len(oxygen_gen_rate_list) // 2
                        ) + y
                    ),
                    int(digit)
                )
    img.save(f"output_part_two/{column + 1:04d}.png")

os.system(
    "ffmpeg -f image2 -framerate 1 -i output_part_two/%04d.png part_two.gif"
)

oxygen_gen_rate = int(oxygen_gen_rate_list[0], 2)
c02_scrub_rate = int(c02_scrub_rate_list[0], 2)

print(oxygen_gen_rate * c02_scrub_rate)
