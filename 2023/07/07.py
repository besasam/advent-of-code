class Hand:
    SUITS = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    JOKER_SUITS = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

    def __init__(self, cards: str, bid: str, has_joker: bool = False):
        self.cards = cards
        self.bid = int(bid)
        self.score = self._get_score() if not has_joker else self._get_jokered_score()
        self.suits = self.SUITS if not has_joker else self.JOKER_SUITS

    def _get_score(self):
        counts = {s: self.cards.count(s) for s in set(self.cards)}
        if len(counts) == 1:
            return 6                                    # five of a kind
        if len(counts) == 2:
            if any(counts[c] == 4 for c in counts):
                return 5                                # four of a kind
            return 4                                    # full house
        if len(counts) == 3:
            if any(counts[c] == 3 for c in counts):
                return 3                                # three of a kind
            return 2                                    # two pair
        if len(counts) == 4:
            return 1                                    # one pair
        return 0                                        # high card

    def _get_jokered_score(self):
        if 'J' not in self.cards:
            return self._get_score()
        counts = {s: self.cards.count(s) for s in set(self.cards) if s != 'J'}
        jokers = self.cards.count('J')
        if jokers == 1:
            if len(counts) == 1:
                return 6                                    # 2222J -> 22222
            if len(counts) == 2:
                if any(counts[c] == 3 for c in counts):
                    return 5                                # 2223J -> 22232
                return 4                                    # 2233J -> 22333
            if len(counts) == 3:
                return 3                                    # 2234J -> 22342
            return 1                                        # 2345J -> 23452
        if jokers == 2:
            if len(counts) == 1:
                return 6                                    # 222JJ -> 22222
            if len(counts) == 2:
                return 5                                    # 223JJ -> 22222
            return 3                                        # 234JJ -> 23422
        if jokers == 3:
            if len(counts) == 1:
                return 6
            return 5
        return 6

    def __gt__(self, other):
        if self.score == other.score:
            for i in range(len(self.cards)):
                if self.cards[i] != other.cards[i]:
                    return self.suits.index(self.cards[i]) < self.suits.index(other.cards[i])
        return self.score > other.score

    def __repr__(self):
        return self.cards


def part_1(data):
    cards = [Hand(l[0], l[1]) for l in data]
    cards.sort()
    return sum((i+1)*hand.bid for i, hand in enumerate(cards))


def part_2(data):
    cards = [Hand(l[0], l[1], True) for l in data]
    cards.sort()
    return sum((i + 1) * hand.bid for i, hand in enumerate(cards))


with open('input.txt') as f:
    data = [line.split() for line in f.read().splitlines()]

print(part_2(data))
