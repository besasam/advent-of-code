debug = False


class ModuloList(list):
    def __getitem__(self, key):
        if type(key) == slice:
            start = None if key.start is None else int(WrappingInteger(int(key.start), len(self)))
            stop = None if key.stop is None else int(WrappingInteger(int(key.stop), len(self)))
            if start is not None and stop is not None and start > stop:
                return ModuloList(super().__getitem__(slice(start, None, key.step)) + super().__getitem__(slice(None, stop, key.step)))
            return ModuloList(super().__getitem__(slice(start, stop, key.step)))
        if type(key) == WrappingInteger:
            return super().__getitem__(int(key))
        return super().__getitem__(int(WrappingInteger(key, len(self))))

    def __contains__(self, item):
        return int(item) in [int(x) for x in self]

    def index(self, item, **kwargs):
        return [int(x) for x in self].index(int(item))

    def pop(self, key):
        if type(key) == WrappingInteger:
            return super().pop(int(key))
        return super().pop(int(WrappingInteger(key, len(self))))


class WrappingInteger:
    def __init__(self, val: int, ceil: int, floor: int = 0):
        self.ceil = ceil
        self.floor = floor
        m = val % ceil
        if floor == 1 and m == 0:
            self.val = ceil
        else:
            self.val = m

    def __add__(self, other):
        return WrappingInteger(self.val + other, self.ceil, self.floor)

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        self.val = int(self.__add__(other))
        return self

    def __sub__(self, other):
        return WrappingInteger(self.val - other, self.ceil, self.floor)

    def __rsub__(self, other):
        return WrappingInteger(other - self.val, self.ceil, self.floor)

    def __isub__(self, other):
        self.val = int(self.__sub__(other))
        return self

    def __eq__(self, other):
        return self.val == int(other)

    def __lt__(self, other):
        return self.val < int(other)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(self.val)

    def __int__(self):
        return self.val


class TwoCrabsOneCup:   # i am so sorry
    def __init__(self, cups: str):
        self.cups = ModuloList([WrappingInteger(int(c), 9, 1) for c in cups])
        self.n = len(cups)
        self.p = WrappingInteger(0, self.n)
        self.round = 1

    def move(self):
        cur = self.cups[self.p]
        start = self.p + 1
        stop = self.p + 4
        pickup = self.cups[start:stop]
        if start < stop:
            self.cups = self.cups[:start] + self.cups[stop:]
        else:
            self.cups = self.cups[stop:start]
        destination = cur - 1
        while destination in pickup:
            destination -= 1
        di = self.cups.index(destination)
        self.cups = ModuloList(self.cups[:di+1] + pickup + self.cups[di+1:])
        self.p = WrappingInteger(self.cups.index(cur) + 1, self.n)
        self.round += 1


class OneCrabManyCups:
    def __init__(self, cups: str, n: int = 9):
        self.cups = dict()
        self.n = n
        for i, c in enumerate(cups[:-1]):
            self.cups[int(c)] = int(cups[i+1])
        if n > 9:
            self.cups[int(cups[-1])] = 10
            for i in range(10, n):
                self.cups[i] = i + 1
            self.cups[n] = int(cups[0])
        else:
            self.cups[int(cups[-1])] = int(cups[0])
        self.cur = WrappingInteger(int(cups[0]), n, 1)
        self.round = 1

    def move(self):
        pickup = [first := self.cups[int(self.cur)], second := self.cups[first], third := self.cups[second]]
        destination = self.cur - 1
        while destination in pickup:
            destination -= 1
        if debug: print(f'-- move {self.round} --\ncups: {self.print_cups()}\npick up: {pickup}\ndestination: {destination}\n')
        self.cups[int(self.cur)] = self.cups[third]
        self.cups[third] = self.cups[int(destination)]
        self.cups[int(destination)] = first
        self.cur = WrappingInteger(self.cups[int(self.cur)], self.n, 1)
        self.round += 1

    def print_cups(self):
        res = f'({self.cur}) '
        nex = self.cups[int(self.cur)]
        while nex != int(self.cur):
            res += f'{nex} '
            nex = self.cups[nex]
        return res


def part_1(cups_string):
    cup_game = TwoCrabsOneCup(cups_string)
    for _ in range(100):
        cup_game.move()
    i = cup_game.cups.index(1)
    return ''.join([str(x) for x in cup_game.cups[i+1:i]])


def part_2(cups_string):
    cup_game = OneCrabManyCups(cups_string, 1000000)
    for _ in range(10000000):
        cup_game.move()
    return cup_game.cups[1] * cup_game.cups[cup_game.cups[1]]


print(part_2('538914762'))
