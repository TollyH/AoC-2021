with open("input.txt") as file:
    puzzle_input = file.read().strip().splitlines()

output_sum = 0

for entry in puzzle_input:
    mapping = [set() for _ in range(10)]
    known_numbers = [
        x for x in entry.split(" | ")[0].split(" ")
        if len(x) in {2, 4, 3, 7}
    ]
    unknown_numbers = [
        x for x in entry.split(" | ")[0].split(" ")
        if len(x) not in {2, 4, 3, 7}
    ]
    for pattern in known_numbers:
        new_set = set(pattern)
        if len(pattern) == 2:
            mapping[1] = new_set
        elif len(pattern) == 4:
            mapping[4] = new_set
        elif len(pattern) == 3:
            mapping[7] = new_set
        elif len(pattern) == 7:
            mapping[8] = new_set
    for pattern in unknown_numbers:
        new_set = set(pattern)
        if len(pattern) == 5:
            if mapping[1].issubset(new_set):
                mapping[3] = new_set
            elif (mapping[4] - mapping[1]).issubset(new_set):
                mapping[5] = new_set
            else:
                mapping[2] = new_set
        elif len(pattern) == 6:
            if len(new_set - mapping[1]) == 5:
                mapping[6] = new_set
            elif len(new_set - mapping[4]) == 2:
                mapping[9] = new_set
            else:
                mapping[0] = new_set
    string_number = ""
    for output in entry.split(" | ")[1].split(" "):
        for number, segments in enumerate(mapping):
            if set(output) == segments:
                string_number += str(number)
                break
    output_sum += int(string_number)

print(f"{output_sum=}")
