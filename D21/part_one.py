with open("input.txt") as file:
    puzzle_input = file.read().strip().splitlines()

p1_location, p2_location = (int(x.split(": ")[1]) for x in puzzle_input)

p1_score = 0
p2_score = 0


def offset_modulo(num1, num2, offset):
    return num1 - num2 * int((num1 - offset) / num2)


rolls = 1
turns = 0
while p1_score < 1000 and p2_score < 1000:
    if turns % 2 == 0:
        places = 0
        for i in range(3):
            places += offset_modulo(rolls + i, 100, 1)
        p1_location = offset_modulo(p1_location + places, 10, 1)
        p1_score += p1_location
    else:
        places = 0
        for i in range(3):
            places += offset_modulo(rolls + i, 100, 1)
        p2_location = offset_modulo(p2_location + places, 10, 1)
        p2_score += p2_location
    rolls += 3
    turns += 1

print(min(p1_score, p2_score) * (rolls - 1))
