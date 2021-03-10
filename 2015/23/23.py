class Computer:
    def __init__(self, register: list):
        self.register = dict()
        for r in register:
            self.register[r] = 0
        self.cur = 0

    def run(self, program: list):
        self.cur = 0
        while 0 <= self.cur < len(program):
            self.execute(program[self.cur])
        return True

    def execute(self, instruction: str):
        i = instruction.split()
        if i[0] == 'hlf':
            self.register[i[1]] //= 2
            self.cur += 1
        elif i[0] == 'tpl':
            self.register[i[1]] *= 3
            self.cur += 1
        elif i[0] == 'inc':
            self.register[i[1]] += 1
            self.cur += 1
        elif i[0] == 'jmp':
            self.cur += int(i[1])
        else:
            r = i[1][:-1]
            if i[0] == 'jie':
                self.cur += int(i[2]) if self.register[r] % 2 == 0 else 1
            elif i[0] == 'jio':
                self.cur += int(i[2]) if self.register[r] == 1 else 1


def part_1(data):
    computer = Computer(['a', 'b'])
    computer.run(data)
    return computer.register


def part_2(data):
    computer = Computer(['a', 'b'])
    computer.register['a'] = 1
    computer.run(data)
    return computer.register


with open('input.txt') as f:
    data = f.read().splitlines()

print(part_2(data))
