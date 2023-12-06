from numpy import prod


def d(t, s):
    return (t - s) * s


def part_1(data):
    return prod([sum([d(t, s) > r for s in range(t)]) for (t, r) in data])


def part_2(data):
    (t, r) = data
    return sum([d(t, s) > r for s in range(t)])


test = [(7, 9), (15, 40), (30, 200)]
test_2 = (71530, 940200)
data = [(58, 478), (99, 2232), (64, 1019), (69, 1071)]
data_2 = (58996469, 478223210191071)

print(part_2(data_2))
