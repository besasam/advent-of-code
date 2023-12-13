def minimize(record):
    return '.'.join([g for g in record.split('.') if g])


def trim_left(record, constraints):
    if not constraints:
        return record, constraints[:]
    c = constraints[0]
    chunks = record.split('.')
    if len(chunks[0]) <= c:
        return trim_left('.'.join(chunks[1:]), constraints[1:])
    return record, constraints[:]


def trim_right(record, constraints):
    if not constraints:
        return record, constraints[:]
    c = constraints[-1]
    groups = record.split('.')
    if len(groups[-1]) <= c:
        return trim_right('.'.join(groups[:-1]), constraints[:-1])
    return record, constraints[:]


def trim(record, constraints):
    r, c = trim_left(minimize(record), constraints)
    return trim_right(r, c)


def possible_solutions(record, constraints):
    record, constraints = trim(record, constraints)
    print(record)
    print(constraints)
    print()
    if not constraints or len(record) == sum(constraints) + len(constraints) - 1:
        return 1
    print()
    return -1


def part_1(data):
    test_results = [1, 4, 1, 1, 4, 10]
    for i, line in enumerate(data):
        constraints = [int(x) for x in line[1].split(',')]
        res = possible_solutions(line[0], constraints)
        print()
        print('SOLUTIONS:', res)
        print('SHOULD BE:', test_results[i])
        print()
        print(100*'-')
        print()


with open('test.txt') as f:
    data = [line.split(' ') for line in f.read().splitlines()]

print(part_1(data))
