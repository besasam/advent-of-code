def part_1(instructions: str):
    return instructions.count('(') - instructions.count(')')


def part_2(instructions: str):
    floor = 0
    for pos, i in enumerate(instructions):
        floor += 1 if i == '(' else -1
        if floor == -1:
            return pos + 1


with open('input.txt') as f:
    data = f.readline()

print(part_2(data))
