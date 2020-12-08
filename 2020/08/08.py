class Console:
    def __init__(self, program):
        self.program = program
        self.p = 0
        self.acc = 0

    def find_acc_at_loop(self):
        visited = []
        while True:
            if self.p in visited:
                return self.acc
            visited.append(self.p)
            self.execute()

    def find_visited_positions(self):
        visited = []
        while True:
            if self.p in visited:
                return visited
            visited.append(self.p)
            self.execute()

    def fix_program(self):
        program = [o[:] for o in self.program]
        positions = self.find_visited_positions()
        for p in positions:
            self.program = [o[:] for o in program]
            self.program[p][0] = 'jmp' if self.program[p][0] == 'nop' else 'nop'
            visited = []
            self.p = 0
            self.acc = 0
            while True:
                if self.p in visited:
                    break
                visited.append(self.p)
                e = self.execute()
                if e == -1:
                    return self.acc

    def execute(self):
        op, o = self.program[self.p]
        p = self.p
        if op == 'jmp':
            self.p += o
        else:
            if op == 'acc':
                self.acc += o
            self.p += 1
        if p == len(self.program) - 1:
            return -1
        return 0


def part_1(data):
    con = Console(data)
    return con.find_acc_at_loop()


def part_2(data):
    con = Console(data)
    return con.fix_program()


with open('input.txt') as f:
    data = [[int(c[1:]) if c[0] == '+' else -int(c[1:]) if c[0] == '-' else c for c in l.split()] for l in f.read().splitlines()]

print(part_2(data))