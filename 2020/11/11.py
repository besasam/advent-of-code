class Seat:
    def __init__(self):
        self.occupied = False

    def change(self, visible, max_occupied):
        if not self.occupied and sum(visible) == 0:
            self.occupied = True
        elif self.occupied and sum(visible) >= max_occupied:
            self.occupied = False


class ConwaysMusicalChairs:
    def __init__(self, seat_layout):
        self.map = [[None if s == '.' else Seat() for s in row] for row in seat_layout]
        self.width = len(seat_layout[0])
        self.height = len(seat_layout)
        self.states = []

    def find_seats(self, part_2=False):
        while True:
            state = int(self)
            if state in self.states:
                return self.count()
            self.states.append(state)
            self.step(part_2)

    def step(self, part_2):
        values = self.copy_values()
        for i, row in enumerate(self.map):
            for k, seat in enumerate(row):
                if seat is None:
                    continue
                if part_2:
                    visible = self.see_all(i, k, values)
                    max_occupied = 5
                else:
                    visible = self.see_adjacent(i, k, values)
                    max_occupied = 4
                seat.change(visible, max_occupied)

    def see_adjacent(self, row, col, values):
        positions = self.get_adjacent_positions(row, col)
        return filter(lambda x: x is not None, [values[p[0]][p[1]] for p in positions])

    def see_all(self, row, col, values):
        vectors = self.get_vectors(row, col)
        visible = []
        for v in vectors:
            y, x = row+v[0], col+v[1]
            while 0 <= x < self.width and 0 <= y < self.height:
                if values[y][x] is not None:
                    visible.append(values[y][x])
                    break
                y += v[0]
                x += v[1]
        return visible

    def get_adjacent_positions(self, row, col):
        vectors = self.get_vectors(row, col)
        return [(row+v[0], col+v[1]) for v in vectors]

    def get_vectors(self, row, col):
        vectors = []
        for y in range(-1, 2):
            if row+y < 0 or row+y >= self.height:
                continue
            for x in range(-1, 2):
                if col+x < 0 or col+x >= self.width or (row+y == row and col+x == col):
                    continue
                vectors.append((y, x))
        return vectors

    def copy_values(self):
        return [[None if s is None else s.occupied for s in row] for row in self.map]

    def count(self):
        count = 0
        for row in self.map:
            for s in row:
                if s is not None and s.occupied:
                    count += 1
        return count

    def __int__(self):
        binary = ''
        for row in self.map:
            for s in filter(lambda x: x is not None, row):
                binary += '1' if s.occupied else '0'
        return int(binary, 2)

    def __str__(self):
        string = ''
        for row in self.map:
            for s in row:
                string += '.' if s is None else '#' if s.occupied else 'L'
            string += '\n'
        return string


def part_1(data):
    seats = ConwaysMusicalChairs(data)
    return seats.find_seats()

def part_2(data):
    seats = ConwaysMusicalChairs(data)
    return seats.find_seats(True)


with open('input.txt') as f:
    data = f.read().splitlines()

print(part_2(data))