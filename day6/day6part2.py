import sys, utils, day6utils

def day6part2(input_file):
    input_lines = utils.read_input(input_file)
    return day6utils.count_loops(input_lines)

if __name__ == "__main__":
    print(day6part2(sys.argv[1]))