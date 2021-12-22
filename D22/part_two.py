with open("input.txt") as file:
    puzzle_input = file.read().strip().splitlines()


def does_overlap(cube_1_x, cube_1_y, cube_1_z, cube_2_x, cube_2_y, cube_2_z):
    return (
        cube_1_x[1] >= cube_2_x[0]
        and cube_1_x[0] <= cube_2_x[1]
        and cube_1_y[1] >= cube_2_y[0]
        and cube_1_y[0] <= cube_2_y[1]
        and cube_1_z[1] >= cube_2_z[0]
        and cube_1_z[0] <= cube_2_z[1]
    )


def get_overlap(cube_1_x, cube_1_y, cube_1_z,
                cube_2_x, cube_2_y, cube_2_z):
    return (
        (max(cube_1_x[0], cube_2_x[0]), min(cube_1_x[1], cube_2_x[1])),
        (max(cube_1_y[0], cube_2_y[0]), min(cube_1_y[1], cube_2_y[1])),
        (max(cube_1_z[0], cube_2_z[0]), min(cube_1_z[1], cube_2_z[1]))
    )


cubes = {}

for line in puzzle_input:
    x_bounds, y_bounds, z_bounds = (
        tuple(sorted(map(int, x.split("=")[1].split(".."))))
        for x in line.split(",")
    )
    overlapping = [
        (x, y, z, c) for (x, y, z), c in cubes.items()
        if does_overlap(x_bounds, y_bounds, z_bounds, x, y, z)
    ]
    for comp_x_bounds, comp_y_bounds, comp_z_bounds, count in overlapping:
        overlap_cube = get_overlap(
            x_bounds, y_bounds, z_bounds,
            comp_x_bounds, comp_y_bounds, comp_z_bounds
        )
        if overlap_cube in cubes:
            cubes[overlap_cube] -= count
        else:
            cubes[overlap_cube] = -count
    if line.startswith("on"):
        if (x_bounds, y_bounds, z_bounds) in cubes:
            cubes[(x_bounds, y_bounds, z_bounds)] += 1
        else:
            cubes[x_bounds, y_bounds, z_bounds] = 1

total = 0
for (x_bounds, y_bounds, z_bounds), count in cubes.items():
    total += (
        (x_bounds[1] - x_bounds[0] + 1)
        * (y_bounds[1] - y_bounds[0] + 1)
        * (z_bounds[1] - z_bounds[0] + 1)
        * count
    )

print(total)
