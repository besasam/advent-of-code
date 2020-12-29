import itertools


def get_guest_list(data: list):
    guests = dict()
    for d in data:
        g1, g2, s = d
        if g1 not in guests:
            guests[g1] = dict()
        guests[g1][g2] = s
    return guests


def happiness_score(guests: dict, seating: tuple):
    score = 0
    for i in range(len(seating)):
        g1 = seating[i]
        g2 = seating[0] if i == len(seating)-1 else seating[i+1]
        score += guests[g1][g2] + guests[g2][g1]
    return score


def part_1(guests: dict):
    names = guests.keys()
    return max([happiness_score(guests, s) for s in list(itertools.permutations(names))])


def part_2(guests: dict):
    names = list(guests.keys())
    guests['yourself'] = dict()
    for n in names:
        guests['yourself'][n] = 0
        guests[n]['yourself'] = 0
    return part_1(guests)


with open('input.txt') as f:
    guests = get_guest_list([[s[0], s[-1][:-1], int(s[3]) if s[2] == 'gain' else -int(s[3])] for s in [line.split() for line in f.read().splitlines()]])

print(part_2(guests))
