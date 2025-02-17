import utils, sys, day7

def day7part1(input_file):
    input_lines = utils.read_input(input_file)
    total_arr, values_arr = [], []
    for line in input_lines:
        elements = line.strip().replace(':', '').split(' ')
        total, values = int(elements[0]), [int(elem) for elem in elements[1:]]
        total_arr.append(total)
        values_arr.append(values)
    return day7.get_valid_total(zip(total_arr, values_arr))

if __name__ == '__main__':
    print(day7part1(sys.argv[1]))