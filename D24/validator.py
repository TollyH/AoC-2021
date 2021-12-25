with open("input.txt") as file:
    puzzle_input = file.read().strip().splitlines()

digit_params = [
    (
        int(puzzle_input[18 * (i + 1) - 14].split(" ")[-1]),
        int(puzzle_input[18 * (i + 1) - 13].split(" ")[-1]),
        int(puzzle_input[18 * (i + 1) - 3].split(" ")[-1])
    )
    for i in range(14)
]


def digit_calc(w, start_z, a, b, c):
    z = start_z
    x = int((z % 26) + b != w)
    z //= a
    z *= x * 25 + 1
    z += (w + c) * x
    return z


model = input("Enter model number to check > ")
previous_z = 0
for digit, params in zip(model, digit_params):
    previous_z = digit_calc(int(digit), previous_z, *params)

if not previous_z:
    print("Model number is valid")
else:
    print("Model number is not valid")
