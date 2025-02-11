import utils, sys

directions = ['^', '>', 'v', '<']

def day6part1(input_file):
    input_lines = utils.read_input(input_file)
    return get_path(input_lines)

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
            if area_map[row][col] in directions:
                return directions.index(area_map[row][col]), (row, col)

def get_next(area_map, info):
    direction, location = info[0], info[1]
    if direction == 0:
        next_location = (location[0] - 1, location[1])
    elif direction == 1:
        next_location = (location[0], location[1] + 1)
    elif direction == 2:
        next_location = (location[0] + 1, location[1])
    else:
        next_location = (location[0], location[1] - 1)
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


if __name__ == "__main__":
    print(day6part1(sys.argv[1]))