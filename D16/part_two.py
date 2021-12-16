with open("input.txt") as file:
    puzzle_input = file.read().strip()
    file.close()

full_string = ""
for hex_char in puzzle_input:
    full_string += format(int(hex_char, 16), '04b')


def parse_packets(binary_string, packet_limit=None):
    bit_counter = 0
    parsed_count = 0
    values = []
    while (bit_counter < len(binary_string)
            and (packet_limit is None or parsed_count < packet_limit)
            and len(binary_string) - bit_counter > 6
            and len(binary_string[bit_counter:].replace("0", "")) > 0):
        parsed_count += 1
        packet_version = int(binary_string[bit_counter:bit_counter + 3], 2)
        bit_counter += 3
        packet_type = int(binary_string[bit_counter:bit_counter + 3], 2)
        bit_counter += 3
        if packet_type == 4:  # Literal value
            literal_string = ""
            continue_parse = True
            while continue_parse:
                continue_parse = bool(int(binary_string[bit_counter], 2))
                bit_counter += 1
                literal_string += binary_string[bit_counter: bit_counter + 4]
                bit_counter += 4
            values.append(int(literal_string, 2))
        else:  # Operator
            length_id = bool(int(binary_string[bit_counter], 2))
            bit_counter += 1
            if length_id:
                sub_packet_count = int(
                    binary_string[bit_counter:bit_counter + 11], 2
                )
                bit_counter += 11
                contained_values, counted_bits = parse_packets(
                    binary_string[bit_counter:], sub_packet_count
                )
                bit_counter += counted_bits
            else:
                sub_bits_count = int(
                    binary_string[bit_counter:bit_counter + 15], 2
                )
                bit_counter += 15
                contained_values = parse_packets(
                    binary_string[bit_counter:bit_counter + sub_bits_count]
                )[0]
                bit_counter += sub_bits_count
            if packet_type == 0:  # Sum
                values.append(sum(contained_values))
            elif packet_type == 1:  # Product
                to_add = 1
                for val in contained_values:
                    to_add *= val
                values.append(to_add)
            elif packet_type == 2:  # Minimum
                values.append(min(contained_values))
            elif packet_type == 3:  # Maximum
                values.append(max(contained_values))
            elif packet_type == 5:  # Greater than
                values.append(int(contained_values[0] > contained_values[1]))
            elif packet_type == 6:  # Less than
                values.append(int(contained_values[0] < contained_values[1]))
            elif packet_type == 7:  # Equal to
                values.append(int(contained_values[0] == contained_values[1]))
    return values, bit_counter


print(parse_packets(full_string)[0][0])
