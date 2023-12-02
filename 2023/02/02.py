def parse(s):
    cubes = [x.split() for x in s]
    res = {'red': 0, 'green': 0, 'blue': 0}
    for cube in cubes:
        res[cube[1]] += int(cube[0])
    return res


def is_possible(game, target):
    for round in game:
        for cube in round.keys():
            if round[cube] > target[cube]:
                return False
    return True


def minimum_set(game):
    return {cube: max(g[cube] for g in game) for cube in ['red', 'green', 'blue']}


def power(cubes):
    return cubes['red'] * cubes['green'] * cubes['blue']


def part_1(data):
    games = [[parse(l) for l in line] for line in data]
    target = {'red': 12, 'green': 13, 'blue': 14}
    possible_games = []
    for i, game in enumerate(games):
        if is_possible(game, target):
            possible_games.append(i+1)
    return sum(possible_games)


def part_2(data):
    games = [[parse(l) for l in line] for line in data]
    return sum(power(minimum_set(game)) for game in games)


with open('input.txt') as f:
    data = [[s.split(', ') for s in line] for line in [line[line.find(':')+2:].split('; ') for line in f.read().splitlines()]]

print(part_2(data))
