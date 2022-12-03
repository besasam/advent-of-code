import string

types = {string.ascii_lowercase[i]: i+1 for i in range(26)} | {string.ascii_uppercase[i]: i+27 for i in range(26)}


def find_duplicate(s: str) -> str:
    [left, right] = split(s)
    for c in left:
        if c in right:
            return c


def split(s: str) -> list:
    l = len(s)//2
    return [s[:l], s[l:]]


def chunk(l: list) -> list:
    return [l[i:i+3] for i in range(0, len(l), 3)]


def find_truplicate(l: list) -> str:
    [first, second, third] = l
    for c in first:
        if c in second and c in third:
            return c


def score(c: string) -> int:
    return types[c]


def part_1(data):
    return sum(score(find_duplicate(line)) for line in data)


def part_2(data):
    return sum(score(find_truplicate(chnk)) for chnk in chunk(data))


with open('input.txt') as f:
    data = f.read().splitlines()

print(part_2(data))
