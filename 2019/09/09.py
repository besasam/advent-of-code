class Intcode:
    STOP, ADD, MUL, IN, OUT, JMP_T, JMP_F, LT, EQ, ADJ = [99, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    MODE_POS, MODE_IMM, MODE_REL = [0, 1, 2]
    p = None
    cur = 0
    offset = 0
    input = None
    output = []

    def run(self, program, input):
        self.p = program
        self.input = input
        self.cur = 0
        self.offset = 0
        loop = 1
        while True:
            c = self.cur
            code = self.parse(self.p[c])
            print(f'{loop}: {self.p[c]} {code}')
            if code['cmd'] == self.STOP:
                print('STOP')
                print(self.p)
                return self.output
            if code['cmd'] in [self.IN, self.OUT, self.ADJ]:
                if code['cmd'] == self.IN:
                    i = self.offset + self.p[c+1] if code['m'] == self.MODE_REL else self.p[c+1]
                    if i >= 0:
                        print(f'INPUT: Writing {self.input} to position {i}')
                        self.write(i, self.input)
                else:
                    i = self.get_value(code['m'], self.p[c+1])
                    if code['cmd'] == self.OUT:
                        print(f'OUTPUT: Outputting {i}')
                        self.output.append(i)
                    elif code['cmd'] == self.ADJ:
                        print(f'OFFSET: Adjusting {self.offset} by {i}')
                        self.offset += i
                self.cur += 2
            elif code['cmd'] in [self.JMP_T, self.JMP_F]:
                i1 = self.get_value(code['m1'], self.p[c+1])
                i2 = self.get_value(code['m2'], self.p[c+2])
                if code['cmd'] == self.JMP_T:
                    print(f'Checking jump condition {i1} != 0')
                else:
                    print(f'Checking jump condition {i1} == 0')
                if (code['cmd'] == self.JMP_T and i1 != 0) or (code['cmd'] == self.JMP_F and i1 == 0):
                    print(f'JUMP: Setting cursor to position {i2}')
                    self.cur = i2
                else:
                    self.cur += 3
            elif code['cmd'] in [self.ADD, self.MUL, self.LT, self.EQ]:
                i1 = self.get_value(code['m1'], self.p[c+1])
                i2 = self.get_value(code['m2'], self.p[c+2])
                o = self.offset + self.p[c+3] if code['m3'] == self.MODE_REL else self.p[c+3]
                if o >= 0:
                    i = 0
                    if code['cmd'] == self.ADD:
                        i = i1 + i2
                        print(f'ADD: Writing {i1} + {i2} ({i}) to position {o}')
                    elif code['cmd'] == self.MUL:
                        i = i1 * i2
                        print(f'MUL: Writing {i1} * {i2} ({i}) to position {o}')
                    elif code['cmd'] == self.LT:
                        i = 1 if i1 < i2 else 0
                        print(f'LT: Writing {i1} < {i2} ({i}) to position {o}')
                    elif code['cmd'] == self.EQ:
                        i = 1 if i1 == i2 else 0
                        print(f'EQ: Writing {i1} == {i2} ({i}) to position {o}')
                    self.write(o, i)
                self.cur += 4
            else:
                return 'ERROR'
            loop += 1
            print()

    def parse(self, codes):
        code = str(codes)
        code, cmd = code[:-2], int(code[-2:])
        parsed = {'cmd': cmd}
        if cmd in [self.IN, self.OUT, self.ADJ]:
            parsed.update({'m': 0 if code == '' else int(code[0])})
        else:
            while len(code) < 3:
                code = '0' + code
            parsed.update({'m1': int(code[2]), 'm2': int(code[1]), 'm3': int(code[0])})
        return parsed

    def get_value(self, mode, param):
        if mode == self.MODE_IMM:
            print(f'MODE_IMM: Returning {param}')
            return param
        if mode == self.MODE_POS:
            val = self.read(param)
            print(f'MODE_POS: Returning value at position {param} ({val})')
            return val
        if mode == self.MODE_REL:
            val = self.read(self.offset + param)
            print(f'MODE_REL: Returning value at position {self.offset + param} ({val})')
            return val

    def read(self, pos):
        if pos >= len(self.p):
            self.p.extend([0 for x in range(pos - len(self.p) + 1)])
        return self.p[pos]

    def write(self, pos, val):
        if pos >= len(self.p):
            self.p.extend([0 for x in range(pos - len(self.p) + 1)])
        self.p[pos] = val


def part_1(data):
    intcode = Intcode()
    return intcode.run(data, 1)


def part_2(data):
    intcode = Intcode()
    return intcode.run(data, 2)


example = [int(x) for x in '104,1125899906842624,99'.split(',')]
with open('input.txt') as f:
    data = [int(x) for x in f.readline().split(',')]

print(part_2(data))