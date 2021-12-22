with open("input.txt") as file:
    puzzle_input = file.read().strip().split(",")

positions = [int(x) for x in puzzle_input]
targets = {}

for target in range(max(positions)):
    targets[target] = 0
    for pos in positions:
        difference = abs(pos - target)
        targets[target] += 0.5 * difference * (difference + 1)

optimal_target = min(targets, key=lambda x: targets[x])

print(int(targets[optimal_target]))
