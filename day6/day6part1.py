import sys, utils, day6utils

def day6part1(input_file):
    input_lines = utils.read_input(input_file)
    return day6utils.get_path(input_lines)

if __name__ == "__main__":
    print(day6part1(sys.argv[1]))