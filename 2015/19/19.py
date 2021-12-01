import re


class Reactor:
    def __init__(self, rules: list):
        self.rules = rules

    def replace(self, molecule: str, rule: tuple):
        molecules = set()
        search, replace = rule
        matches = re.finditer(search, molecule)
        for m in matches:
            start, end = m.span()
            molecules.add(molecule[:start] + replace + molecule[end:])
        return molecules

    def replace_all(self, molecule: str):
        molecules = set()
        for rule in self.rules:
            molecules |= self.replace(molecule, rule)
        return molecules


def part_1(data):
    reactor = Reactor(data['rules'])
    return len(reactor.replace_all(data['molecule']))


def part_2(data):
    molecule = data['molecule']
    elements = len([e for e in molecule if e.isupper()])
    elementsRnAr = molecule.count('Rn') + molecule.count('Ar')
    elementsY = molecule.count('Y')
    return elements - elementsRnAr - 2*elementsY - 1


with open('input.txt') as f:
    lines = f.read().splitlines()
    data = {'rules': [tuple(line.split(' => ')) for line in lines[:-2]], 'molecule': lines[-1]}

print(part_2(data))
