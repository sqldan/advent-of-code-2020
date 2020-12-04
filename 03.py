from functools import reduce

lines = []
with open("input03.txt") as f:
    lines = f.read().splitlines()

height = len(lines)
width = len(lines[0])


def count_trees(slope):
    trees = x = 0
    right, down = slope
    for y in range(1, height, down):
        x = (x + right) % width
        if lines[y][x] == "#":
            trees += 1
    return trees

solution1 = count_trees((3, 1))
print("solution1:", solution1)

solution2 = map(count_trees, ((1, 1), (3,1), (5, 1), (7, 1), (1, 2)))
print("solution2:", reduce(lambda x, y: x*y, list(solution2)))