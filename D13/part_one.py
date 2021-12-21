with open("input.txt") as file:
    puzzle_input = file.read().strip().split("\n\n")

paper_width = int(
    puzzle_input[1].splitlines()[0].split(" ")[2].split("=")[1]) * 2 + 1
paper_height = int(
    puzzle_input[1].splitlines()[1].split(" ")[2].split("=")[1]) * 2 + 1

coords = [
    tuple(map(int, x.split(',')))
    for x in puzzle_input[0].splitlines()
]
paper = [
    [False for _ in range(paper_width)] for _ in range(paper_height)
]
for x_coord, y_coord in coords:
    paper[y_coord][x_coord] = True

fold_direction = puzzle_input[1].splitlines()[0].split(" ")[2].split("=")[0]
fold_position = int(
    puzzle_input[1].splitlines()[0].split(" ")[2].split("=")[1]
)
if fold_direction == 'x':
    for row_index, row in enumerate(paper):
        for column_index in range(fold_position + 1, len(row)):
            if row[column_index]:
                paper[row_index][len(row) - column_index - 1] = True
    paper = [x[:fold_position] for x in paper]
else:
    for row_index in range(fold_position + 1, len(paper)):
        for column_index, column in enumerate(paper[row_index]):
            if column:
                paper[len(paper) - row_index - 1][column_index] = True
    paper = paper[:fold_position]

print(sum(1 for x in paper for y in x if y))
