class Intcode:
    STOP = 99
    ADD = 1
    MUL = 2

    p = None
    cur = 0

    def run(self, program):
        self.p = program
        self.cur = 0
        while True:
            c = self.cur
            cmd = self.p[c]
            if cmd == self.STOP:
                return self.p[0]
            [i1, i2, o] = self.p[c+1:c+4]
            if cmd == self.ADD:
                self.p[o] = self.p[i1] + self.p[i2]
            else:
                self.p[o] = self.p[i1] * self.p[i2]
            self.cur += 4


def part_1(data):
    [data[1], data[2]] = [12, 2]
    intcode = Intcode()
    return intcode.run(data)


def part_2(data):
    search = 19690720
    intcode = Intcode()
    for n in range(100):
        for v in range(100):
            program = data[:]
            [program[1], program[2]] = [n, v]
            if intcode.run(program) == search:
                return 100 * n + v
    return None


example = [int(x) for x in '1,9,10,3,2,3,11,0,99,30,40,50'.split(',')]
with open('input.txt') as f:
    data = [int(x) for x in f.readline().split(',')]

print(part_2(data))