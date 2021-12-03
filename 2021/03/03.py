# yes this is terrible i wanted to get the points and might refactor this at a later point lol

def find_most_common_bits(binary_numbers):
    res = ''
    for i in range(len(binary_numbers[0])):
        nbits = ''.join(bn[i] for bn in binary_numbers)
        res += '1' if nbits.count('1') > nbits.count('0') else '0'
    return res


def get_oxygen(binary_numbers):
    for i in range(len(binary_numbers[0]) + 1):
        if len(binary_numbers) == 1:
            return binary_numbers[0]
        nbits = ''.join(bn[i] for bn in binary_numbers)
        b = '1' if nbits.count('1') >= nbits.count('0') else '0'
        binary_numbers = [bn for bn in binary_numbers[:] if bn[i] == b]


def get_co2(binary_numbers):
    for i in range(len(binary_numbers[0]) + 1):
        if len(binary_numbers) == 1:
            return binary_numbers[0]
        nbits = ''.join(bn[i] for bn in binary_numbers)
        b = '0' if nbits.count('1') >= nbits.count('0') else '1'
        binary_numbers = [bn for bn in binary_numbers[:] if bn[i] == b]


def part_1(data):
    gamma = find_most_common_bits(data)
    epsilon = gamma.replace('1', 'x').replace('0', '1').replace('x', '0')
    return int(gamma, 2) * int(epsilon, 2)


def part_2(data):
    return int(get_oxygen(data), 2) * int(get_co2(data), 2)


with open('input.txt') as f:
    data = f.read().splitlines()

print(part_2(data))
