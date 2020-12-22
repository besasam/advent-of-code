class Tile:
    def __init__(self, id, tile):
        self.id = id
        self.content = tile

    def get_all_possible_borders(self):
        borders = {'r0': get_borders(self.content)}
        for d in [90, 180, 270]:
            tile = rotate(self.content, d)
            borders['r' + str(d)] = get_borders(tile)
        tile = flip(self.content)
        borders['f0'] = get_borders(tile)
        for d in [90, 180, 270]:
            tile = rotate(self.content, d)
            borders['f' + str(d)] = get_borders(tile)
        return borders

    def get_all_orientations(self):
        orientations = {'r0': self.content}
        for d in [90, 180, 270]:
            orientations['r' + str(d)] = rotate(self.content, d)
        flipped = flip(self.content)
        orientations['f0'] = flipped
        for d in [90, 180, 270]:
            orientations['f' + str(d)] = rotate(flipped, d)
        return orientations

    def print_row(self, row):
        return ''.join(['#' if c else '.' for c in row])

    def print_tile(self, tile):
        return '\n'.join([self.print_row(row) for row in tile])

    def __str__(self):
        return self.print_tile(self.content)


def rotate(tile, deg):
    new_tile = []
    for i in range(10):
        if deg == 90:
            new_tile.append(list(reversed([x[i] for x in tile])))
        elif deg == 180:
            new_tile.append(list(reversed(tile[9-i])))
        else:
            new_tile.append([x[9-i] for x in tile])
    return new_tile


def flip(tile):
    new_tile = []
    for i in range(10):
        new_tile.append(list(reversed(tile[i])))
    return new_tile


def get_borders(tile):
    return {'u': tile[0], 'r': [x[-1] for x in tile], 'd': tile[-1], 'l': [x[0] for x in tile]}


def make_tiles(input_file):
    tiles = dict()
    with open(input_file) as f:
        lines = f.read().splitlines()
    while lines:
        tile_id = int(lines.pop(0)[5:-1])
        tile_content = []
        for i in range(10):
            tile_content.append([True if c == '#' else False for c in lines.pop(0)])
        tiles[tile_id] = Tile(tile_id, tile_content)
        lines.pop(0)
    return tiles


# def make_grid(tiles_dict, grid_size, tiles_list=None, grid=None, pos=None, nex=0):
#     if tiles_list is None:
#         tiles_list = [tiles_dict[t] for t in tiles_dict]
#         grid = [[None for col in range(grid_size)] for row in range(grid_size)]
#         pos = 0
#     y, x = pos // grid_size, pos % grid_size
#     return y, x


def part_1(input_file):
    tiles = make_tiles(input_file)


print(part_1('example.txt'))

# tiles = make_tiles('example.txt')
# borders = tiles[2311].get_all_possible_borders()
# for orientation in borders:
#     print(orientation)
#     for b in borders[orientation]:
#         print(f'{b}: {tiles[2311].print_row(borders[orientation][b])}')
#     print()
# print()
