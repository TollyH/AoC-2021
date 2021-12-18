def parse_snailfish_number(string):
    raw_num = string.removeprefix("[").removesuffix("]")
    raw_contained = []
    open_brackets = 0
    last_insert = 0
    for i, char in enumerate(raw_num):
        if char == "[":
            open_brackets += 1
        elif char == "]":
            open_brackets -= 1
        elif char == "," and open_brackets == 0:
            raw_contained.append(raw_num[last_insert:i])
            last_insert = i + 1
    raw_contained.append(raw_num[last_insert:])
    contained = []
    for item in raw_contained:
        if item.isnumeric():
            contained.append(int(item))
        else:
            contained.append(parse_snailfish_number(item))
    return contained


def get_all_indices(num, current):
    indices = []
    for index, item in enumerate(num):
        if isinstance(item, list):
            indices += get_all_indices(item, current + [index])
        else:
            indices.append(current + [index])
    return indices


def search_list_of_lists(source, target):
    for index, item in enumerate(source):
        if item == target:
            return index
    raise ValueError


def explode(num, full_num, indices):
    if len(indices) >= 4:
        all_indices = get_all_indices(full_num, [])
        first_num_index = search_list_of_lists(all_indices, indices + [0])
        second_num_index = search_list_of_lists(all_indices, indices + [1])
        if first_num_index >= 1:
            prev_indices = all_indices[first_num_index - 1]
            prev_item = full_num
            for prev_index in prev_indices[:-1]:
                prev_item = prev_item[prev_index]
            prev_item[prev_indices[-1]] += num[0]
        if second_num_index < len(all_indices) - 1:
            next_indices = all_indices[second_num_index + 1]
            next_item = full_num
            for next_index in next_indices[:-1]:
                next_item = next_item[next_index]
            next_item[next_indices[-1]] += num[1]
        full_item = full_num
        for index in indices[:-1]:
            full_item = full_item[index]
        full_item[indices[-1]] = 0
        return True
    for index, item in enumerate(num):
        if isinstance(item, list):
            if explode(item, full_num, indices + [index]):
                return True
    return False


def split(num):
    for index, item in enumerate(num):
        if isinstance(item, list):
            if split(item):
                return True
        elif item >= 10:
            num[index] = [item // 2, item // 2 + item % 2]
            return True
    return False


def reduce_snailfish_number(num):
    performed_operation = explode(num, num, [])
    if not performed_operation:
        performed_operation = split(num)

    if not performed_operation:
        return num
    return reduce_snailfish_number(num)


def calculate_magnitude(num):
    if isinstance(num, int):
        return num
    magnitude_total = 0
    for index, item in enumerate(num):
        if index == 0:
            magnitude_total += 3 * calculate_magnitude(item)
        else:
            magnitude_total += 2 * calculate_magnitude(item)
    return magnitude_total


def copy(to_copy):
    new = []
    for item in to_copy:
        if isinstance(item, list):
            new.append(copy(item))
        else:
            new.append(item)
    return new


with open("input.txt") as file:
    puzzle_input = file.read().strip().splitlines()

sf_numbers = []
for sf_num in puzzle_input:
    sf_numbers.append(parse_snailfish_number(sf_num))

results = []
for index_a, num_a in enumerate(sf_numbers):
    for index_b, num_b in enumerate(sf_numbers):
        if index_a != index_b:
            results.append(calculate_magnitude(
                reduce_snailfish_number([copy(num_a), copy(num_b)])))

print(max(results))
