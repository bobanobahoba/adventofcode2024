import utils, sys, day7

def day7part2(input_file):
    input_lines = utils.read_input(input_file)
    return day7.get_valid_total(input_lines, day7.is_valid_with_concat)

if __name__ == '__main__':
    print(day7part2(sys.argv[1]))