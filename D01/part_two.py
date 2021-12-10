with open("input.txt") as file:
    puzzle_input = file.read().strip().splitlines()
    file.close()

cast_puzzle_input = [int(x) for x in puzzle_input]

total_increased = 0
previous_sum = sum(cast_puzzle_input[0:3])

for i in range(2, len(puzzle_input)):
    current_sum = sum(cast_puzzle_input[i - 2:i + 1])
    if current_sum > previous_sum:
        total_increased += 1
    previous_sum = current_sum

print(total_increased)
