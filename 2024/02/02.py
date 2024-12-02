def inc_or_dec(numbers: list) -> bool:
    return True if (sorted(numbers) == numbers or sorted(numbers, reverse=True) == numbers) else False


def is_safe(numbers: list, min_distance: int=1, max_distance: int=3) -> bool:
    if inc_or_dec(numbers):
        for i in range(len(numbers)-1):
            if not min_distance <= abs(numbers[i] - numbers[i+1]) <= max_distance:
                return False
        return True
    return False


def part_1(data: list) -> int:
    return sum(is_safe(line) for line in data)


# fuck it, we bruteforce
def part_2(data: list) -> int:
    safe_reports = 0
    for line in data:
        if is_safe(line):
            safe_reports += 1
        else:
            variants = [line[:i] + line[i+1:] for i in range(len(line))]
            for v in variants:
                if is_safe(v):
                    safe_reports += 1
                    break
    return safe_reports


with open('input.txt') as f:
    data = [[int(x) for x in line.split()] for line in f.read().splitlines()]

print(part_2(data))
