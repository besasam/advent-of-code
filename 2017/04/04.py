def contains_anagram(line):
    words = line[:]
    while words:
        w = words.pop()
        for v in words:
            if sorted(w) == sorted(v):
                return True
    return False


def part_1(data):
    count = 0
    for line in data:
        if len(set(line)) == len(line):
            count += 1
    return count


def part_2(data):
    count = 0
    for line in data:
        if not contains_anagram(line):
            count += 1
    return count


with open('input.txt') as f:
    data = [l.split(' ') for l in f.read().splitlines()]

tests = [l.split(' ') for l in ['abcde fghij', 'abcde xyz ecdab', 'a ab abc abd abf abj', 'iiii oiii ooii oooi oooo', 'oiii ioii iioi iiio']]

print(part_2(data))