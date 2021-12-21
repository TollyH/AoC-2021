with open("input.txt") as file:
    puzzle_input = file.read().strip().split(",")

fish = [int(x) for x in puzzle_input]

for _ in range(80):
    for i in range(len(fish)):
        if fish[i] == 0:
            fish[i] = 6
            fish.append(8)
        else:
            fish[i] -= 1

print(len(fish))
