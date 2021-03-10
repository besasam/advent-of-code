from string import ascii_lowercase


def react(polymer: str):
    result = ''
    i = 0
    while i < len(polymer):
        try:
            last_char = result[-1]
        except IndexError:
            last_char = ''
        if last_char.swapcase() == polymer[i]:
            result = result[:-1]
        else:
            result += polymer[i]
        i += 1
    return result


def react_recursive(polymer: str, prev: str = ''):
    if polymer == '':
        return ''
    if prev != '' and polymer == prev:
        return polymer
    return react_recursive(react(polymer), polymer)


def part_1(data):
    return len(react_recursive(data))


def part_2(data):
    polymers = []
    for c in ascii_lowercase:
        new_polymer = data.replace(c, '').replace(c.upper(), '')
        polymers.append(new_polymer)
    smallest = len(data)
    for polymer in polymers:
        reaction = len(react_recursive(polymer))
        if reaction < smallest:
            smallest = reaction
    return smallest


with open('input.txt') as f:
    data = f.read()

print(part_2(data))