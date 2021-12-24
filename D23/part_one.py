with open("input.txt") as file:
    puzzle_input = file.read().strip().splitlines()

amphipods = ["A", "B", "C", "D"]
costs = [1, 10, 100, 1000]

hallway = [None] * puzzle_input[1].count(".")
rooms = [
    [
        puzzle_input[2].strip().replace("#", "")[i],
        puzzle_input[3].strip().replace("#", "")[i]
    ]
    for i in range(4)
]


def get_possible_moves(current_hallway, current_rooms, current_pos,
                       current_room, letter):
    moves = {}
    move_addition = 0
    move_multiplier = costs[amphipods.index(letter)]
    if current_room is not None:
        if current_pos == 1 and current_rooms[current_room][0] is not None:
            return {}
        if current_pos == 1 and current_room == amphipods.index(letter):
            return {}
        if (current_pos == 0 and current_room == amphipods.index(letter)
                and current_rooms[current_room][1] == letter):
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
                    if current_rooms[next_room][1] is None:
                        moves[(next_room, 1)] = (
                            (count + 3 + move_addition) * move_multiplier
                        )
                    elif (current_rooms[next_room][0] is None
                            and current_rooms[next_room][1] ==
                            amphipods[next_room]):
                        moves[(next_room, 0)] = (
                            (count + 2 + move_addition) * move_multiplier
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


def path_find(state_hallway, state_rooms, current_energy):
    if not any(state_hallway):
        complete = True
        for i in range(4):
            if state_rooms[i].count(amphipods[i]) != 2:
                complete = False
                break
        if complete:
            energies.append(current_energy)
            return [current_energy]
    new_energies = []
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
                            new_energies += path_find(
                                resulting_hallway, resulting_rooms,
                                current_energy + energy
                            )
                        else:
                            resulting_hallway, resulting_rooms = perform_move(
                                state_hallway, state_rooms, inner_room_index,
                                room_index, target, None
                            )
                            new_energies += path_find(
                                resulting_hallway, resulting_rooms,
                                current_energy + energy
                            )
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
                        new_energies += path_find(
                            resulting_hallway, resulting_rooms,
                            current_energy + energy
                        )
                    else:
                        resulting_hallway, resulting_rooms = perform_move(
                            state_hallway, state_rooms, hallway_index, None,
                            target, None
                        )
                        new_energies += path_find(
                            resulting_hallway, resulting_rooms,
                            current_energy + energy
                        )
    return new_energies


energies = [100000]
print(min(path_find(hallway, rooms, 0)))
