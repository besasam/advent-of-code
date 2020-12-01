class Intcode:
    STOP, ADD, MUL, IN, OUT, JMP_T, JMP_F, LT, EQ = [99, 1, 2, 3, 4, 5, 6, 7, 8]
    p = None
    cur = 0
    input = None
    output = None

    def run(self, program, input):
        self.p = program
        self.input = input
        self.cur = 0
        while True:
            c = self.cur
            code = self.parse(self.p[c])
            if code['cmd'] == self.STOP:
                return self.output
            if code['cmd'] in [self.IN, self.OUT]:
                if code['cmd'] == self.IN:
                    i = self.p[c+1]
                    self.p[i] = self.input
                elif code['cmd'] == self.OUT:
                    i = self.get_value(code['m'], self.p[c+1])
                    self.output = i
                self.cur += 2
            elif code['cmd'] in [self.JMP_T, self.JMP_F]:
                i1 = self.get_value(code['m1'], self.p[c+1])
                i2 = self.get_value(code['m2'], self.p[c+2])
                if (code['cmd'] == self.JMP_T and i1 != 0) or (code['cmd'] == self.JMP_F and i1 == 0):
                    self.cur = i2
                else:
                    self.cur += 3
            elif code['cmd'] in [self.ADD, self.MUL, self.LT, self.EQ]:
                i1 = self.get_value(code['m1'], self.p[c+1])
                i2 = self.get_value(code['m2'], self.p[c+2])
                o = self.p[c+3]
                if code['cmd'] == self.ADD:
                    self.p[o] = i1 + i2
                elif code['cmd'] == self.MUL:
                    self.p[o] = i1 * i2
                elif code['cmd'] == self.LT:
                    self.p[o] = 1 if i1 < i2 else 0
                elif code['cmd'] == self.EQ:
                    self.p[o] = 1 if i1 == i2 else 0
                self.cur += 4
            else:
                return 'ERROR'

    def parse(self, codes):
        code = str(codes)
        code, cmd = code[:-2], int(code[-2:])
        parsed = {'cmd': cmd}
        if cmd == self.OUT:
            parsed.update({'m': 0 if code == '' else 1})
        else:
            while len(code) < 2:
                code = '0' + code
            parsed.update({'m1': int(code[1]), 'm2': int(code[0])})
        return parsed

    def get_value(self, mode, param):
        if mode == 0:
            return self.p[param]
        else:
            return param


def part_1(data):
    intcode = Intcode()
    return intcode.run(data, 1)


def part_2(data):
    intcode = Intcode()
    return intcode.run(data, 5)


example = [int(x) for x in '1002,4,3,4,33'.split(',')]
with open('input.txt') as f:
    data = [int(x) for x in f.readline().split(',')]

print(part_2(data))