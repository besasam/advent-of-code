class SpaceCards:
    def __init__(self):
        self.p1 = []
        self.p2 = []

    def play(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        while self.p1 and self.p2:
            self.round()

    def round(self):
        v1 = self.p1.pop(0)
        v2 = self.p2.pop(0)
        if v1 > v2:
            self.p1 += [v1, v2]
        else:
            self.p2 += [v2, v1]


class RecursiveSpaceCards:
    def __init__(self):
        self.p1 = []
        self.p2 = []
        self.p1_cache = []
        self.p2_cache = []

    def play(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        while self.p1 and self.p2:
            if self.p1 in self.p1_cache and self.p2 in self.p2_cache:
                return 1
            else:
                self.p1_cache.append(self.p1[:])
                self.p2_cache.append(self.p2[:])
            self.round()
        return 1 if self.p1 else 2

    def round(self):
        v1 = self.p1.pop(0)
        v2 = self.p2.pop(0)
        if v1 > len(self.p1) or v2 > len(self.p2):
            if v1 > v2:
                self.p1 += [v1, v2]
            else:
                self.p2 += [v2, v1]
        else:
            new_game = RecursiveSpaceCards().play(self.p1[:v1], self.p2[:v2])
            if new_game == 1:
                self.p1 += [v1, v2]
            else:
                self.p2 += [v2, v1]


def get_score(deck):
    res = 0
    i = len(deck)
    for card in deck:
        res += i * card
        i -= 1
    return res


def part_1(data):
    cards = SpaceCards()
    cards.play(data[0], data[1])
    winner = cards.p1 if cards.p1 else cards.p2
    return get_score(winner)


def part_2(data):
    cards = RecursiveSpaceCards()
    cards.play(data[0], data[1])
    winner = cards.p1 if cards.p1 else cards.p2
    return get_score(winner)


with open('input.txt') as f:
    data = [[int(x) for x in d.split(': ')[1].split()] for d in ' '.join([x if x != '' else '###' for x in f.read().splitlines()]).split(' ### ')]
    # kids, don't try this at home

print(part_2(data))