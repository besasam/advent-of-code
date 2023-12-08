from numpy import lcm
from functools import reduce


def part_1(ins, nodes):
    steps = 0
    i = 0
    cur = 'AAA'
    while True:
        k = 0 if ins[i] == 'L' else 1
        steps += 1
        cur = nodes[cur][k]
        if cur == 'ZZZ':
            return steps
        i = 0 if i == len(ins)-1 else i + 1


def get_phase(ins, nodes, n):
    steps = 0
    i = 0
    while True:
        k = 0 if ins[i] == 'L' else 1
        steps += 1
        n = nodes[n][k]
        if n[-1] == 'Z':
            return steps
        i = 0 if i == len(ins) - 1 else i + 1


def part_2(ins, nodes):
    phases = [get_phase(ins, nodes, n) for n in nodes if n[-1] == 'A']
    return reduce(lambda a, b: lcm(a, b, dtype='int64'), phases)


with open('input.txt') as f:
    data = f.read().splitlines()

ins = data[0]
nodes = {a: b[1:-1].split(', ') for (a, b) in [line.split(' = ') for line in data[2:]]}

print(part_2(ins, nodes))
