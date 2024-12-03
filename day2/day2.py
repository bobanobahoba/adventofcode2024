import utils


def day2part1():
    input_lines = utils.read_input('../input/day2input.txt').split()
    safe_lines = 0
    for input_line in input_lines:
        line = list(int(x) for x in input_line.split())
        if is_safe(line):
            safe_lines += 1
            print(line + ' - safe')
        else:
            print(line + ' - not')
    print(safe_lines)


def day2part2():
    input_lines = utils.read_input('../input/day2input.txt')
    safe_lines = 0
    for input_line in input_lines:
        line = list(int(x) for x in input_line.split())
        for permutation in generate_permutations(line):
            if is_safe(permutation):
                safe_lines += 1
                break
    print(safe_lines)


def generate_permutations(line):
    for i in range(len(line)):
        yield line[0:i] + line[i+1:]


def is_safe(line):
    value = line[0]
    is_increasing = None
    for i in range(1, len(line)):
        next_value = line[i]
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
    day2part2()
