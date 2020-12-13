def part_1(data):
    arrival_time, buses = data[0], [d for d in data[1] if d is not None]
    times = [(bus, bus - (arrival_time % bus)) for bus in buses]
    for t in times:
        if t[1] == min([t[1] for t in times]):
            return t[0] * t[1]


def part_2(data):
    buses = data[1]
    t = 0
    cycle = buses.pop(0)
    for i, bus in enumerate(buses, 1):
        if bus is None:
            continue
        while True:
            t += cycle
            if (t + i) % bus == 0:
                cycle *= bus
                break
    return t


with open('input.txt') as f:
    data = [[int(l) if l.isdigit() else None for l in line.split(',')] if ',' in line else int(line) for line in f.read().splitlines()]

print(part_2(data))