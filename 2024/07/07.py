def is_possible(result: int, sequence: list, part_2: bool=False) -> bool:
    if sequence[0] > result:
        return False
    if len(sequence) == 1:
        return sequence[0] == result
    sequence_add = [(nex := sequence[:]).pop(0) + nex.pop(0)] + nex
    sequence_mult = [(nex := sequence[:]).pop(0) * nex.pop(0)] + nex
    if not part_2:
        return is_possible(result, sequence_add) or is_possible(result, sequence_mult)
    sequence_concat = [int(str((nex := sequence[:]).pop(0)) + str(nex.pop(0)))] + nex
    return is_possible(result, sequence_add, True) or is_possible(result, sequence_mult, True) or is_possible(result, sequence_concat, True)


def part_1(data: list) -> int:
    return sum(equation['result'] for equation in data if is_possible(equation['result'], equation['sequence']))


def part_2(data: list) -> int:
    return sum(equation['result'] for equation in data if is_possible(equation['result'], equation['sequence'], True))


with open('input.txt') as f:
    data = [{'result': int(d[0][:-1]), 'sequence': [int(x) for x in d[1:]]} for d in [line.split() for line in f.read().splitlines()]]

print(part_2(data))
