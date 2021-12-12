with open("input.txt") as file:
    puzzle_input = file.read().strip().splitlines()
    file.close()

pairs = [tuple(x.split("-")) for x in puzzle_input]

connection_map = {}
for pair in pairs:
    if pair[0] not in connection_map:
        connection_map[pair[0]] = [pair[1]]
    else:
        connection_map[pair[0]].append(pair[1])
    if pair[1] not in connection_map:
        connection_map[pair[1]] = [pair[0]]
    else:
        connection_map[pair[1]].append(pair[0])


def visited_small_twice(path):
    for cave in path:
        if cave.islower() and path.count(cave) == 2:
            return True
    return False


def path_find(current_path):
    valid_paths = []
    for target in connection_map[current_path[-1]]:
        if target == "end":
            valid_paths.append(current_path + [target])
            continue
        if target == "start":
            continue
        if (target.islower() and target in current_path and
                visited_small_twice(current_path)):
            continue
        valid_paths += path_find(current_path + [target])
    return valid_paths


print(len(path_find(["start"])))
