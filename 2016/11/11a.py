import constraint as csp

DEBUG = True


# God bless StackOverflow
def powerset(s):
    def ps(s):
        x = len(s)
        masks = [1 << i for i in range(x)]
        for i in range(1 << x):
            yield [ss for mask, ss in zip(masks, s) if i & mask]
    return list(ps(s))


class RTF():
    def __init__(self, elems, floors):
        self.c = elems
        self.g = [-c for c in self.c]
        self.vars = self.c + self.g
        self.states = powerset(self.vars)
        self.domain = list(range(floors))
        self.conflicts = [s for s in self.states if self.conflict(s)]
        self.csp = self.init_csp()
        self.sol = self.csp.getSolutions()

        if DEBUG:
            print(self.domain)
            print(self.vars)
            print(len(self.sol))

    def conflict(self, state):
        vars = len(state)
        if vars < 2 or vars == len(self.vars):
            return False
        pos = [v for v in state if v > 0]
        if len(pos) == vars:
            return False
        for v in pos:
            if -v not in state:
                return True
        return False

    def init_csp(self):
        p = csp.Problem()
        p.addVariables(self.vars, self.domain)

        for s in self.states:
            p.addConstraint(lambda *vars: not self.conflict(vars), s)
        return p


test = RTF([1, 2], 4)





def conflict(vars, total_vars):
    if len(vars) < 2:
        return False
    pos = [v for v in vars if v > 0]
    neg = [v for v in vars if v < 0]


exit()

elements = [H, Li] = [i+1 for i in range(2)]
domain = list(range(4))
#ps = powerset(vars)
#print(ps)

p = csp.Problem()
p.addVariables(vars, domain)
#for i in elems:
#    p.addConstraint(lambda c, g: )
solutions = p.getSolutions()
print(len(solutions))
# for s in solutions:
#     print(s)

data = {
    0: {'gen': [], 'chip': [H, Li]},
    1: {'gen': [H], 'chip': []},
    2: {'gen': [Li], 'chip': []},
    3: {'gen': [], 'chip': []}
}
