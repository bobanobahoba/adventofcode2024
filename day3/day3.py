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


if __name__ == "__main__":
    print(day3part1(sys.argv[1]))
