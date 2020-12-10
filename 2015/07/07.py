class Circuit:
    INPUT = 0
    NOT = 1
    AND = 2
    OR = 3
    LSHIFT = 4
    RSHIFT = 5

    def __init__(self, instructions):
        self.i = [self.parse(i) for i in instructions]
        self.gates = dict()

    def parse(self, instruction):
        gate, i = instruction[1], instruction[0].split()
        p = {'gate': gate, 'op': None, 'params': None}
        if len(i) == 1:
            p['op'] = self.INPUT
            p['params'] = i[0]
        elif len(i) == 2:
            p['op'] = self.NOT
            p['params'] = i[1]
        else:
            op = i[1]
            p['op'] = self.AND if op == 'AND' else self.OR if op == 'OR' else self.LSHIFT if op == 'LSHIFT' else self.RSHIFT
            p['params'] = [i[0], i[2]]
        return p

    def run(self):
        instructions = self.i[:]
        while instructions:
            for i in instructions[:]:
                if i['op'] == self.INPUT and self.get(i['params']) is not None:
                    self.gates.update({i['gate']: self.get(i['params'])})
                    instructions.remove(i)

    def get(self, p):
        if p.isdigit():
            return int(p)
        if p in self.gates:
            return self.gates[p]
        return None


with open('example.txt') as f:
    # data = [[[x if not x.isdigit() else int(x) for x in k[0].split()], k[1]] for k in [l.split(' -> ') for l in f.read().splitlines()]]
    data = [l.split(' -> ') for l in f.read().splitlines()]

circuit = Circuit(data)