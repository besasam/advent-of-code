import string


straights = [string.ascii_lowercase[i:i+3] for i in range(24)]


def contains_increasing_straight(password: str):
    return any(s in password for s in straights)


def contains_forbidden_characters(password: str):
    return any(c in password for c in ['i', 'o', 'l'])


def contains_two_pairs(password: str):
    pair = ''
    prev = ''
    for i, c in enumerate(password):
        if c == prev:
            pair = c*2
            pos = i + 1
            break
        prev = c
    if not pair:
        return False
    prev = ''
    for c in password[pos:]:
        if c == prev and c*2 != pair:
            return True
        prev = c
    return False


def next_string(password: str):
    chars = list(reversed(password))
    pwd = []
    carry = False
    i = string.ascii_lowercase.find(chars[0]) + 1
    if i == 26:
        i = 0
        carry = True
    pwd.append(string.ascii_lowercase[i])
    for c in chars[1:]:
        if carry:
            carry = False
            i = string.ascii_lowercase.find(c) + 1
            if i == 26:
                i = 0
                carry = True
            pwd.append(string.ascii_lowercase[i])
        else:
            pwd.append(c)
    return ''.join(reversed(pwd))


def part_1(password: str):
    while contains_forbidden_characters(password) or not contains_increasing_straight(password) or not contains_two_pairs(password):
        password = next_string(password)
    return password


def part_2(password: str):
    return part_1(next_string(part_1(password)))


print(part_2('vzbxkghb'))
