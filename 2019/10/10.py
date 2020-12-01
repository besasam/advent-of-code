def gcd(a, b):
    if a == b == 0:
        return 0
    a = abs(a)
    b = abs(b)
    while b != 0:
        a1 = b
        b1 = a % b
        a = a1
        b = b1
    return a


class Asteroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vectors = []
        self.visible = 0

    def detect(self, asteroid):
        if asteroid == self:
            return
        # print(f'Trying to detect {asteroid} from {self}')
        x, y = [asteroid.x - self.x, asteroid.y - self.y]
        d = gcd(x, y)
        x, y = x//d, y//d
        if [x, y] in self.vectors:
            # print(f'Not visible: Blocked by [{x, y}]')
            # print()
            return False
        # print(f'Visible! Adding [{x, y}] to vectors')
        # print()
        self.vectors.append([x, y])
        self.visible += 1
        return True

    def __str__(self):
        return f'<{self.x},{self.y}>: {self.visible}'


class AsteroidMap:
    def __init__(self, data):
        self.map = dict()
        self.asteroids = []
        self.width = len(data[0])
        self.height = len(data)
        for y, line in enumerate(data):
            for x, char in enumerate(line):
                if char == '#':
                    self.insert(x, y)

    def insert(self, x, y):
        asteroid = Asteroid(x, y)
        # print(f'Adding asteroid {asteroid}')
        if y not in self.map:
            self.map.update({y: {x: asteroid}})
        else:
            self.map[y].update({x: asteroid})
        self.asteroids.append(asteroid)
        return asteroid

    def detect_all(self):
        for a in self.asteroids:
            # print(f'Detecting from {a}')
            i = 1
            while i < self.width or i < self.height:
            #     print(f'Detecting at range {i}')
                self.detect(a, i)
                i += 1
            # print()

    def detect(self, asteroid, radius):
        if radius == 0:
            return
        N, E, S, W = [0, 1, 2, 3]
        x = asteroid.x - radius
        y = asteroid.y - radius
        d = E
        while True:
            if y in self.map and x in self.map[y]:
                asteroid.detect(self.map[y][x])
            if d == E:
                if x == asteroid.x + radius:
                    d = S
                    y += 1
                else:
                    x += 1
            elif d == S:
                if y == asteroid.y + radius:
                    d = W
                    x -= 1
                else:
                    y += 1
            elif d == W:
                if x == asteroid.x - radius:
                    d = N
                    y -= 1
                else:
                    x -= 1
            elif y == asteroid.y - radius:
                break
            else:
                y -= 1

    def find_best_location(self):
        self.detect_all()
        return max([a.visible for a in self.asteroids])

    def __str__(self):
        lines = []
        for y in range(self.height):
            if y not in self.map:
                lines.append(''.join(['.' for x in range(self.width)]))
            else:
                line = ''
                for x in range(self.width):
                    if x not in self.map[y]:
                        line += '.'
                    else:
                        line += str(self.map[y][x].visible)
                lines.append(line)
        return '\n'.join(lines)


with open('input.txt') as f:
    data = f.read().splitlines()

asteroid_map = AsteroidMap(data)
print(asteroid_map.find_best_location())