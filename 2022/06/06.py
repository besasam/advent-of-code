def find_marker(signal: str, length: int) -> int:
    for i in range(length-1, len(signal)):
        if len(set(signal[i-length+1:i+1])) == length:
            return i+1
    return -1


def part_1(data: str) -> int:
    return find_marker(data, 4)


def part_2(data: str) -> int:
    return find_marker(data, 14)


tests = [
    'mjqjpqmgbljsphdztnvjfqwrcgsmlb',
    'bvwbjplbgvbhsrlpgdmjqwftvncz',
    'nppdvjthqldpwncqszvftbrmjlhg',
    'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg',
    'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'
]

with open('input.txt') as f:
    data = f.readline()

print(part_2(data))
