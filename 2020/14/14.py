import re
import itertools


class FerryDocker:
    def __init__(self):
        self.memory = dict()
        self.bitmask = dict()

    def run(self, program):
        for line in program:
            if line[0] == 'mask':
                self.update_bitmask(line[1])
            else:
                address = int(re.findall(r'\d+', line[0])[0])
                integer_value = int(line[1])
                self.save_to_memory(address, integer_value)

    def save_to_memory(self, address, integer_value):
        self.memory[address] = int(self.apply_bitmask(format(integer_value, '036b')), 2)

    def update_bitmask(self, bitmask_string):
        self.bitmask = dict()
        for i, bit in enumerate(bitmask_string):
            if bit != 'X':
                self.bitmask[i] = bit

    def apply_bitmask(self, binary_num, bitmask=None):
        if bitmask is None:
            bitmask = self.bitmask
        result = ''
        for i, bit in enumerate(binary_num):
            if i in bitmask:
                result += bitmask[i]
            else:
                result += bit
        return result


class FerryDockerV2(FerryDocker):
    def __init__(self):
        super().__init__()
        self.bitmasks = []

    def save_to_memory(self, address, integer_value):
        for bitmask in self.bitmasks:
            modified_address = int(self.apply_bitmask(format(address, '036b'), bitmask), 2)
            self.memory[modified_address] = integer_value

    def update_bitmask(self, bitmask_string):
        self.bitmasks = []
        bitmask = dict()
        floating_bits = []
        for i, bit in enumerate(bitmask_string):
            if bit == '1':
                bitmask[i] = bit
            elif bit == 'X':
                floating_bits.append(i)
        floating_bits_values = itertools.product([0, 1], repeat=len(floating_bits))
        for tup in floating_bits_values:
            bitmask_with_floats = bitmask.copy()
            for i, k in enumerate(floating_bits):
                bitmask_with_floats[k] = str(tup[i])
            self.bitmasks.append(bitmask_with_floats)


def part_1(data):
    docker = FerryDocker()
    docker.run(data)    # haha get it
    return sum(docker.memory.values())


def part_2(data):
    docker = FerryDockerV2()
    docker.run(data)
    return sum(docker.memory.values())


with open('input.txt') as f:
    data = [line.split(' = ') for line in f.read().splitlines()]

print(part_2(data))
