class Node:
    def __init__(self, id):
        self.id = id
        self.pipes = []

    def connect(self, node):
        if node not in self.pipes:
            self.pipes.append(node)
        if self not in node.pipes:
            node.pipes.append(self)

    def __str__(self):
        return f'{self.id}: {[p.id for p in self.pipes]}'


def make_groups(data):
    nodes = {int(i[0]): Node(int(i[0])) for i in data}
    for i in data:
        for n in i[2:]:
            nodes[int(i[0])].connect(nodes[int(n)])
    groups = [[0]]
    for n in nodes:
        new = True
        for group in groups:
            if n in group:
                group.extend([node.id for node in nodes[n].pipes])
                new = False
            else:
                for p in nodes[n].pipes:
                    if p.id in group:
                        group.append(n)
                        new = False
        if new:
            groups.append([n])
    return [set(g) for g in groups]


def part_1(data):
    groups = make_groups(data)
    for g in groups:
        if 0 in g:
            return len(g)


with open('example.txt') as f:
    example = [l.replace(',', '').split() for l in f.read().splitlines()]
with open('input.txt') as f:
    data = [l.replace(',', '').split() for l in f.read().splitlines()]

print(part_1(data))