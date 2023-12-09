def make_sequences(sequences):
    cur = sequences[-1]
    nex = [cur[i+1] - cur[i] for i in range(len(cur)-1)]
    sequences.append(nex)
    if all(x == 0 for x in nex):
        return sequences
    return make_sequences(sequences)


def extrapolate(sequences):
    for i in reversed(range(len(sequences)-1)):
        sequences[i].append(sequences[i][-1] + sequences[i+1][-1])
    return sequences[0][-1]


def etalopartxe(sequences):
    for i in reversed(range(len(sequences)-1)):
        sequences[i].insert(0, sequences[i][0] - sequences[i+1][0])
    return sequences[0][0]


def part_1(data):
    return sum(extrapolate(make_sequences([line])) for line in data)


def part_2(data):
    return sum(etalopartxe(make_sequences([line])) for line in data)


with open('input.txt') as f:
    data = [[int(x) for x in line.split()] for line in f.read().splitlines()]

print(part_2(data))
