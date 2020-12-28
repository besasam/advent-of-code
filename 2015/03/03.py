from util.infinitegrid import Grid2D


def deliver_presents(grid: Grid2D, instructions: str):
    x = y = 0
    for i in instructions:
        x += 1 if i == '>' else -1 if i == '<' else 0
        y += 1 if i == '^' else -1 if i == 'v' else 0
        grid[x, y] += 1


def part_1(data: str):
    grid = Grid2D(0)
    grid[0, 0] = 1
    deliver_presents(grid, data)
    return len(grid.all_values())


def part_2(data: str):
    santa = ''.join([s for i, s in enumerate(data) if i % 2 != 0])
    robo = ''.join([s for i, s in enumerate(data) if i % 2 == 0])
    grid = Grid2D(0)
    grid[0, 0] = 2
    deliver_presents(grid, santa)
    deliver_presents(grid, robo)
    return len(grid.all_values())


with open('input.txt') as f:
    data = f.readline()

print(part_2(data))
