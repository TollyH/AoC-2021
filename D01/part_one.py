import matplotlib.pyplot as plt

with open("input.txt") as file:
    puzzle_input = file.read().strip().splitlines()

cast_puzzle_input = [int(x) for x in puzzle_input]

total_increased = 0

for i in range(1, len(puzzle_input)):
    if cast_puzzle_input[i] > cast_puzzle_input[i - 1]:
        if i <= 200:
            plt.plot(i, -cast_puzzle_input[i], color="green", marker=".")
        total_increased += 1
    elif i <= 200:
        plt.plot(i, -cast_puzzle_input[i], color="red", marker=".")

print(total_increased)
plt.savefig("part_one.png", dpi=200)
