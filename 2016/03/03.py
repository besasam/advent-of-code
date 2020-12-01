def is_possible_triangle(sides):
    for i in range(3):
        if sides[i] >= sides[(i+1) % 3] + sides[(i+2) % 3]:
            return False
    return True


def convert_data(data):
    new_data = []
    row = 0
    while row < len(data) - 2:
        for col in range(3):
            new_data.append([data[row][col], data[row+1][col], data[row+2][col]])
        row += 3
    return new_data


def part_1(data):
    count = 0
    for sides in data:
        if is_possible_triangle(sides):
            count += 1
    return count


def part_2(data):
    return part_1(convert_data(data))


with open('input.txt') as f:
    data = [[int(x) for x in split if x != ''] for split in
            [line.split(' ') for line in f.read().splitlines()]]  # this took me way too long

print(part_2(data))
#print(convert_data(data))