def distance(t: int, reindeer: tuple):
    d, fly, rest = reindeer
    full_cycles = t // (fly + rest)
    remainder = t % (fly + rest)
    if remainder >= fly:
        full_cycles += 1
        remainder = 0
    return (full_cycles * fly + remainder) * d


def lead(t: int, reindeer: dict):
    distances = {r: distance(t, reindeer[r]) for r in reindeer}
    lead_distance = max(distances.values())
    return [r for r in reindeer if distances[r] == lead_distance]


def part_1(data: dict):
    return max([distance(2503, data[r]) for r in data])


def part_2(data: dict):
    points = {d: 0 for d in data}
    for t in range(1, 2504):    # 2504
        leads = lead(t, data)
        for l in leads:
            points[l] += 1
    return max(points.values())


with open('input.txt') as f:
    data = {s[0]: tuple([int(s[3]), int(s[6]), int(s[13])]) for s in [line.split() for line in f.read().splitlines()]}

print(part_2(data))
