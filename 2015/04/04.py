import hashlib


def md5hash(string: str):
    return hashlib.md5(bytes(string, 'UTF-8')).hexdigest()


def find_hash(string: str, leading_zeroes: int):
    i = 1
    while True:
        if md5hash(string + str(i)).startswith('0'*leading_zeroes):
            return i
        i += 1


def part_1(string: str):
    return find_hash(string, 5)


def part_2(string: str):
    return find_hash(string, 6)


print(part_2('iwrupvqb'))
