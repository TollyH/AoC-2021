with open("input.txt") as file:
    puzzle_input = file.read().strip().splitlines()

p1_location, p2_location = (int(x.split(": ")[1]) for x in puzzle_input)


def offset_modulo(num1, num2, offset):
    return num1 - num2 * int((num1 - offset) / num2)


cache = {}


def simulate_round(p1_score, p2_score, p1_pos, p2_pos):
    if p1_score >= 21:
        return 1, 0
    if p2_score >= 21:
        return 0, 1
    if (p1_score, p2_score, p1_pos, p2_pos) in cache:
        return cache[(p1_score, p2_score, p1_pos, p2_pos)]
    wins = (0, 0)
    for i in range(1, 4):
        for j in range(1, 4):
            for k in range(1, 4):
                new_pos = offset_modulo(p1_pos + i + j + k, 10, 1)
                result = simulate_round(
                    p2_score + new_pos, p1_score, p2_pos, new_pos
                )
                wins = (wins[0] + result[1], wins[1] + result[0])
    cache[(p1_score, p2_score, p1_pos, p2_pos)] = wins
    return wins


print(max(simulate_round(0, 0, p1_location, p2_location)))
