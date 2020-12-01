import hashlib


def get_hash(string):
    return hashlib.md5(string.encode()).hexdigest()


def get_limit(offset):
    limit = ''.join(['0' if i < offset else 'F' for i in range(32)])
    return int(limit, 16)


# slow as shit but it works
# (am I talking about myself or the code)
# (we may never know)
def get_password(door_id, length, offset):
    password = []
    limit = get_limit(offset)
    i = 0
    while len(password) < length:
        door_hash = get_hash(door_id + str(i))
        door_value = int(door_hash, 16)
        if door_value <= limit:
            password.append(door_hash[offset])
        i += 1
    return ''.join(password)


def get_better_password(door_id, length, offset):
    password = ['' for i in range(length)]
    limit = get_limit(offset)
    found = 0
    i = 0
    while found < length:
        door_hash = get_hash(door_id + str(i))
        door_value = int(door_hash, 16)
        if door_value <= limit:
            pos = door_hash[offset]
            if pos.isdigit() and int(pos) < length and password[int(pos)] == '':
                password[int(pos)] = door_hash[offset+1]
                found += 1
        i += 1
    return ''.join(password)


def part_1(door_id):
    return get_password(door_id, 8, 5)


def part_2(door_id):
    return get_better_password(door_id, 8, 5)


door_id = 'abc'
print(part_2(door_id))