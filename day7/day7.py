# equations = [(totals, [values]), ...]
def get_valid_total(equations, validation_method):
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