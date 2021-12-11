with open("input.txt") as file:
    puzzle_input = file.read().strip().splitlines()
    file.close()

octopuses = [[int(x) for x in y] for y in puzzle_input]
octopuses_count = len(puzzle_input) * len(puzzle_input[0])


def flash(x_coord, y_coord):
    octopuses[y_coord][x_coord] = 0
    if (x_coord, y_coord) in already_flashed:
        return
    already_flashed.append((x_coord, y_coord))
    adjacent = []
    if y_coord >= 1:
        adjacent.append((x_coord, y_coord - 1))
    if y_coord < len(octopuses) - 1:
        adjacent.append((x_coord, y_coord + 1))
    if x_coord >= 1:
        adjacent.append((x_coord - 1, y_coord))
    if x_coord < len(octopuses[y_coord]) - 1:
        adjacent.append((x_coord + 1, y_coord))
    if y_coord >= 1 and x_coord >= 1:
        adjacent.append((x_coord - 1, y_coord - 1))
    if y_coord < len(octopuses) - 1 and x_coord < len(octopuses) - 1:
        adjacent.append((x_coord + 1, y_coord + 1))
    if x_coord >= 1 and y_coord < len(octopuses) - 1:
        adjacent.append((x_coord - 1, y_coord + 1))
    if x_coord < len(octopuses[y_coord]) - 1 and y_coord >= 1:
        adjacent.append((x_coord + 1, y_coord - 1))
    for coords in adjacent:
        octopuses[coords[1]][coords[0]] += 1
        if octopuses[coords[1]][coords[0]] == 10:
            flash(*coords)


i = 0
already_flashed = []
while len(already_flashed) != octopuses_count:
    already_flashed = []
    for y, row in enumerate(octopuses):
        for x, octopus in enumerate(row):
            octopuses[y][x] += 1
            if octopuses[y][x] == 10:
                flash(x, y)
    for x, y in already_flashed:
        octopuses[y][x] = 0
    i += 1

print(f"{i=}")
