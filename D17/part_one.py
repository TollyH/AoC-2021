with open("input.txt") as file:
    puzzle_input = file.read().strip().removeprefix("target area: ")

target_x_bounds, target_y_bounds = (
    tuple(map(int, x.split("=")[1].split("..")))
    for x in puzzle_input.split(", ")
)


def get_stop_points(init_x_velocity, init_y_velocity):
    probe_x = 0
    probe_y = 0
    x_velocity = init_x_velocity
    y_velocity = init_y_velocity
    points = []
    overshot = False
    while not overshot:
        probe_x += x_velocity
        probe_y += y_velocity
        points.append((probe_x, probe_y))
        if x_velocity > 0:
            x_velocity -= 1
        elif x_velocity < 0:
            x_velocity += 1
        y_velocity -= 1

        if probe_x > max(target_x_bounds):
            overshot = True
        if y_velocity < 0 and probe_y < min(target_y_bounds):
            overshot = True
    return points


valid_velocities = {}
for x in range(max(target_x_bounds) + 1):
    for y in range(min(target_y_bounds) - 1, abs(min(target_y_bounds)) + 1):
        stops = get_stop_points(x, y)
        for point in stops:
            if (point[0] >= target_x_bounds[0]
                    and point[0] <= target_x_bounds[1]
                    and point[1] >= target_y_bounds[0]
                    and point[1] <= target_y_bounds[1]):
                valid_velocities[(x, y)] = max(stops, key=lambda x: x[1])[1]
                break

best_velocity = max(valid_velocities, key=lambda x: valid_velocities[x])
print(valid_velocities[best_velocity])
