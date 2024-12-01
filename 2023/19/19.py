class Rule:
    def __init__(self, rule: str):
        self.key, self.condition, self.value = rule[0], rule[1], int(rule[2:])

    def eval(self, part: dict):
        if self.condition == '<':
            return part[self.key] < self.value
        else:
            return part[self.key] > self.value


class DEA:  # Deterministic Elfin Automaton
    def __init__(self, workflows: list):
        self.workflows = dict()
        for workflow in workflows:
            label, rules = workflow.split('{')
            self.workflows[label] = [r.split(':') for r in rules[:-1].split(',')]

    def process(self, part: dict):
        cur = 'in'
        while True:
            if cur == 'A':
                return True
            if cur == 'R':
                return False
            rules = self.workflows[cur]
            for rule in rules:
                if len(rule) == 1:
                    cur = rule[0]
                    break
                if self.eval(rule[0], part):
                    cur = rule[1]
                    break

    def eval(self, rule: str, part: dict):
        key, condition, value = rule[0], rule[1], int(rule[2:])
        if condition == '<':
            return part[key] < value
        else:
            return part[key] > value

    def reduce(self):
        final = dict()
        keys = [k for k in self.workflows]
        while True:
            if len(final) == len(self.workflows):
                return final
            for key in keys[:]:
                workflow = self.workflows[key]
                targets = [rule[-1] for rule in workflow]
                if len(set(targets)) == 1 and ('A' in targets or 'R' in targets):
                    final[key] = [targets.pop()]
                    keys.remove(key)


def part_1(data):
    parts = []
    for line in data[1]:
        parts.append({p[0]: int(p[1]) for p in [l.split('=') for l in line[1:-1].split(',')]})
    dea = DEA(data[0])
    res = 0
    for part in parts:
        if dea.process(part):
            res += sum(part.values())
    for w in dea.workflows.values():
        print(w)
    return res


with open('test.txt') as f:
    data = [part.splitlines() for part in f.read().split('\n\n')]

print(part_1(data))
