import matplotlib.pyplot as plt

with open("input.txt") as file:
    puzzle_input = file.read().strip().splitlines()

horizontal = [0]
depth = [0]
aim = 0

for line in puzzle_input:
    split_line = line.split(" ")
    instruction = split_line[0]
    parameter = int(split_line[1])
    if instruction == "forward":
        horizontal.append(horizontal[-1] + parameter)
        depth.append(depth[-1] + (aim * parameter))
    elif instruction == "down":
        aim += parameter
    elif instruction == "up":
        aim -= parameter

print(horizontal[-1] * depth[-1])
plt.plot(horizontal, list(map(lambda x: -x, depth)))
plt.savefig("part_two.png", dpi=200)
