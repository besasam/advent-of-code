debugging = True


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


def debug(string):
    if debugging:
        print(string)


class Asteroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vectors = []
        self.targets = []
        self.visible = 0
        self.value = 0

    def detect(self, asteroid):
        if asteroid == self:
            return
        x, y = [asteroid.x - self.x, asteroid.y - self.y]
        d = gcd(x, y)
        x, y = x//d, y//d
        if [x, y] in self.vectors:
            return False
        self.vectors.append([x, y])
        self.targets.append(asteroid)
        self.visible += 1
        return True

    def get_vector(self, coords):
        x, y = coords[0] - self.x, coords[1] - self.y
        d = gcd(x, y)
        return [x//d, y//d]

    def val(self):
        return '#' if self.value == 0 else str(self.value)

    def __str__(self):
        return f'<{self.x},{self.y}>: {self.visible}'


class AsteroidMap:
    def __init__(self, data):
        self.map = dict()
        self.asteroids = []
        self.width = len(data[0])
        self.height = len(data)
        self.count = 0
        for y, line in enumerate(data):
            for x, char in enumerate(line):
                if char == '#':
                    self.insert(x, y)

    def insert(self, x, y):
        asteroid = Asteroid(x, y)
        if y not in self.map:
            self.map.update({y: {x: asteroid}})
        else:
            self.map[y].update({x: asteroid})
        self.asteroids.append(asteroid)
        self.count += 1
        return asteroid

    def detect_all(self):
        for a in self.asteroids:
            r = 1
            while r < self.width or r < self.height:
                self.detect(a, r)
                r += 1

    def detect(self, asteroid, radius):
        if radius == 0:
            return
        N, E, S, W, E2 = [0, 1, 2, 3, 4]
        x = asteroid.x
        y = asteroid.y - radius
        d = E
        while True:
            if y in self.map and x in self.map[y]:
                asteroid.detect(self.map[y][x])
                yield [x, y]
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
            elif d == N:
                if y == asteroid.y - radius:
                    d = E2
                    x += 1
                else:
                    y -= 1
            elif x == asteroid.x:
                break
            else:
                x += 1

    def detect_all_from_one(self, asteroid):
        r = 1
        detected = []
        while r < self.width or r < self.height:
            detected.extend([x for x in self.detect(asteroid, r)])
            r += 1
        return detected

    def find_best_location(self):
        self.detect_all()
        best = None
        for a in self.asteroids:
            if best is None or a.visible > best.visible:
                best = a
        return best

    def pewpew(self, asteroid: Asteroid=None, search=1):
        if asteroid is None:
            asteroid = self.find_best_location()
        asteroid.vectors = []
        asteroid.targets = []
        vaporized = 0
        border = self.get_border(asteroid.x)
        for b in border:
            debug(f'{b} -> {asteroid.get_vector(b)}')
        return

    def rotate(self, asteroid: Asteroid):
        start_x, start_y = asteroid.x, asteroid.y

    def get_border(self, x):
        w, h = self.width, self.height
        return [[x+i, 0] for i in range(w-x)] + \
               [[w-1, i] for i in range(1, h)] + \
               [[w-i, h-1] for i in range(2, w)] + \
               [[0, h-i] for i in range(1, h)] + \
               [[i, 0] for i in range(w-x-1)]

    def __str__(self):
        lines = []
        for y in range(self.height):
            if y not in self.map:
                lines.append(''.join(['.' for x in range(self.width)]))
            else:
                lines.append(''.join(['.' if x not in self.map[y] else self.map[y][x].val() for x in range(self.width)]))
        return '\n'.join(lines)


with open('input.txt') as f:
    data = f.read().splitlines()

with open('example2.txt') as f:
    example = f.read().splitlines()

asteroid_map = AsteroidMap(example)
station = asteroid_map.map[3][8]
print(asteroid_map.pewpew(station, 10))

# w, h = asteroid_map.width, asteroid_map.height
# x = 8
# border = [[x+i, 0] for i in range(w-x)] + \
#          [[w-1, i] for i in range(1, h)] + \
#          [[w-i, h-1] for i in range(2, w)] + \
#          [[0, h-i] for i in range(1, h)] + \
#          [[i, 0] for i in range(w-x-1)]
# test = [['.' for x in range(w)] for y in range(h)]
# for x, y in border:
#     test[y][x] = '#'
# for t in test:
#     debug(t)