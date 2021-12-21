with open("input.txt") as file:
    puzzle_input = file.read().strip().splitlines()

cast_puzzle_input = [int(x) for x in puzzle_input]

total_increased = 0

for i in range(1, len(puzzle_input)):
    if cast_puzzle_input[i] > cast_puzzle_input[i - 1]:
        total_increased += 1

print(total_increased)
