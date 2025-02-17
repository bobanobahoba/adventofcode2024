directions_ordered = ['^', '>', 'v', '<']
direction_vector = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}

# infos are TUPLE OF (DIRECTION INDEX, TUPLE OF (LOCATION))

def get_path(area_map):
    visited_locations = set()
    next_info = get_start_info(area_map)
    while next_info is not None:
        visited_locations.add(next_info[1])
        next_info = get_next(area_map, next_info)
    return len(visited_locations)

def get_start_info(area_map):
    for row in range(len(area_map)):
        for col in range(len(area_map[0])):
            if area_map[row][col] in directions_ordered:
                return directions_ordered.index(area_map[row][col]), (row, col)

def get_next(area_map, info):
    direction, location = info[0], info[1]
    next_location = (location[0] + direction_vector[direction][0], location[1] + direction_vector[direction][1])
    if not validate(area_map, next_location):
        return None
    elif area_map[next_location[0]][next_location[1]] == '#':
        return (direction + 1) % 4, location
    else:
        return direction, next_location

def validate(area_map, location):
    if location[0] < 0 or location[0] >= len(area_map):
        return False
    elif location[1] < 0 or location[1] >= len(area_map[0]):
        return False
    else:
        return True

def count_loops(area_map):
    loops = 0
    for row in range(len(area_map)):
        for col in range(len(area_map[0])):
            temp_area_map = area_map.copy()
            if temp_area_map[row][col] == '#' or temp_area_map[row][col] in direction_vector:
                continue
            else:
                temp_area_map[row] = temp_area_map[row][:col] + '#' + temp_area_map[row][col + 1:]
                prev_infos = set()
                next_info = get_start_info(area_map)
                prev_infos.add(next_info)
                while next_info is not None:
                    next_info = get_next(temp_area_map, next_info)
                    if next_info in prev_infos:
                        loops += 1
                        break
                    prev_infos.add(next_info)
    return loops
