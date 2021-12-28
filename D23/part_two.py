import os

from PIL import Image

with open("input.txt") as file:
    puzzle_input = file.read().strip().splitlines()

if not os.path.isdir("output_part_two"):
    os.mkdir("output_part_two")

shape = """#############
#...........#
###.#.#.#.###
  #.#.#.#.#
  #.#.#.#.#
  #.#.#.#.#
  #########""".splitlines()
img_base = Image.new("RGB", (832, 448), (255, 255, 255))
for y, row in enumerate(shape):
    for x, char in enumerate(row):
        if char == "#":
            for ix in range(64):
                for iy in range(64):
                    img_base.putpixel((x * 64 + ix, y * 64 + iy), (0, 0, 0))

amphipods = ["A", "B", "C", "D"]
costs = [1, 10, 100, 1000]
addons = [["D", "D"], ["C", "B"], ["B", "A"], ["A", "C"]]

hallway = [None] * puzzle_input[1].count(".")
rooms = [
    [
        puzzle_input[2].strip().replace("#", "")[i],
        puzzle_input[3].strip().replace("#", "")[i]
    ]
    for i in range(4)
]
for i in range(4):
    for j in range(2):
        rooms[i].insert(j + 1, addons[i][j])


def get_possible_moves(current_hallway, current_rooms, current_pos,
                       current_room, letter):
    moves = {}
    move_addition = 0
    move_multiplier = costs[amphipods.index(letter)]
    if current_room is not None:
        if current_pos >= 1 and any(
                current_rooms[current_room][:current_pos]):
            return {}
        if current_pos == 3 and current_room == amphipods.index(letter):
            return {}
        if (current_pos < 3 and current_room == amphipods.index(letter)
                and current_rooms[current_room][current_pos:].count(letter) ==
                4 - current_pos):
            return {}
        if (current_hallway[1 + current_room * 2] is not None
                and current_hallway[3 + current_room * 2] is not None):
            return {}
        move_addition = current_pos + 1
        current_pos = 2 + current_room * 2

    for modifier in [-1, 1]:
        pos = current_pos + modifier
        count = 0
        while 0 <= pos < len(current_hallway) and current_hallway[pos] is None:
            if pos not in [2, 4, 6, 8] and move_addition != 0:
                moves[pos] = (count + 1 + move_addition) * move_multiplier
            elif pos in [2, 4, 6, 8]:
                next_room = pos // 2 - 1
                if next_room == amphipods.index(letter):
                    if (not all(current_rooms[next_room])
                            and current_rooms[next_room].count(letter) ==
                            len([
                                x for x in current_rooms[next_room]
                                if x is not None])):
                        next_free = 0
                        for index, item in reversed(
                                list(enumerate(current_rooms[next_room]))):
                            if item is None:
                                next_free = index
                                break
                        moves[(next_room, next_free)] = (
                            (count + next_free + 2 + move_addition)
                            * move_multiplier
                        )
            pos += modifier
            count += 1

    can_move_to_room = False
    for target in moves:
        if isinstance(target, tuple):
            can_move_to_room = True
            break
    if can_move_to_room:
        moves = {x: y for x, y in moves.items() if isinstance(x, tuple)}
    return moves


def perform_move(current_hallway, current_rooms, current_pos, current_room,
                 target_pos, target_room):
    new_hallway = current_hallway.copy()
    new_rooms = [x.copy() for x in current_rooms]
    if current_room is not None:
        to_move = current_rooms[current_room][current_pos]
        new_rooms[current_room][current_pos] = None
    else:
        to_move = current_hallway[current_pos]
        new_hallway[current_pos] = None
    if target_room is not None:
        new_rooms[target_room][target_pos] = to_move
    else:
        new_hallway[target_pos] = to_move
    return new_hallway, new_rooms


def path_find(state_hallway, state_rooms, current_energy, full_path):
    if not any(state_hallway):
        complete = True
        for index in range(4):
            if state_rooms[index].count(amphipods[index]) != 4:
                complete = False
                break
        if complete:
            energies.append(current_energy)
            return [current_energy], [full_path]
    new_energies = []
    valid_paths = []
    for room_index, room in enumerate(state_rooms):
        for inner_room_index, room_space in enumerate(room):
            if room_space is not None:
                for target, energy in get_possible_moves(
                        state_hallway, state_rooms, inner_room_index,
                        room_index, room_space).items():
                    if current_energy + energy < min(energies):
                        if isinstance(target, tuple):
                            resulting_hallway, resulting_rooms = perform_move(
                                state_hallway, state_rooms, inner_room_index,
                                room_index, target[1], target[0]
                            )
                            results = path_find(
                                resulting_hallway, resulting_rooms,
                                current_energy + energy,
                                full_path +
                                [(resulting_hallway, resulting_rooms)]
                            )
                            new_energies += results[0]
                            valid_paths += results[1]
                        else:
                            resulting_hallway, resulting_rooms = perform_move(
                                state_hallway, state_rooms, inner_room_index,
                                room_index, target, None
                            )
                            results = path_find(
                                resulting_hallway, resulting_rooms,
                                current_energy + energy,
                                full_path +
                                [(resulting_hallway, resulting_rooms)]
                            )
                            new_energies += results[0]
                            valid_paths += results[1]
    for hallway_index, hallway_space in enumerate(state_hallway):
        if hallway_space is not None:
            for target, energy in get_possible_moves(
                    state_hallway, state_rooms, hallway_index, None,
                    hallway_space).items():
                if current_energy + energy < min(energies):
                    if isinstance(target, tuple):
                        resulting_hallway, resulting_rooms = perform_move(
                            state_hallway, state_rooms, hallway_index, None,
                            target[1], target[0]
                        )
                        results = path_find(
                            resulting_hallway, resulting_rooms,
                            current_energy + energy,
                            full_path +
                            [(resulting_hallway, resulting_rooms)]
                        )
                        new_energies += results[0]
                        valid_paths += results[1]
                    else:
                        resulting_hallway, resulting_rooms = perform_move(
                            state_hallway, state_rooms, hallway_index, None,
                            target, None
                        )
                        results = path_find(
                            resulting_hallway, resulting_rooms,
                            current_energy + energy,
                            full_path +
                            [(resulting_hallway, resulting_rooms)]
                        )
                        new_energies += results[0]
                        valid_paths += results[1]
    return new_energies, valid_paths


energies = [100000]
result = path_find(hallway, rooms, 0, [(hallway, rooms)])

for frame, state in enumerate(result[1][result[0].index(min(result[0]))]):
    img = img_base.copy()
    for hall_index, hall_space in enumerate(state[0]):
        if hall_space == "A":
            colour = (209, 43, 31)
        elif hall_space == "B":
            colour = (66, 207, 48)
        elif hall_space == "C":
            colour = (46, 65, 191)
        elif hall_space == "D":
            colour = (191, 46, 186)
        else:
            continue
        for ix in range(64):
            for iy in range(64):
                img.putpixel((hall_index * 64 + 64 + ix, iy + 64), colour)
    for state_room_index, state_room in enumerate(state[1]):
        for room_space_index, room_item in enumerate(state_room):
            if room_item == "A":
                colour = (209, 43, 31)
            elif room_item == "B":
                colour = (66, 207, 48)
            elif room_item == "C":
                colour = (46, 65, 191)
            elif room_item == "D":
                colour = (191, 46, 186)
            else:
                continue
            for ix in range(64):
                for iy in range(64):
                    img.putpixel(
                        (
                            state_room_index * 128 + ix + 192,
                            room_space_index * 64 + iy + 128
                        ),
                        colour
                    )
    img.save(f"output_part_two/{frame:04d}.png")

os.system(
    "ffmpeg -f image2 -framerate 1 -i output_part_two/%04d.png part_two.gif"
)

print(min(result[0]))
