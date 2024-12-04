import sys

import utils


def day3part1(input_file):
    input_lines = [str(line) for line in utils.read_input(input_file)]
    mul_str = 'mul('
    total = 0
    for input_line in input_lines:
        next_mul_index = input_line.find(mul_str)
        while next_mul_index != -1:
            next_comma_index = input_line.find(',', next_mul_index)
            if next_comma_index == -1:
                break
            next_endparen_index = input_line.find(')', next_comma_index)
            if next_endparen_index == -1:
                break
            first_num_length = next_comma_index - next_mul_index - 4
            second_num_length = next_endparen_index - next_comma_index - 1
            if 0 < first_num_length <= 3 and 0 < second_num_length <= 3:
                try:
                    left = int(input_line[next_mul_index + 4:next_comma_index])
                    right = int(input_line[next_comma_index + 1:next_endparen_index])
                    total += left * right
                except ValueError:
                    pass
            next_mul_index = input_line.find(mul_str, next_mul_index + 1)
    return total


def day3part2(input_file):
    input_lines = [str(line) for line in utils.read_input(input_file)]
    mul_str = 'mul('
    do_str = 'do()'
    dont_str = 'don\'t()'
    total = 0
    is_doing = True
    for input_line in input_lines:
        next_mul_index = input_line.find(mul_str)
        if is_doing:
            doing_toggle_str = dont_str
        else:
            doing_toggle_str = do_str
        next_doing_toggle = input_line.find(doing_toggle_str, 1)
        while next_mul_index != -1:
            while next_doing_toggle != -1 and next_doing_toggle < next_mul_index:
                is_doing = not is_doing
                if is_doing:
                    doing_toggle_str = dont_str
                else:
                    doing_toggle_str = do_str
                next_doing_toggle = input_line.find(doing_toggle_str, next_doing_toggle + 1)
            next_comma_index = input_line.find(',', next_mul_index)
            if next_comma_index == -1:
                break
            next_endparen_index = input_line.find(')', next_comma_index)
            if next_endparen_index == -1:
                break
            first_num_length = next_comma_index - next_mul_index - 4
            second_num_length = next_endparen_index - next_comma_index - 1
            if 0 < first_num_length <= 3 and 0 < second_num_length <= 3:
                try:
                    left = int(input_line[next_mul_index + 4:next_comma_index])
                    right = int(input_line[next_comma_index + 1:next_endparen_index])
                    if is_doing:
                        total += left * right
                except ValueError:
                    pass
            next_mul_index = input_line.find(mul_str, next_mul_index + 1)
    return total


if __name__ == "__main__":
    print(day3part2(sys.argv[1]))
