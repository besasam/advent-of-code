from itertools import groupby
import math


def parse(data):
    def convert(line):
        return int('0b' + ''.join(['1' if c == '#' else '0' for c in line]), 2)
    res = []
    for rows in data:
        cols = list(zip(*rows[:]))
        res.append({'rows': [convert(row) for row in rows], 'cols': [convert(col) for col in cols]})
    return res


def check_reflection(matrix, i, s=None):
    width = len(matrix)
    d = min(i+1, width-i-1)
    rng = range(0, i+d+1) if i < width//2 else range(i-d+1, width)
    if s is not None:
        if s not in rng:
            return False
    for k in range(len(rng)//2):
        if matrix[i-k] ^ matrix[i+k+1]:
            return False
    return True


def find_reflection(matrix, s=None):
    for i, row in enumerate(matrix[:-1]):
        if row ^ matrix[i+1] == 0 and check_reflection(matrix, i, s):
            return i+1
    return 0


def check_smudges(matrix):
    for i, c in enumerate(matrix):
        m = matrix[:]
        for x in [1 << i for i in range(math.floor(math.log2(c))+1)]:
            m[i] = c ^ x
            if r := find_reflection(m, i):
                return r


def part_1(data):
    res = 0
    for matrix in data:
        if x := find_reflection(matrix['rows']):
            res += 100*x
        elif x := find_reflection(matrix['cols']):
            res += x
    return res


def part_2(data):
    res = 0
    for matrix in data:
        if x := check_smudges(matrix['rows']):
            res += 100*x
        elif x := check_smudges(matrix['cols']):
            res += x
    return res


with open('input.txt') as f:
    data = parse([list(l) for e, l in groupby(f.read().splitlines(), key=bool) if e])

print(part_2(data))
