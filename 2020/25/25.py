def get_loop_size(public_key: int):
    val = 1
    i = 0
    while val != public_key:
        val = (val * 7) % 20201227
        i += 1
    return i


def get_encryption_key(public_key: int, loop_size: int):
    val = 1
    for i in range(loop_size):
        val = (val * public_key) % 20201227
    return val


def part_1(data):
    public_key_card, public_key_door = data
    loop_size = get_loop_size(public_key_card)
    return get_encryption_key(public_key_door, loop_size)


with open('input.txt') as f:
    data = [int(line) for line in f.read().splitlines()]

print(part_1(data))
