import statistics


def part_1(data): return sum(abs(x-int(statistics.median(data))) for x in data)


def part_2(data):
    dist = lambda n : sum((abs(x-n)*(abs(x-n)+1))//2 for x in data)
    mn, mx = min(data), max(data)
    res = dist(mn)
    for i in range(mn+1, mx+1):
        tmp = dist(i)
        if tmp < res:
            res = tmp
    return res


with open('input.txt') as f:
    data = [int(x) for x in f.readline().split(',')]

print(part_2(data))
