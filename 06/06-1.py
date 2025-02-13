import copy


def read_data(PATH: str):
    pages_to_produce = []
    with open(PATH, "r") as file:
        for line in file:
            temp_row = list(line.strip("\n"))
            pages_to_produce.append(temp_row)
    return pages_to_produce


def find_starting_position(data: list):
    for row in range(len(data)):
        for column in range(len(data[0])):
            if (
                data[row][column] == "^"
                or data[row][column] == "<"
                or data[row][column] == ">"
                or data[row][column] == "v"
            ):
                start_id = [row, column]
                break
    return start_id


def determine_starting_direction(start_char: str):
    direction = ""
    if start_char == "^":
        direction = "up"
    elif start_char == ">":
        direction = "right"
    elif start_char == "v":
        direction = "down"
    elif start_char == "<":
        direction = "left"
    return direction


def move_till_collision(data: list, position: list, direction, end_of_search: bool):

    positions_visited = []
    end_of_search = False
    character = data[position[0]][position[1]]
    match direction:
        case "up":
            while character != "#":
                try:
                    position[0] -= 1
                    character = data[position[0]][position[1]]
                    if position[0] < 0:
                        raise IndexError
                except:
                    end_of_search = True
                    position[0] += 1
                    break
                else:
                    if character != "#":
                        positions_visited.append(position.copy())
                    else:
                        direction = "right"
                        position[0] += 1
                        break

        case "right":
            while character != "#":
                try:
                    position[1] += 1
                    character = data[position[0]][position[1]]
                except:
                    end_of_search = True
                    break
                else:
                    if character != "#":
                        positions_visited.append(position.copy())
                    else:
                        direction = "down"
                        position[1] -= 1
                        break

        case "down":
            while character != "#":
                try:
                    position[0] += 1
                    character = data[position[0]][position[1]]
                except:
                    end_of_search = True
                    break
                else:
                    if character != "#":
                        positions_visited.append(position.copy())
                    else:
                        direction = "left"
                        position[0] -= 1
                        break

        case "left":
            while character != "#":
                try:
                    position[1] -= 1
                    character = data[position[0]][position[1]]
                    if position[1] < 0:
                        raise IndexError
                except:
                    end_of_search = True
                    position[1] += 1
                    break
                else:
                    if character != "#":
                        positions_visited.append(position.copy())
                    else:
                        direction = "up"
                        position[1] += 1
                        break
    return direction, positions_visited, end_of_search, position


PATH = "/home/jonas/coding_practice/advent_of_code/06/input.txt"
data = read_data(PATH)

start_row, start_column = find_starting_position(data)
direction = determine_starting_direction(data[start_row][start_column])

current_postion = [start_row, start_column]
all_positions = []
all_positions.append(copy.deepcopy(current_postion))

i = 0
end_of_search = False

loop_counter = 0

while end_of_search is not True:
    direction, positions_visited, end_of_search, position = move_till_collision(
        data, current_postion, direction, False
    )
    all_positions.extend(positions_visited)
    all_positions = [list(x) for x in set(tuple(x) for x in all_positions)]
    current_postion = position
    i += 1


unique_positions = [list(x) for x in set(tuple(x) for x in all_positions)]
print(loop_counter)
