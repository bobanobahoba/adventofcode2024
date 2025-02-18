# equations = [(totals, [values]), ...]
def get_valid_total(input_lines, validation_method):
    equations = read_input(input_lines)
    valid_total = 0
    for total, values in equations:
        if validation_method(total, values):
            valid_total += total
    return valid_total

def is_valid(total, values):
    if len(values) == 1:
        return total == values[0]
    else:
        new_values_plus = [values[0] + values[1]] + values[2:]
        new_values_times = [values[0] * values[1]] + values[2:]
        return is_valid(total, new_values_plus) or is_valid(total, new_values_times)

def is_valid_with_concat(total, values):
    if len(values) == 1:
        return total == values[0]
    else:
        new_values_plus = [values[0] + values[1]] + values[2:]
        new_values_times = [values[0] * values[1]] + values[2:]
        new_values_concat = [int(str(values[0]) + str(values[1]))] + values[2:]
        return is_valid_with_concat(total, new_values_plus) or is_valid_with_concat(total, new_values_times) or is_valid_with_concat(total, new_values_concat)

def read_input(input_lines):
    total_arr, values_arr = [], []
    for line in input_lines:
        elements = line.strip().replace(':', '').split(' ')
        total, values = int(elements[0]), [int(elem) for elem in elements[1:]]
        total_arr.append(total)
        values_arr.append(values)
    return zip(total_arr, values_arr)