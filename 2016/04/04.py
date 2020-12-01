import re
from string import ascii_lowercase

def process_data(data):
    sector_id = re.findall(r'\d+', data)[0]
    letters = re.findall(r'[a-z]+', data)
    checksum = letters.pop()
    return {
        'sector_id': int(sector_id),
        'name': letters,
        'checksum': checksum
    }


def count_letters(name):
    count = {}
    for sequence in name:
        for c in sequence:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
    return count


def get_checksum(count):
    sorted_count = sorted(count.items(), key=lambda item: (-item[1], item[0]))
    checksum = []
    for i in range(5):
        checksum.append(sorted_count[i][0])
    return ''.join(checksum)


def is_real_room(room):
    return room['checksum'] == get_checksum(count_letters(room['name']))


def shift(string, offset):
    offset_mod = offset % len(ascii_lowercase)
    return string.translate(str.maketrans(ascii_lowercase, ascii_lowercase[offset_mod:] + ascii_lowercase[:offset_mod]))


def decrypt_room_name(room):
    offset = room['sector_id']
    return ' '.join([shift(string, offset) for string in room['name']])


def part_1(rooms):
    return sum([room['sector_id'] for room in rooms if is_real_room(room)])


def part_2(rooms):
    real_rooms = [room for room in rooms if is_real_room(room)]
    for room in real_rooms:
        name = decrypt_room_name(room)
        if name.find('north') != -1:
            return { 'sector_id': room['sector_id'], 'name': name }


with open('input.txt') as f:
    data = f.read().splitlines()
rooms = [process_data(line) for line in data]

print(part_2(rooms))