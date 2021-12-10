with open("input.txt") as file:
    puzzle_input = file.read().strip().splitlines()
    file.close()

openers = {'(': ')', '[': ']', '{': '}', '<': '>'}
closers = {')': 1, ']': 2, '}': 3, '>': 4}

scores = []

for line in puzzle_input:
    new_score = 0
    expected = []
    valid = True
    for char in line:
        if char in openers:
            expected.append(openers[char])
        elif char == expected[-1]:
            expected = expected[:-1]
        else:
            valid = False
            break
    if valid:
        for missing in reversed(expected):
            new_score *= 5
            new_score += closers[missing]
        scores.append(new_score)

median_score = sorted(scores)[(len(scores) + 1) // 2 - 1]

print(f"{median_score=}")
