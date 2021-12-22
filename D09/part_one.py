with open("input.txt") as file:
    puzzle_input = file.read().strip().splitlines()

heightmap = [list(x) for x in puzzle_input]

risk_level = 0

for row_index, row in enumerate(heightmap):
    for index, height in enumerate(row):
        adjacent = [int(height)]
        if row_index >= 1:
            adjacent.append(int(heightmap[row_index - 1][index]))
        if row_index < len(heightmap) - 1:
            adjacent.append(int(heightmap[row_index + 1][index]))
        if index >= 1:
            adjacent.append(int(row[index - 1]))
        if index < len(row) - 1:
            adjacent.append(int(row[index + 1]))
        if min(adjacent) == int(height) and adjacent.count(int(height)) == 1:
            risk_level += int(height) + 1

print(risk_level)
