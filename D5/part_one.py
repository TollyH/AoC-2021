with open("input.txt") as file:
    puzzle_input = file.read().strip().splitlines()
    file.close()

points = [[]]

for line in puzzle_input:
    one = tuple(int(x) for x in line.split(" -> ")[0].split(","))
    two = tuple(int(x) for x in line.split(" -> ")[1].split(","))

    max_x_coord = max((one, two), key=lambda x: x[0])[0]
    max_y_coord = max((one, two), key=lambda x: x[1])[1]
    min_x_coord = min((one, two), key=lambda x: x[0])[0]
    min_y_coord = min((one, two), key=lambda x: x[1])[1]

    if max_y_coord > len(points) - 1:
        for _ in range(max_y_coord - len(points) + 1):
            points.append([0] * len(points[0]))

    if max_x_coord > len(points[0]) - 1:
        for row in points:
            for _ in range(max_x_coord - len(row) + 1):
                row.append(0)

    if one[0] == two[0]:
        for i in range(min_y_coord, max_y_coord + 1):
            points[i][one[0]] += 1
    elif one[1] == two[1]:
        for i in range(min_x_coord, max_x_coord + 1):
            points[one[1]][i] += 1

print(sum(1 for y in points for x in y if x > 1))
