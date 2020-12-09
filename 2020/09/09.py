import itertools


def validate(nums, length):
    for i, n in enumerate(nums[length:]):
        if n not in [sum(s) for s in itertools.combinations(nums[i:i+length], 2)]:
            return n
    return None


def find_set(nums, invalid):
    for i in range(len(nums) - 1):
        k = 1
        while k < len(nums) - i:
            s = nums[i:i+k]
            if sum(s) >= invalid:
                if sum(s) == invalid:
                    return sum([min(s), max(s)])
                break
            k += 1


def part_1(data):
    return validate(data, 25)


def part_2(data):
    invalid = validate(data, 25)
    return find_set(data, invalid)


with open('input.txt') as f:
    data = [int(l) for l in f.read().splitlines()]

print(part_2(data))