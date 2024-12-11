def blink_all_stones(stones: list) -> list:
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif not (l := len(str(stone))) % 2:
            new_stones.append(int(str(stone)[:l//2]))
            new_stones.append(int(str(stone)[l//2:]))
        else:
            new_stones.append(stone*2024)
    return new_stones


blinks = dict()  # blackpink in your area
blink_lengths = dict()


def blink(stone: int) -> list:
    if stone not in blinks:
        if stone == 0:
            blinks[stone] = [1]
        elif not (l := len(str(stone))) % 2:
            blinks[stone] = [int(str(stone)[:l//2]), int(str(stone)[l//2:])]
        else:
            blinks[stone] = [stone*2024]
    return blinks[stone]


def blink_length(stone: int, current_cycle: int=0, total_cycles: int=75) -> int:
    if stone not in blink_lengths:
        blink_lengths[stone] = dict()
    cycle = total_cycles - current_cycle
    if cycle in blink_lengths[stone]:
        return blink_lengths[stone][cycle]
    nex = blink(stone)
    blink_lengths[stone][current_cycle] = len(nex)
    if current_cycle == total_cycles:
        return blink_lengths[stone][current_cycle]
    return sum(blink_length(new_stone, current_cycle+1, total_cycles) for new_stone in nex)


def part_1(data: list, cycles: int=25) -> int:
    res = data
    for _ in range(cycles):
        res = blink_all_stones(res)
    return len(res)


def part_2(data: list) -> int:
    # keeping this for posterity
    # return part_1(data, 75)  # our father Landau who art in heaven, hallowed be thy runtime
    return sum(blink_length(stone) for stone in data)


with open('input.txt') as f:
    data = [int(x) for x in f.readline().split()]

print(part_2(data))
