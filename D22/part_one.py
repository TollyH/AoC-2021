with open("input.txt") as file:
    puzzle_input = file.read().strip().splitlines()

active_cubes = set()

for line in puzzle_input:
    x_bounds, y_bounds, z_bounds = (
        tuple(map(int, x.split("=")[1].split(".."))) for x in line.split(",")
    )
    for x in range(x_bounds[0], x_bounds[1] + 1):
        if x < -50 or x > 50:
            break
        for y in range(y_bounds[0], y_bounds[1] + 1):
            if y < -50 or y > 50:
                break
            for z in range(z_bounds[0], z_bounds[1] + 1):
                if z < -50 or z > 50:
                    break
                if line.startswith("on"):
                    active_cubes.add((x, y, z))
                elif (x, y, z) in active_cubes:
                    active_cubes.remove((x, y, z))

print(len(active_cubes))
