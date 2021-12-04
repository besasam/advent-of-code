class BingoCard:
    def __init__(self, numbers: list):
        self.card = [[False for _ in range(5)] for _ in range(5)]
        self.numbers = dict()
        for i, row in enumerate(numbers):
            for k, num in enumerate(row):
                self.numbers[num] = (i, k)

    def play(self, n: int):
        if n not in self.numbers:
            return False
        (i, k) = self.numbers[n]
        self.card[i][k] = True
        return True

    def is_win(self):
        return any(all(row) for row in self.card) or any(all(col) for col in self._cols())

    def get_score(self):
        return sum(n for n, (i, k) in self.numbers.items() if not self.card[i][k])

    def _cols(self):
        return [[row[i] for row in self.card] for i in range(5)]

    def _diagonals(self):
        return [[self.card[i][i] for i in range(5)], [self.card[4-i][i] for i in range(5)]]

    def __str__(self):
        card = [['' for _ in range(5)] for _ in range(5)]
        for n, (i, k) in self.numbers.items():
            if self.card[i][k]:
                card[i][k] = '(' + str(n) + ')'
            else:
                card[i][k] = str(n)
        return '\n'.join(' '.join(row) for row in card)


class BingoSubsystem:
    def __init__(self, data: list):
        self.numbers = [int(n) for n in data[0].split(',')]
        self.cards = []
        cur = []
        for line in data[2:]:
            if line == '':
                self.cards.append(BingoCard(cur))
                cur = []
                continue
            cur.append([int(n) for n in line.split()])

    def play(self):
        for n in self.numbers:
            for card in self.cards:
                if card.play(n) and card.is_win():
                    return card, n
        return False

    def play_until_last(self):
        cards = self.cards[:]
        for n in self.numbers:
            for card in cards[:]:
                if card.play(n) and card.is_win():
                    if len(cards) == 1:
                        return card, n
                    cards.remove(card)
        return False


def part_1(data):
    bingo = BingoSubsystem(data)
    (winner, n) = bingo.play()
    return winner.get_score() * n


def part_2(data):
    bingo = BingoSubsystem(data)
    (winner, n) = bingo.play_until_last()
    return winner.get_score() * n


with open('input.txt') as f:
    data = f.read().splitlines()

print(part_2(data))
