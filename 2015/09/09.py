import itertools


def route_distance(route: tuple, routes: dict):
    dist = 0
    prev = None
    for loc in route:
        if prev is not None:
            dist += routes[prev][loc]
        prev = loc
    return dist


def get_routes(data: list):
    routes = dict()
    for d in data:
        start, dest, dist = d
        if start not in routes:
            routes[start] = dict()
        if dest not in routes:
            routes[dest] = dict()
        routes[start][dest] = dist
        routes[dest][start] = dist
    return routes


def part_1(routes: dict):
    locations = routes.keys()
    return min([route_distance(r, routes) for r in list(itertools.permutations(locations))])


def part_2(routes: dict):
    locations = routes.keys()
    return max([route_distance(r, routes) for r in list(itertools.permutations(locations))])


with open('input.txt') as f:
    routes = get_routes([[s[0], s[2], int(s[-1])] for s in [line.split() for line in f.read().splitlines()]])

print(part_2(routes))
