def execute(stacks: dict, instruction: list) -> None:
    [amount, move_from, move_to] = instruction
    while amount > 0:
        stacks[move_to].append(stacks[move_from].pop())
        amount -= 1


def execute_2(stacks: dict, instruction: list) -> None:
    [amount, move_from, move_to] = instruction
    moved = stacks[move_from][-amount:]
    stacks[move_from] = stacks[move_from][:-amount]
    stacks[move_to] += moved


def part_1(stacks: dict, instructions: list) -> str:
    for i in instructions:
        execute(stacks, i)
    return ''.join(stacks[s][-1] for s in stacks)


def part_2(stacks: dict, instructions: list) -> str:
    for i in instructions:
        execute_2(stacks, i)
    return ''.join(stacks[s][-1] for s in stacks)


with open('input.txt') as f:
    data = [line.split('\n') for line in f.read().split('\n\n')]

stacks = {i: [] for i in range(1, int(data[0].pop()[-1][-1]) + 1)}
for row in data[0]:
    items = [row[i+1:i+2] for i in range(0, len(row), 4)]
    for i, c in enumerate(items):
        if c != ' ':
            stacks[i+1] = [c] + stacks[i+1]

instructions = [[int(c) for c in row.split(' ') if c.isdigit()] for row in data[1]]

print(part_2(stacks, instructions))
