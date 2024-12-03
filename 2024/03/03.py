import re


def part_1(memory: str) -> int:
    pattern = r"mul\((\d{1,3}),\s*(\d{1,3})\)"
    matches = re.findall(pattern, memory)
    return sum(int(m[0]) * int(m[1]) for m in matches)


def part_2(memory: str) -> int:
    chunks = re.split(r"(do\(\)|don't\(\))", memory)
    valid_chunks = []
    enabled = True
    for chunk in chunks:
        if chunk == "do()":
            enabled = True
        elif chunk == "don't()":
            enabled = False
        elif enabled:
            valid_chunks.append(chunk)
    return part_1(''.join(valid_chunks))


with open('input.txt') as f:
    data = f.read()

print(part_2(data))
