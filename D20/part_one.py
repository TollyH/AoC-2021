with open("input.txt") as file:
    puzzle_input = file.read().strip().split("\n\n")
    file.close()


def copy(to_copy):
    new = []
    for item in to_copy:
        if isinstance(item, list):
            new.append(copy(item))
        else:
            new.append(item)
    return new


enhancement = [x == "#" for x in puzzle_input[0]]
input_image = [[x == "#" for x in y] for y in puzzle_input[1].splitlines()]
output_image = [
    [False for _ in input_image[0]]
    for _ in input_image
]

for i in range(2):
    default = i % 2 == 1 if enhancement[0] else False
    for y in range(len(output_image)):
        output_image[y] = [default] + output_image[y] + [default]
    output_image.insert(0, [default for _ in output_image[0]])
    output_image.append(
        [default for _ in output_image[0]]
    )
    for y in range(len(output_image)):
        for x in range(len(output_image[0])):
            bin_string = ""
            for input_y in range(-1, 2):
                target_y = y + input_y
                for input_x in range(-1, 2):
                    target_x = x + input_x
                    if target_y < 1 or target_y > len(input_image):
                        row = [default for _ in input_image[0]]
                    else:
                        row = input_image[target_y - 1]
                    if target_x < 1 or target_x > len(input_image):
                        bin_string += '1' if default else '0'
                    else:
                        bin_string += '1' if row[target_x - 1] else '0'
            enhancement_index = int(bin_string, 2)
            output_image[y][x] = enhancement[enhancement_index]
    input_image = copy(output_image)

print([x for y in output_image for x in y].count(True))
