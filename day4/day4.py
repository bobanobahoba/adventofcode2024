import utils, sys

XMAS = ['X', 'M', 'A', 'S']

def day4part1(input_file):
    input_lines = [x.split()[0] for x in utils.read_input(input_file)]
    total_xmas = 0
    for i in range(len(input_lines)):
        for j in range(len(input_lines[0])):
            total_xmas += count_xmas(input_lines, i, j)
    return total_xmas


def count_xmas(input_lines, i, j):
    xmas_count = 0
    for i_offset, j_offset in ij_generator():
        not_xmas = False
        for dist in range(0, 4):
            final_i = i + i_offset * dist
            final_j = j + j_offset * dist
            is_valid = 0 <= final_i < len(input_lines) and 0 <= final_j < len(input_lines[0])
            if not is_valid or (is_valid and input_lines[final_i][final_j] != XMAS[dist]):
                not_xmas = True
                break
        if not not_xmas:
            xmas_count += 1
    return xmas_count


def ij_generator():
    for i in range(-1, 2, 2):
        for j in range(-1, 2, 2):
            yield (i, j)
    for i in range(-1, 2, 2):
        yield (i, 0)
    for j in range(-1, 2, 2):
        yield (0, j)


if __name__ == '__main__':
    print(day4part1(sys.argv[1]))