with open("input.txt") as file:
    puzzle_input = file.read().strip().splitlines()

unique_count = 0

for entry in puzzle_input:
    for output in entry.split(" | ")[1].split(" "):
        if len(output) in {2, 4, 3, 7}:
            unique_count += 1

print(unique_count)
