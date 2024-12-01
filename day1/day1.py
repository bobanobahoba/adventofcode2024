import utils


class Bst:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value > self.value:
            if self.right is None:
                self.right = Bst(value)
            else:
                self.right.insert(value)
        else:
            if self.left is None:
                self.left = Bst(value)
            else:
                self.left.insert(value)

    # inorder traversal
    def generate(self):
        if self.left is not None:
            yield from self.left.generate()
        yield self.value
        if self.right is not None:
            yield from self.right.generate()

    def count(self, value):
        total = 0
        if self.value == value:
            total += 1
        if value > self.value and self.right is not None:
            total += self.right.count(value)
        elif self.left is not None:
            total += self.left.count(value)
        return total

def initialize_bsts():
    problem_input = utils.read_input("../input/day1input.txt")
    left_bst, right_bst = map(Bst, map(int, problem_input[0].split()))
    for line in problem_input[1:]:
        left, right = map(int, line.split())
        left_bst.insert(left)
        right_bst.insert(right)
    return left_bst, right_bst

def day1part1():
    left_bst, right_bst = initialize_bsts()
    left_gen, right_gen = left_bst.generate(), right_bst.generate()
    distance = 0
    for left_val in left_gen:
        right_val = next(right_gen)
        distance += abs(left_val - right_val)
    print(distance)

def day1part2():
    left_bst, right_bst = initialize_bsts()
    total_similarity = 0
    for left_val in left_bst.generate():
        total_similarity += left_val * right_bst.count(left_val)
    print(total_similarity)

if __name__ == "__main__":
    day1part1()
    day1part2()