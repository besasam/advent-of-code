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
        self.targets = []
        self.visible = 0

    def detect(self, asteroid):
        if asteroid == self:
            return
        x, y = [asteroid.x - self.x, asteroid.y - self.y]
        d = gcd(x, y)
        x, y = x//d, y//d
        if [x, y] in self.vectors:
            print(f'Could not detect: Blocked by [{x}, {y}]')
            return False
        print(f'Asteroid detected')
        self.vectors.append([x, y])
        self.targets.append(asteroid)
        self.visible += 1
        return True

    def get_vector(self, coords):
        x, y = coords[0] - self.x, coords[1] - self.y
        d = gcd(x, y)
        return [x//d, y//d]

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
        print()
        print(f'Detecting at radius {radius}')
        N, E, S, W, E2 = [0, 1, 2, 3, 4]
        x = asteroid.x
        y = asteroid.y - radius
        print(f'Starting coordinates: [{x}, {y}]')
        print()
        d = E
        while True:
            if y in self.map and x in self.map[y]:
                print(f'Asteroid found at [{x}, {y}]')
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
        print(f'Detecting all from asteroid {asteroid}')
        r = 1
        while r < self.width or r < self.height:
            self.detect(asteroid, r)
            r += 1

    def find_best_location(self):
        self.detect_all()
        best = None
        for a in self.asteroids:
            if best is None or a.visible > best.visible:
                best = a
        return best

    def pewpew(self, asteroid=None, search=1):
        if asteroid is None:
            asteroid = self.find_best_location()
        asteroid.vectors = []
        asteroid.targets = []
        vaporized = 0
        border = self.get_border(asteroid.x)
        for bx, by in border:
            x, y = asteroid.x, asteroid.y
            vx, vy = asteroid.get_vector([bx, by])
            while 0 < x < self.width and 0 < y < self.height:
                x, y = x + vx, y + vy
                if y in self.map and x in self.map[y]:
                    a = self.map[y].pop(x)
                    vaporized += 1
                    if vaporized == search:
                        return a
                    break
        return

        # N, E, S, W, E2 = [0, 1, 2, 3, 4]
        # while self.count > 1:
        #     r = 1
        #     d = E
        #     x = asteroid.x
        #     y = 0
        #     while r < self.width or r < self.height:
        #         while True:
        #             if y in self.map and x in self.map[y]:
        #                 a = self.map[y].pop(x)
        #                 vaporized += 1
        #                 if vaporized == search:
        #                     return a
        #             if d == E:
        #                 if x == asteroid.x + r:
        #                     d = S
        #                     y += 1
        #                 else:
        #                     x += 1
        #             elif d == S:
        #                 if y == asteroid.y + r:
        #                     d = W
        #                     x -= 1
        #                 else:
        #                     y += 1
        #             elif d == W:
        #                 if x == asteroid.x - r:
        #                     d = N
        #                     y -= 1
        #                 else:
        #                     x -= 1
        #             elif d == N:
        #                 if y == asteroid.y - r:
        #                     d = E2
        #                     x += 1
        #                 else:
        #                     y -= 1
        #             elif x == asteroid.x:
        #                 break
        #             else:
        #                 x += 1
        # return
        #     station.vectors = []
        #     station.targets = []
        #     self.detect_all_from_one(station)
        #     while station.targets:
        #         a = station.targets.pop(0)
        #         self.map[a.y].pop(a.x)
        #         vaporized += 1
        #         if vaporized == search:
        #             return a
        # return

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
                line = ''
                for x in range(self.width):
                    if x not in self.map[y]:
                        line += '.'
                    else:
                        line += '#' #str(self.map[y][x].visible)
                lines.append(line)
        return '\n'.join(lines)


with open('input.txt') as f:
    data = f.read().splitlines()

with open('example2.txt') as f:
    example = f.read().splitlines()

asteroid_map = AsteroidMap(example)
station = asteroid_map.map[3][8]
print(asteroid_map.pewpew(station, 3))

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
#     print(t)