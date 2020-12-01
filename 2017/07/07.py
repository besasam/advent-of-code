class Node:
    def __init__(self, name, val, parent=None):
        self.name = name
        self.val = val
        self.parent = parent
        self.children = []

    def insert(self, node):
        if node not in self.children:
            self.children.append(node)
            node.parent = self

    def get_root(self):
        if self.parent is None:
            return self
        else:
            return self.parent.get_root()

    def get_height(self):
        if not self.children:
            return 0
        return 1 + max([c.get_height() for c in self.children])

    def get_weight(self):
        if not self.children:
            return self.val
        sum = self.val
        for c in self.children:
            sum += c.get_weight()
        return sum

    def is_balanced(self):
        if not self.children:
            return True
        c = [c.get_weight for c in self.children]
        if len(set(c)) == 1:
            return True
        return False

    def find_unbalanced(self, parent=None):
        if self.is_balanced():
            return None
        weights = [c.get_weight() for c in self.children]
        for c in self.children:
            if weights.count(c.get_weight()) == 1:
                return c.find_unbalanced(self)
        return parent.get_tower_weights()

    def get_tower_weights(self):
        if not self.children:
            return dict()
        weights = [c.get_weight() for c in self.children]
        wset = set(weights)
        return {w: weights.count(w) for w in wset}

    def print(self, d=''):
        str = f'- {self.name} ({self.val} / {self.get_weight()})'
        if not self.children:
            return str
        d += '  '
        for c in self.children:
            str += f'\n{d}{c.print(d)}'
        return str

    def __str__(self):
        parent = 'None' if self.parent is None else self.parent.name
        children = 'None' if self.children is None else ', '.join([c.name for c in self.children])
        return f'{self.name} - Value: {self.val} - Parent: {parent} - Children: {children}'


def prepare_data(data):
    d = dict()
    for line in data:
        d.update({line[0]: {'val': int(line[1][1:-1])}})
        if len(line) > 2:
            d[line[0]].update({'children': [c for c in line[3:]]})
    return d


def make_tree(data):
    nodes = dict()
    node = None
    for d in data:
        if d not in nodes:
            nodes.update({d: Node(d, data[d]['val'])})
        if 'children' in data[d]:
            for c in data[d]['children']:
                if c not in nodes:
                    nodes.update({c: Node(c, data[c]['val'], nodes[d])})
                nodes[d].insert(nodes[c])
        node = nodes[d]
    return node


def part_1(data):
    d = prepare_data([line.replace(',', '').split() for line in data])
    tree = make_tree(d)
    return(tree.get_root())


def part_2(data):
    tree = part_1(data)
    return tree.find_unbalanced()


with open('example.txt') as f:
    example = f.read().splitlines()
with open('input.txt') as f:
    data = f.read().splitlines()

print(part_2(data))
