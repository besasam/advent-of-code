import re


def get_occurences(haystack: list) -> int:
    return sum(sum(1 for _ in re.finditer('(?=XMAS)', line)) for line in haystack) + \
           sum(sum(1 for _ in re.finditer('(?=SAMX)', line)) for line in haystack)


def is_x_mas(grid: list, x: int, y: int) -> bool:
    if x == 0 or x == len(grid) - 1 or y == 0 or y == len(grid) - 1:
        return False
    return grid[y][x] == 'A' and \
           ((grid[y - 1][x - 1] == 'M' and grid[y + 1][x + 1] == 'S') or (grid[y - 1][x - 1] == 'S' and grid[y + 1][x + 1] == 'M')) and \
           ((grid[y + 1][x - 1] == 'M' and grid[y - 1][x + 1] == 'S') or (grid[y + 1][x - 1] == 'S' and grid[y - 1][x + 1] == 'M'))


def part_1(rows: list) -> int:
    width = len(rows)
    columns = [''.join(col) for col in zip(*rows)]
    major_diagonals = [''.join(row[i + offset] for i, row in enumerate(rows) if 0 <= i + offset < len(rows))
                       for offset in range(-width + 1, width)]
    minor_diagonals = [''.join(row[~i - offset] for i, row in enumerate(rows) if 0 <= i + offset < len(rows))
                       for offset in range(-width + 1, width)]
    return sum((get_occurences(rows), get_occurences(columns),
                get_occurences(major_diagonals), get_occurences(minor_diagonals)))


def part_2(grid: list) -> int:
    return sum(is_x_mas(grid, x, y) for x in range(len(grid)) for y in range(len(grid)))


with open('input.txt') as f:
    data = f.read().splitlines()

print(part_2(data))
