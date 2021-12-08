with open("input.txt") as file:
    puzzle_input = file.read().strip().split(",")
    file.close()

positions = [int(x) for x in puzzle_input]
targets = {}

for target in range(max(positions)):
    targets[target] = 0
    for pos in positions:
        targets[target] += abs(pos - target)

optimal_target = min(targets, key=lambda x: targets[x])

print(f"Position: {optimal_target}, Fuel: {targets[optimal_target]}")
