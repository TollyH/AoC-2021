with open("input.txt") as file:
    puzzle_input = file.read().strip().splitlines()
    file.close()

oxygen_gen_rate_list = puzzle_input.copy()
c02_scrub_rate_list = puzzle_input.copy()

for column in range(len(puzzle_input[0])):
    oxygen_bits = [x[column] for x in oxygen_gen_rate_list]
    c02_bits = [x[column] for x in c02_scrub_rate_list]

    if oxygen_bits.count('1') != len(oxygen_bits) / 2:
        most_common = max(('0', '1'), key=oxygen_bits.count)
    else:
        most_common = '1'

    if c02_bits.count('0') != len(c02_bits) / 2:
        least_common = min(('0', '1'), key=c02_bits.count)
    else:
        least_common = '0'

    if len(oxygen_gen_rate_list) != 1:
        oxygen_gen_rate_list = [
            x for x in oxygen_gen_rate_list if x[column] == most_common
        ]
    if len(c02_scrub_rate_list) != 1:
        c02_scrub_rate_list = [
            x for x in c02_scrub_rate_list if x[column] == least_common
        ]

oxygen_gen_rate = int(oxygen_gen_rate_list[0], 2)
c02_scrub_rate = int(c02_scrub_rate_list[0], 2)

print(
    f"{oxygen_gen_rate=} {c02_scrub_rate=}\n" +
    f"{oxygen_gen_rate * c02_scrub_rate=}"
)
