def solve(initial_state: str, days: int):
    state = [initial_state.count(str(i)) for i in range(7)]
    buffer = [0, 0]
    for i in range(days):
        mature_fish = buffer.pop(0)
        new_fish = state.pop(0)
        buffer.append(new_fish)
        state.append(new_fish + mature_fish)
    return sum(state) + sum(buffer)


def part_1(data):
    return solve(data, 80)


def part_2(data):
    return solve(data, 256)


with open('input.txt') as f:
    data = f.readline()

print(part_2(data))
