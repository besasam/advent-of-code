def part_1(data: list) -> int:
    nums = [sorted(x) for x in list(zip(*data[::-1]))]
    return sum(abs(a-nums[1][i]) for i, a in enumerate(nums[0]))


def part_2(data: list) -> int:
    nums = list(zip(*data[::-1]))
    counts = dict()
    score = 0
    for x in nums[0]:
        if x not in counts:
            counts[x] = x*nums[1].count(x)
        score += counts[x]
    return score


with open('input.txt') as f:
    data = [[int(x) for x in line.split('   ')] for line in f.read().splitlines()]

print(part_2(data))
