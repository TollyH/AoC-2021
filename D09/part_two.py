with open("input.txt") as file:
    puzzle_input = file.read().strip().splitlines()
    file.close()

heightmap = [list(x) for x in puzzle_input]
basins = []

def generate_basin(x_coord, y_coord):
    if (heightmap[y_coord][x_coord] == '9'
            or (x_coord, y_coord) in [x for y in basins for x in y]):
        return
    basins[-1].append((x_coord, y_coord))
    adjacent = [(x_coord, y_coord)]
    if y_coord >= 1:
        adjacent.append((x_coord, y_coord - 1))
    if y_coord < len(heightmap) - 1:
        adjacent.append((x_coord, y_coord + 1))
    if x_coord >= 1:
        adjacent.append((x_coord - 1, y_coord))
    if x_coord < len(heightmap[y_coord]) - 1:
        adjacent.append((x_coord + 1, y_coord))
    for coords in adjacent:
        generate_basin(*coords)

for y, row in enumerate(puzzle_input):
    for x, height in enumerate(row):
        if (x, y) not in [i for j in basins for i in j]:
            basins.append([])
            generate_basin(x, y)
            if basins[-1] == []:
                basins = basins[:-1]

basins.sort(key=len, reverse=True)
product = 1
for basin in basins[:3]:
    product *= len(basin)

print(f"{product=}")
