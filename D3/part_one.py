with open("input.txt") as file:
    puzzle_input = file.read().strip().splitlines()
    file.close()

gamma_rate_str = ''
epsilon_rate_str = ''

for column in range(len(puzzle_input[0])):
    all_bits = [x[column] for x in puzzle_input]
    gamma_rate_str += max(('0', '1'), key=all_bits.count)
    epsilon_rate_str += min(('0', '1'), key=all_bits.count)

gamma_rate = int(gamma_rate_str, 2)
epsilon_rate = int(epsilon_rate_str, 2)

print(f"{gamma_rate=} {epsilon_rate=}\n{gamma_rate * epsilon_rate=}")
