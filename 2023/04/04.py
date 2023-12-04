def part_1(data):
    return sum(0 if (wins := sum(n in line[0] for n in line[1])) == 0 else 2**(wins-1) for line in data)


def part_2(data):
    cards = {i: 1 for i in range(len(data))}
    for i, card in enumerate(data):
        wins = sum(n in card[0] for n in card[1])
        if wins > 0:
            for k in range(wins if wins < (r := len(cards)-i-1) else r):
                cards[i+k+1] += cards[i]
    return sum(cards.values())


with open('input.txt') as f:
    data = [[n.split() for n in m] for m in [l.split(' | ') for l in [line[line.find(':')+2:] for line in f.read().splitlines()]]]

print(part_1(data))
