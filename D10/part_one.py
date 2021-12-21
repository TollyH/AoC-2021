with open("input.txt") as file:
    puzzle_input = file.read().strip().splitlines()

openers = {'(': ')', '[': ']', '{': '}', '<': '>'}
closers = {')': 3, ']': 57, '}': 1197, '>': 25137}

illegal_score = 0

for line in puzzle_input:
    expected = []
    for char in line:
        if char in openers:
            expected.append(openers[char])
        elif char == expected[-1]:
            expected = expected[:-1]
        else:
            illegal_score += closers[char]
            break

print(f"{illegal_score=}")
