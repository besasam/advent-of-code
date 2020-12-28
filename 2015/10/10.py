def split_sequence(seq: str):
    mod = ''
    for s in seq:
        if mod and mod[-1] != s:
            mod += '#'
        mod += s
    return mod.split('#')


def look_and_say(seq: str):
    split = split_sequence(seq)
    res = ''
    for s in split:
        res += str(len(s)) + s[0]
    return res


def part_1(seq: str):
    for i in range(40):
        seq = look_and_say(seq)
    return len(seq)


def part_2(seq: str):
    for i in range(50):
        seq = look_and_say(seq)
    return len(seq)


print(part_2('1113122113'))
