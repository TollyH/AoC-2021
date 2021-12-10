with open("input.txt") as file:
    puzzle_input = file.read().strip().split(",")
    file.close()

fish_spawn = {}
for fish in puzzle_input:
    if int(fish) not in fish_spawn:
        fish_spawn[int(fish)] = 1
    else:
        fish_spawn[int(fish)] += 1

if 8 not in fish_spawn:
    fish_spawn[8] = 0
if 6 not in fish_spawn:
    fish_spawn[6] = 0
if 0 not in fish_spawn:
    fish_spawn[0] = 0

for _ in range(256):
    new_fish = {6: 0, 8: 0}
    for day, count in fish_spawn.items():
        if day == 0:
            new_fish[6] += count
            new_fish[8] += count
        else:
            if day - 1 not in new_fish:
                new_fish[day - 1] = count
            else:
                new_fish[day - 1] += count
    fish_spawn = new_fish

print(sum(fish_spawn.values()))
