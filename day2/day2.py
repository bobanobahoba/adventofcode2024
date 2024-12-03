import utils


def day2part1():
    input_lines = utils.read_input('../input/day2input.txt')
    safe_lines = 0
    for line in input_lines:
        if is_safe(line):
            safe_lines += 1
            print(line + ' - safe')
        else:
            print(line + ' - not')
    print(safe_lines)


def is_safe(line):
    processed_line = list(int(x) for x in line.split())
    value = processed_line[0]
    is_increasing = None
    for i in range(1, len(processed_line)):
        next_value = processed_line[i]
        if is_increasing is None:
            is_increasing = next_value > value
        if is_increasing:
            if not (1 <= next_value - value <= 3):
                return False
        else:
            if not (-3 <= next_value - value <= -1):
                return False
        value = next_value
    return True


if __name__ == "__main__":
    day2part1()
