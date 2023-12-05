from itertools import groupby


class AlmanacEntry:
    def __init__(self, entry):
        [self.destination, self.source, self.range] = [int(x) for x in entry]

    def __repr__(self):
        return str([self.destination, self.source, self.range])


class Almanac:
    def __init__(self, entries):
        self.entries = []
        for entry in entries:
            self.entries.append(AlmanacEntry(entry.split()))
        self.entries.sort(key=lambda x: x.source, reverse=True)

    def find(self, number):
        for entry in self.entries:
            if number == entry.source:
                return entry.destination
            if entry.source < number and (distance := number - entry.source) < entry.range:
                    return entry.destination + distance
        return number


def parse(data):
    seeds = [int(n) for n in data[0][0].split(': ')[1].split()]
    maps = []
    for entry in data[1:]:
        maps.append(Almanac(entry[1:]))
    return [seeds, maps]


def intersect(x, y):
    return max(x[0], y[0]), min(x[1], y[1])


def chunk(source_range, dest_range):
    (start, stop) = source_range
    (dest_start, dest_stop) = dest_range
    res = []

    # source starts before dest
    if start < dest_start:
        # and ends before dest
        if stop <= dest_start:
            return [(start, stop)]
        res.append((start, dest_start))
        start = dest_start
        # and ends in dest
        if stop <= dest_stop:
            res.append((start, stop))
            return res
        # and ends after dest
        res.append((start, dest_stop))
        res.append((dest_stop, stop))
        return res

    # source starts in dest
    if dest_start <= start < dest_stop:
        # and ends in dest
        if stop <= dest_stop:
            return ((start, stop))
        # and ends after dest
        res.append((start, dest_stop))
        res.append((dest_stop, stop))
        return res

    # source starts after dest
    return [(start, stop)]


def chunks(source_range, destination):
    destination_tpl = [(d.source, d.range) for d in destination]
    dest_ranges = sorted(destination_tpl, key=lambda x: x[0])
    res = []
    cur = source_range[0]
    while dest_ranges:
        dest = dest_ranges.pop(0)
        if res:
            cur = res.pop()
        res.extend(chunk(cur, dest))
    return res


def dechunk(chunks):
    if not chunks:
        return []
    res = []
    cur = chunks.pop(0)
    while chunks:
        nex = chunks.pop(0)
        if cur[1] == nex[0]:
            cur = (cur[0], nex[1])
        else:
            res.append(cur)
            cur = nex
    res.append(cur)
    return res


def part_1(data):
    [seeds, maps] = parse(data)
    for almanac in maps:
        seeds = [almanac.find(seed) for seed in seeds]
    return min(seeds)


def part_2(data):
    [seeds, maps] = parse(data)
    cur = []
    for i in range(0, len(seeds), 2):
        cur.append((seeds[i], seeds[i]+seeds[i+1]))
    for almanac in maps:
        cur = dechunk(cur)
        cur = chunks(cur, almanac.entries)
        cur = [(almanac.find(c[0]), c[1]+(c[1]-c[0])) for c in cur]
    return min(c[0] for c in cur)


with open('test.txt') as f:
    data = [list(g) for k, g in groupby(f.read().splitlines(), key=bool) if k]

print(part_2(data))
