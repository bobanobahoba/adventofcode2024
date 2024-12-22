import utils, sys

def day5part1(input_file):
    rules = {}
    updates = []

    rules_ended = False
    for line in utils.read_input(input_file):
        if line == '\n':
            rules_ended = True
        elif rules_ended:
            updates.append([int(x) for x in line.split()[0].split(',')])
        else:
            left, right = [int(x) for x in line.split()[0].split('|')]
            if left in rules:
                rules[left].append(right)
            else:
                rules[left] = [right]
    total_middles = 0
    for update in updates:
        if is_valid(update, rules):
            total_middles += update[int(len(update)/2)]
    return total_middles

def is_valid(update, rules):
    seens = []
    for page in update:
        if page in rules:
            current_rule = rules[page]
            for seen in seens:
                if seen in current_rule:
                    return False
        seens.append(page)
    return True




if __name__ == '__main__':
    print(day5part1(sys.argv[1]))