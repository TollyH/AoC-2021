with open("input.txt") as file:
    puzzle_input = file.read().strip().splitlines()
    file.close()

horizontal = 0
depth = 0
aim = 0

for line in puzzle_input:
    split_line = line.split(" ")
    instruction = split_line[0]
    parameter = int(split_line[1])
    if instruction == "forward":
        horizontal += parameter
        depth += aim * parameter
    elif instruction == "down":
        aim += parameter
    elif instruction == "up":
        aim -= parameter

print(f"{horizontal=} {depth=} {horizontal*depth=}")
