with open("input.txt") as file:
    puzzle_input = file.read().strip().split("\n\n")
    file.close()

template = list(puzzle_input[0])
unique_elements = {
    x.split(" -> ")[1]: 0 for x in puzzle_input[1].splitlines()
}
pairs = {
    x.split(" -> ")[0]: x.split(" -> ")[1]
    for x in puzzle_input[1].splitlines()
}
current_pairs = {x + y: 0 for x in unique_elements for y in unique_elements}

for element in template:
    unique_elements[element] += 1

for i in range(len(template) - 1):
    current_pairs[''.join(template[i:i + 2])] += 1

for _ in range(40):
    additions = {x: 0 for x in current_pairs}
    for pair, addition in pairs.items():
        unique_elements[addition] += current_pairs[pair]
        additions[pair[0] + addition] += current_pairs[pair]
        additions[addition + pair[1]] += current_pairs[pair]
        current_pairs[pair] = 0
    for pair, value in additions.items():
        current_pairs[pair] += value

print(max(unique_elements.values()) - min(unique_elements.values()))
