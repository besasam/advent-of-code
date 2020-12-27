import math


class SeaMap:
    def __init__(self, content: list):
        self.content = content
        self.size = len(content)
        self.monster_pattern = [(0, 18), (1, 0), (1, 5), (1, 6), (1, 11), (1, 12), (1, 17), (1, 18), (1, 19), (2, 1), (2, 4), (2, 7), (2, 10), (2, 13), (2, 16)]

    def locate_sea_monster(self, y, x):
        if y > self.size - 3 or x > self.size - 20:
            return False
        return all(self.content[y+p[0]][x+p[1]] for p in self.monster_pattern)

    def find_correct_orientation(self):
        rotated = 0
        while True:
            for y in range(self.size):
                for x in range(self.size):
                    if self.locate_sea_monster(y, x):
                        return
            if rotated < 3:
                self.content = rotate(self.content, 90)
                rotated += 1
            else:
                self.content = flip(rotate(self.content, 90))
                rotated = 0

    def get_water_roughness(self):
        self.find_correct_orientation()
        no_monsters = [row[:] for row in self.content]
        for y in range(self.size):
            for x in range(self.size):
                if self.locate_sea_monster(y, x):
                    for p in self.monster_pattern:
                        no_monsters[y+p[0]][x+p[1]] = False
        return sum([sum(row) for row in no_monsters])

    def __str__(self):
        return '\n'.join([''.join(['#' if c else '.' for c in row]) for row in self.content])


class Tile:
    def __init__(self, id: int, content: list, rotation: int = 0, flipped: bool = False):
        self.id = id
        self.content = content
        self.rotation = rotation
        self.flipped = flipped
        self.borders = get_borders(self.content)
        self.matches = dict()
        self.y = None
        self.x = None

    def match_tile(self, tile):
        if self == tile:
            return False
        if tile in self.matches.items():
            return True
        if self.borders['u'] == tile.borders['d']:
            self.matches['u'] = tile
            return True
        if self.borders['r'] == tile.borders['l']:
            self.matches['r'] = tile
            return True
        if self.borders['d'] == tile.borders['u']:
            self.matches['d'] = tile
            return True
        if self.borders['l'] == tile.borders['r']:
            self.matches['l'] = tile
            return True
        return False

    def get_orientation(self):
        return 'f' if self.flipped else 'r' + str(self.rotation)

    def place_tile(self, y, x):
        self.y = y
        self.x = x

    def __str__(self):
        return '\n'.join([''.join(['#' if c else '.' for c in row]) for row in self.content])

    def __repr__(self):
        return f'Tile({self.id} {self.get_orientation()})'


class Grid:
    def __init__(self, tiles):
        self.map = []
        self.matched_tiles = dict()
        self.tiles = dict()
        for tile in tiles:
            self.tiles[tile.id] = {'r0': tile}
            self.tiles[tile.id]['f0'] = flipped = Tile(tile.id, flip(tile.content), flipped=True)
            for d in [90, 180, 270]:
                self.tiles[tile.id]['r' + str(d)] = Tile(tile.id, rotate(tile.content, d), rotation=d)
                self.tiles[tile.id]['f' + str(d)] = Tile(tile.id, rotate(flipped.content, d), rotation=d, flipped=True)

    def match_tiles(self):
        if self.matched_tiles:
            return self.matched_tiles
        order = ['r0', 'r90', 'r180', 'r270', 'f0', 'f90', 'f180', 'f270']
        tile_ids = list(self.tiles.keys())
        while len(self.matched_tiles) < len(tile_ids):
            for tile1_id in tile_ids:
                if self.matched_tiles and tile1_id not in self.matched_tiles:
                    continue
                elif not self.matched_tiles:
                    found = False
                    for o1 in order:
                        if found:
                            break
                        tile1 = self.tiles[tile1_id][o1]
                        for tile2_id in [tile_id for tile_id in tile_ids if tile_id != tile1_id]:
                            for o2 in order:
                                tile2 = self.tiles[tile2_id][o2]
                                if tile1.match_tile(tile2):
                                    self.matched_tiles[tile1_id] = o1
                                    self.matched_tiles[tile2_id] = o2
                                    found = True
                                    break
                else:
                    tile1 = self.tiles[tile1_id][self.matched_tiles[tile1_id]]
                    for tile2_id in [tile_id for tile_id in tile_ids if tile_id != tile1_id]:
                        if tile2_id in self.matched_tiles:
                            tile2 = self.tiles[tile2_id][self.matched_tiles[tile2_id]]
                            if tile1.match_tile(tile2):
                                continue
                        else:
                            for o2 in order:
                                tile2 = self.tiles[tile2_id][o2]
                                if tile1.match_tile(tile2):
                                    self.matched_tiles[tile2_id] = o2
                                    break
        return self.matched_tiles

    def build_map(self):
        if self.map:
            return self.map
        self.match_tiles()
        grid_size = int(math.sqrt(len(self.matched_tiles)))
        self.map = [[None for _ in range(grid_size)] for _ in range(grid_size)]
        for tile_id in self.matched_tiles:
            tile = self.tiles[tile_id][self.matched_tiles[tile_id]]
            if len(tile.matches) == 2 and 'r' in tile.matches and 'd' in tile.matches:
                tile.y = 0
                tile.x = 0
                self.map[0][0] = tile
                self.place_tiles(tile)
        return self.map

    def make_map(self):
        self.build_map()
        tile_size = len(self.map[0][0].content)
        seamap = []
        for row in self.map:
            for y in range(tile_size)[1:-1]:
                seamap_row = []
                for tile in row:
                    seamap_row += tile.content[y][1:-1]
                seamap.append(seamap_row[:])
        return SeaMap(seamap)

    def place_tiles(self, tile):
        if all(None not in row for row in self.map):
            return
        for m in tile.matches:
            nx = tile.x
            ny = tile.y
            if m == 'u':
                ny -= 1
            elif m == 'r':
                nx += 1
            elif m == 'd':
                ny += 1
            elif m == 'l':
                nx -= 1
            if self.map[ny][nx] is not None:
                continue
            next_tile = tile.matches[m]
            next_tile.y = ny
            next_tile.x = nx
            self.map[ny][nx] = next_tile
            self.place_tiles(next_tile)


    # def match_tiles(self, cur=None, tiles_to_check=None, cache=None):
    #     order = ['r0', 'r90', 'r180', 'r270', 'f0', 'f90', 'f180', 'f270']
    #     if tiles_to_check == []:
    #         found = False
    #         while not found:
    #             for o in order:
    #                 if found:
    #                     break
    #                 cur_tile = self.tiles[cur][o]
    #                 for prev in list(cache.keys()):
    #                     prev_tile = self.tiles[prev][cache[prev]]
    #                     if cur_tile.match_tile(prev_tile):
    #                         prev_tile.match_tile(cur_tile)
    #                         cache[cur] = o
    #                         found = True
    #                         break
    #     if cur is None:
    #         tiles_to_check = self.tile_ids[:]
    #         cur = tiles_to_check.pop(0)
    #         return self.match_tiles(cur, tiles_to_check, {cur: 'r0'})
    #     cur_tile = self.tiles[cur][cache[cur]]
    #     for prev in cache:
    #         prev_tile = self.tiles[prev][cache[prev]]
    #         if cur_tile.match_tile(prev_tile):
    #             prev_tile.match_tile(cur_tile)
    #     for nex in tiles_to_check:
    #         for o in order:
    #             nex_tile = self.tiles[nex][o]
    #             if cur_tile.match_tile(nex_tile):
    #                 nex_tile.match_tile(cur_tile)
    #                 cache[nex] = o
    #                 next_tiles_to_check = tiles_to_check[:]
    #                 next_tiles_to_check.remove(nex)
    #                 return self.match_tiles(nex, next_tiles_to_check, cache)
    #     if tiles_to_check == []:
    #         return cache
    #     next_tiles_to_check = tiles_to_check[:]
    #     nex = next_tiles_to_check.pop(0)
    #     return self.match_tiles(nex, next_tiles_to_check, cache)
    #
    # def make_map(self):
    #     all_matches = self.match_tiles()
    #     matches = dict()
    #     for m in all_matches:
    #         if all_matches[m]:
    #             matches[m] = all_matches[m]
    #     grid_size = int(math.sqrt(len(matches)))
    #     self.map = [[None for _ in range(grid_size)] for _ in range(grid_size)]
    #     for m in matches:
    #         tile = self.tiles[m][matches[m]]
    #     return matches


def rotate(tile, deg):
    new_tile = []
    tile_size = len(tile)
    for i in range(tile_size):
        if deg == 90:
            new_tile.append(list(reversed([x[i] for x in tile])))
        elif deg == 180:
            new_tile.append(list(reversed(tile[tile_size-i-1])))
        else:
            new_tile.append([x[tile_size-i-1] for x in tile])
    return new_tile


def flip(tile):
    new_tile = []
    tile_size = len(tile)
    for i in range(tile_size):
        new_tile.append(list(reversed(tile[i])))
    return new_tile


def get_borders(tile):
    return {'u': tile[0], 'r': [x[-1] for x in tile], 'd': tile[-1], 'l': [x[0] for x in tile]}


def make_tiles(input_file):
    tiles = []
    with open(input_file) as f:
        lines = f.read().splitlines()
    while lines:
        tile_id = int(lines.pop(0)[5:-1])
        tile_content = []
        for i in range(10):
            tile_content.append([True if c == '#' else False for c in lines.pop(0)])
        tiles.append(Tile(tile_id, tile_content))
        lines.pop(0)
    return tiles


def part_1(input_file):
    tiles = make_tiles(input_file)
    grid = Grid(tiles)
    grid.build_map()
    return grid.map[0][0].id * grid.map[0][-1].id * grid.map[-1][0].id * grid.map[-1][-1].id


def part_2(input_file):
    tiles = make_tiles(input_file)
    grid = Grid(tiles)
    seamap = grid.make_map()
    return seamap.get_water_roughness()


print(part_2('input.txt'))
