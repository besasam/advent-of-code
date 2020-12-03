import math


def sled(trees, right, down):
    height = len(trees)
    width = len(trees[0])
    count = x = y = 0
    while y < height - down:
        x = (x + right) % width
        y += down
        if trees[y][x]:
            count += 1
    return count


def part_2(trees):
    return math.prod([sled(trees, 1, 1), sled(trees, 3, 1), sled(trees, 5, 1), sled(trees, 7, 1), sled(trees, 1, 2)])


with open('input.txt') as f:
    data = [[c == '#' for c in l] for l in f.read().splitlines()]

print(part_2(data))