with open("input.txt") as file:
    puzzle_input = file.read().splitlines()

cucumbers = [list(x) for x in puzzle_input]
new_cucumbers = None

counter = 0
performed_move = True
while performed_move:
    new_cucumbers = [x.copy() for x in cucumbers]
    performed_move = False
    for row_index, row in enumerate(cucumbers):
        for index, cucumber in enumerate(row):
            if cucumber == ">" and row[(index + 1) % len(row)] == ".":
                new_cucumbers[row_index][index] = "."
                new_cucumbers[row_index][(index + 1) % len(row)] = ">"
                performed_move = True
    cucumbers = [x.copy() for x in new_cucumbers]
    for row_index, row in enumerate(cucumbers):
        for index, cucumber in enumerate(row):
            if (cucumber == "v"
                    and cucumbers[(row_index + 1) % len(cucumbers)][index]
                    == "."):
                new_cucumbers[row_index][index] = "."
                new_cucumbers[(row_index + 1) % len(cucumbers)][index] = "v"
                performed_move = True
    cucumbers = [x.copy() for x in new_cucumbers]
    counter += 1

print(counter)
