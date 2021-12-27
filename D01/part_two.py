import matplotlib.pyplot as plt

with open("input.txt") as file:
    puzzle_input = file.read().strip().splitlines()

cast_puzzle_input = [int(x) for x in puzzle_input]

total_increased = 0
previous_sum = sum(cast_puzzle_input[0:3])

for i in range(2, len(puzzle_input)):
    current_sum = sum(cast_puzzle_input[i - 2:i + 1])
    if current_sum > previous_sum:
        if i <= 200:
            plt.plot(i, -current_sum, color="green", marker=".")
        total_increased += 1
    elif i <= 200:
        plt.plot(i, -current_sum, color="red", marker=".")
    previous_sum = current_sum

print(total_increased)
plt.savefig("part_two.png", dpi=200)
