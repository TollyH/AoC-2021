with open("input.txt") as file:
    puzzle_input = file.read().strip().split("\n\n")
    file.close()

template = list(puzzle_input[0])
pairs = {
    x.split(" -> ")[0]: x.split(" -> ")[1]
    for x in puzzle_input[1].splitlines()
}

for _ in range(10):
    new_insertions = {}
    for i in range(len(template) - 1):
        pair_str = ''.join(template[i:i + 2])
        if pair_str in pairs:
            new_insertions[i + 1] = pairs[pair_str]
    for count, (index, element) in enumerate(new_insertions.items()):
        template.insert(index + count, element)

unique_elements = set(template)
counts = [template.count(x) for x in unique_elements]

print(max(counts) - min(counts))
