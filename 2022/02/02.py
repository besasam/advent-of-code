ROCK = 1
PAPER = 2
SCISSORS = 3

WIN = 6
DRAW = 3
LOSE = 0


def shape(x):
    return ROCK if x in ['A', 'X'] else PAPER if x in ['B', 'Y'] else SCISSORS


def outcome(x):
    return LOSE if x == 'X' else DRAW if x == 'Y' else WIN


def get_outcome(opponent, self):
    if self == opponent:
        return DRAW
    elif (self == ROCK and opponent == PAPER) or (self == PAPER and opponent == SCISSORS) or (self == SCISSORS and opponent == ROCK):
        return LOSE
    else:
        return WIN


def shape_by_outcome(opponent, outcome):
    if outcome == DRAW:
        return opponent
    elif (outcome == WIN and opponent == ROCK) or (outcome == LOSE and opponent == SCISSORS):
        return PAPER
    elif (outcome == WIN and opponent == PAPER) or (outcome == LOSE and opponent == ROCK):
        return SCISSORS
    else:
        return ROCK


def score(a, b, is_part_2=False):
    score = shape_by_outcome(a, b) if is_part_2 else get_outcome(a, b)
    return score + b


def part_1(data):
    return sum(score(shape(opponent), shape(self)) for [opponent, self] in data)


def part_2(data):
    return sum(score(shape(opponent), outcome(result), True) for [opponent, result] in data)


with open('input.txt') as f:
    data = [l.split(' ') for l in f.read().splitlines()]

print(part_2(data))
