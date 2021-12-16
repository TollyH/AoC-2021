with open("input.txt") as file:
    puzzle_input = file.read().strip()
    file.close()

full_string = ""
for hex_char in puzzle_input:
    full_string += format(int(hex_char, 16), '04b')


def parse_packets(binary_string, packet_limit=None):
    bit_counter = 0
    packet_version_total = 0
    parsed_count = 0
    while (bit_counter < len(binary_string)
            and (packet_limit is None or parsed_count < packet_limit)
            and len(binary_string) - bit_counter > 6
            and len(binary_string[bit_counter:].replace("0", "")) > 0):
        packet_version = int(binary_string[bit_counter:bit_counter + 3], 2)
        bit_counter += 3
        packet_version_total += packet_version
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
            packet_literal = int(literal_string, 2)
        else:  # Operator
            length_id = bool(int(binary_string[bit_counter], 2))
            bit_counter += 1
            if length_id:
                sub_packet_count = int(
                    binary_string[bit_counter:bit_counter + 11], 2
                )
                bit_counter += 11
                packet_version_res, counted_bits = parse_packets(
                    binary_string[bit_counter:], sub_packet_count
                )
                packet_version_total += packet_version_res
                bit_counter += counted_bits
            else:
                sub_bits_count = int(
                    binary_string[bit_counter:bit_counter + 15], 2
                )
                bit_counter += 15
                packet_version_total += parse_packets(
                    binary_string[bit_counter:bit_counter + sub_bits_count]
                )[0]
                bit_counter += sub_bits_count
    return packet_version_total, bit_counter


print(parse_packets(full_string)[0])
