class Player:
    def __init__(self, x: int = 0, y: int = 0):
        self.x, self.y = x, y
        self.inventory = []


class SpaceMaze:
    def __init__(self, input_file_path: str):
        self.map = dict()
        self.state = dict()
        self.player = Player()
        with open(input_file_path) as f:
            maze_rows = f.read().splitlines()
        for y, row in enumerate(maze_rows):
            self.map[y] = dict()
            self.state[y] = dict()
            for x, val in enumerate(row):
                self.state[y][x] = None
                is_tile = val != '#'
                self.map[y][x] = is_tile
                if is_tile and val != '.':
                    if val == '@':
                        self.player.x = x
                        self.player.y = y
                    else:
                        self.state[y][x] = val

    def __str__(self):
        rows = []
        for y in self.map:
            rows.append(''.join(['.' if self.map[y][x] else '#' for x in self.map[y]]))
        return '\n'.join(rows)


def part_1(input_file_path):
    maze = SpaceMaze(input_file_path)
    print(maze)


part_1('example.txt')
