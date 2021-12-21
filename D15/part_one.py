with open("input.txt") as file:
    puzzle_input = file.read()

cavern = [[int(x) for x in y] for y in puzzle_input.splitlines()]

default_data = {"risk": float('inf'), "previous": None}

unvisited = {
    (x, y): default_data.copy()
    for y in range(len(cavern)) for x in range(len(cavern[y]))
}
visited = {}
unvisited[(0, 0)]["risk"] = 0

while len(unvisited) > 0:
    current_x, current_y = min(unvisited, key=lambda x: unvisited[x]["risk"])
    current_data = unvisited.pop((current_x, current_y))
    visited[(current_x, current_y)] = current_data

    if (current_x, current_y) == (len(cavern[-1]) - 1, len(cavern) - 1):
        break

    adjacent_coords = []
    if current_x >= 1:
        adjacent_coords.append((current_x - 1, current_y))
    if current_x < len(cavern[current_y]) - 1:
        adjacent_coords.append((current_x + 1, current_y))
    if current_y >= 1:
        adjacent_coords.append((current_x, current_y - 1))
    if current_y < len(cavern[current_y]) - 1:
        adjacent_coords.append((current_x, current_y + 1))

    for adjacent_x, adjacent_y in adjacent_coords:
        if (adjacent_x, adjacent_y) in visited:
            continue
        adjacent = unvisited[(adjacent_x, adjacent_y)]
        new_risk = current_data["risk"] + cavern[adjacent_y][adjacent_x]
        if new_risk < unvisited[(adjacent_x, adjacent_y)]["risk"]:
            adjacent["risk"] = new_risk
            adjacent["previous"] = (current_x, current_y)

final_path = []
current = (len(cavern[-1]) - 1, len(cavern) - 1)
while current is not None:
    final_path.insert(0, current)
    current = visited[current]["previous"]

print(sum(cavern[y][x] for x, y in final_path[1:]))
