# equations = [(totals, [values]), ...]
def get_valid_total(equations):
    valid_total = 0
    for total, values in equations:
        if is_valid(total, values):
            valid_total += total
    return valid_total

def is_valid(total, values):
    if len(values) == 1:
        return total == values[0]
    else:
        new_values_plus = [values[0] + values[1]] + values[2:]
        new_values_times = [values[0] * values[1]] + values[2:]
        return is_valid(total, new_values_plus) or is_valid(total, new_values_times)