class Tree:
    def __init__(self, height: int, row: int, col: int, tree_map: 'TreeMap'):
        self.height = height
        self.visible = None
        self.row = row
        self.col = col
        self.map = tree_map
        self.neighbors = self._get_neighbors()

    def is_visible(self):
        if self.visible:
            return True
        if any(n is None for n in self.neighbors):
            self.visible = True
            return True


    def _get_neighbors(self):
        up = None if self.row == 0 else self.map[self.row-1][self.col]
        down = None if self.row == self.map.height-1 else self.map[self.row+1][self.col]
        left = None if self.col == 0 else self.map[self.row][self.col-1]
        right = None if self.col == self.map.width-1 else self.map[self.row][self.col+1]
        return [up, down, left, right]


    def __str__(self):
        return '#' if self.visible else '.'


class TreeMap:
    def __init__(self, treemap: list):
        self.map = []
        self.width = len(treemap[0])
        self.height = len(treemap)
        is_edge = lambda row, col : row == 0 or col == 0 or row == h-1 or col == w-1
        for i, row in enumerate(treemap):
            trees = []
            for k, col in enumerate(row):
                tree = Tree(col)
                if is_edge(i, k):
                    tree.visible = True
                trees.append(tree)
            self.map.append(trees)

    def get_all_trees(self) -> list:
        return sum(self.map, [])

    def look_right(self):
        for row in self.map:
            vis = True
            for i, tree in enumerate(row):
                if tree.visible:
                    continue
                if vis and tree.height <= row[i-1].height:
                    vis = False
                tree.visible = vis

    def look_left(self):
        for row in self.map:
            vis = True
            for i, tree in enumerate(reversed(row)):
                if tree.visible:
                    continue
                if vis and tree.height <= row[i-1].height:
                    vis = False
                tree.visible = vis

    def look_down(self):
        for col in range(len(self.map[0])):
            vis = True
            for row in range(len(self.map)):
                cur = self.map[row][col]
                if cur.visible:
                    continue
                prev = self.map[row-1][col]
                if vis and cur.height <= prev.height:
                    vis = False
                cur.visible = vis

    def look_up(self):
        for col in range(len(self.map[0])):
            vis = True
            for row in reversed(range(len(self.map))):
                cur = self.map[row][col]
                if cur.visible:
                    continue
                prev = self.map[row-1][col]
                if vis and cur.height <= prev.height:
                    vis = False
                cur.visible = vis

    def look(self):
        self.look_up()
        self.look_down()
        self.look_left()
        self.look_right()

    def __getitem__(self, item):
        return self.map[item]

    def __str__(self):
        return '\n'.join(''.join(str(tree) for tree in line) for line in self.map)


with open('input.txt') as f:
    data = [[int(c) for c in line] for line in f.read().splitlines()]

treemap = TreeMap(data)
treemap.look()
print(sum(tree.visible for tree in treemap.get_all_trees()))
