def get_row(seat):
    l = 128
    rows = [i for i in range(l)]
    for c in seat[:7]:
        l //= 2
        if c == 'F':
            rows = rows[:l]
        else:
            rows = rows[l:]
    return rows[0]


def get_column(seat):
    l = 8
    columns = [i for i in range(l)]
    for c in seat[7:]:
        l //= 2
        if c == 'L':
            columns = columns[:l]
        else:
            columns = columns[l:]
    return columns[0]


def get_seat_id(seat):
    return get_row(seat) * 8 + get_column(seat)


def part_1(data):
    return max(map(get_seat_id, data))


def part_2(data):
    seats = [get_seat_id(d) for d in data]
    seats.sort()
    for s in seats[1:-1]:
        if s-1 not in seats:
            return s-1
        if s+1 not in seats:
            return s+1


with open('input.txt') as f:
    data = f.read().splitlines()

print(part_2(data))