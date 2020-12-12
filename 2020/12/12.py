class Ship:
    COMPASS = ['E', 'S', 'W', 'N']

    def __init__(self):
        self.x = 0
        self.y = 0
        self.d = 0

    def navigate(self, instructions):
        for [action, value] in instructions:
            self.do(action, value)
        return [self.x, self.y]

    def do(self, action, value):
        if action in ['L', 'R']:
            self.turn(action, value)
        elif action == 'F':
            self.move(self.COMPASS[self.d], value)
        else:
            self.move(action, value)

    def move(self, direction, length):
        if direction == 'E':
            self.x += length
        elif direction == 'S':
            self.y -= length
        elif direction == 'W':
            self.x -= length
        elif direction == 'N':
            self.y += length

    def turn(self, direction, degrees):
        d = degrees // 90
        if direction == 'R':
            self.d = (self.d + d) % 4
        elif direction == 'L':
            self.d = (self.d - d) % 4


class WaypointShip(Ship):
    def __init__(self):
        super().__init__()
        self.wp_x = 10
        self.wp_y = 1

    def do(self, action, value):
        if action in ['L', 'R']:
            self.turn(action, value)
        elif action == 'F':
            self.x += value * self.wp_x
            self.y += value * self.wp_y
        else:
            self.move(action, value)

    def move(self, direction, length):
        if direction == 'E':
            self.wp_x += length
        elif direction == 'S':
            self.wp_y -= length
        elif direction == 'W':
            self.wp_x -= length
        elif direction == 'N':
            self.wp_y += length

    def turn(self, direction, degrees):
        if degrees == 180:
            self.wp_x, self.wp_y = -self.wp_x, -self.wp_y
        elif (direction == 'R' and degrees == 90) or (direction == 'L' and degrees == 270):
            self.wp_x, self.wp_y = self.wp_y, -self.wp_x
        else:
            self.wp_x, self.wp_y = -self.wp_y, self.wp_x


def part_1(data):
    ship = Ship()
    pos = ship.navigate(data)
    return abs(pos[0]) + abs(pos[1])


def part_2(data):
    ship = WaypointShip()
    pos = ship.navigate(data)
    return abs(pos[0]) + abs(pos[1])


with open('input.txt') as f:
    data = [[l[0], int(l[1:])] for l in f.read().splitlines()]

print(part_2(data))