with open("input.txt") as file:
    puzzle_input = (file.read().strip().replace("  ", " ")
                    .replace("\n ", "\n").split("\n\n"))
    file.close()


def check_win(matrix, numbers):
    for horizontal in board:
        if set(horizontal).issubset(numbers):
            return True
    for vertical_index in range(len(matrix[0])):
        vertical = [x[vertical_index] for x in matrix]
        if set(vertical).issubset(numbers):
            return True
    return False


random_sequence = [int(x) for x in puzzle_input[0].split(",")]
boards = [
    [
        [int(x) for x in y.split(" ")]
        for y in z.split("\n")
    ]
    for z in puzzle_input[1:]
]

drawn_numbers = []

for draw in random_sequence:
    drawn_numbers.append(draw)
    if len(drawn_numbers) >= 5:
        has_won = False
        for board in boards:
            if check_win(board, drawn_numbers):
                has_won = True
                total_unmarked = sum(
                    [x for y in board for x in y if x not in drawn_numbers]
                )
                print(f"{total_unmarked * draw=}")
                break
        if has_won:
            break
