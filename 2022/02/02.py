rock = ['A', 'X']
paper = ['B', 'Y']
scissors = ['C', 'Z']


def score(own, opp):
    s = 1 if own in rock else 2 if own in paper else 3
    if (own in rock and opp in rock) or (own in paper and opp in paper) or (own in scissors and opp in scissors):
        s += 3
    elif (opp in rock and own in paper) or (opp in paper and own in scissors) or (opp in scissors and own in rock):
        s += 6
    return s


def score_2(own, opp):
    s = 6 if own == 'Z' else 3 if own == 'Y' else 0
    if opp in rock:
        s += 1 if own == 'Y' else 2 if own == 'Z' else 3
    elif opp in paper:
        s += 2 if own == 'Y' else 3 if own == 'Z' else 1
    else:
        s += 3 if own == 'Y' else 1 if own == 'Z' else 2
    return s


def part_1(data):
    return sum(score(l[1], l[0]) for l in data)


def part_2(data):
    return sum(score_2(l[1], l[0]) for l in data)


with open('input.txt') as f:
    data = [l.split(' ') for l in f.read().splitlines()]

print(part_2(data))
