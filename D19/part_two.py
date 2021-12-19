with open("input.txt") as file:
    puzzle_input = file.read().strip().split("\n\n")
    file.close()


def rotate_point(point, x_rot, y_rot, z_rot):
    new_point = point
    for _ in range(x_rot):
        new_point = (new_point[0], -new_point[2], new_point[1])
    for _ in range(y_rot):
        new_point = (new_point[2], new_point[1], -new_point[0])
    for _ in range(z_rot):
        new_point = (-new_point[1], new_point[0], new_point[2])
    return new_point


def transform_point(point, x_pos, y_pos, z_pos):
    return (point[0] + x_pos, point[1] + y_pos, point[2] + z_pos)


def calculate_distance(point1, point2):
    return (abs(point1[0] - point2[0])
            + abs(point1[1] - point2[1])
            + abs(point1[2] - point2[2]))


all_scans = [
    {tuple(map(int, x.split(","))) for x in y.splitlines()[1:]}
    for y in puzzle_input
]
beacons = all_scans[0]
completed_scanners = {0: (0, 0, 0)}

while len(completed_scanners) < len(all_scans):
    for index, scan in enumerate(all_scans[1:]):
        if index + 1 in completed_scanners:
            continue
        for xro in range(4):
            for yro in range(4):
                for zro in range(4):
                    rotated_points = set(
                        map(lambda p: rotate_point(p, xro, yro, zro), scan)
                    )
                    differences = {}
                    for pt1 in beacons:
                        for pt2 in rotated_points:
                            dif = (
                                pt1[0] - pt2[0],
                                pt1[1] - pt2[1],
                                pt1[2] - pt2[2]
                            )
                            if dif in differences:
                                differences[dif] += 1
                            else:
                                differences[dif] = 1
                    max_similar = max(
                        differences, key=lambda d: differences[d]
                    )
                    if differences[max_similar] >= 12:
                        for pnt in rotated_points:
                            beacons.add(transform_point(pnt, *max_similar))
                        completed_scanners[index + 1] = max_similar

distances = [
    calculate_distance(x, y)
    for x in completed_scanners.values()
    for y in completed_scanners.values()
]

print(max(distances))
