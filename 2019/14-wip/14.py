class Nanofactory:
    def __init__(self, reactions: dict, ore: int = 1000000000000):
        self.reactions = reactions
        self.store = {r: 0 for r in self.reactions}
        self.store['ORE'] = ore
        self.ore_start = ore

    def make(self, chemical: str):
        recipe, quantity = self.reactions[chemical]['ingredients'], self.reactions[chemical]['quantity']
        for ingredient in recipe:
            q = recipe[ingredient]
            if ingredient == 'ORE':
                if self.store['ORE'] < q:
                    return False
                self.store['ORE'] -= q
            else:
                while self.store[ingredient] < q:
                    self.make(ingredient)
                self.store[ingredient] -= q
        self.store[chemical] += quantity
        return True


def parse(line):
    parts = line.split(' => ')
    inputs = [i.split() for i in parts[0].split(', ')]
    output_quantity, output_type = parts[1].split()
    return {output_type: {'quantity': int(output_quantity), 'ingredients': {i[1]: int(i[0]) for i in inputs}}}


def part_1(recipes):
    factory = Nanofactory(recipes)
    factory.make('FUEL')
    return factory.ore_start - factory.store['ORE']


def part_2(recipes):
    factory = Nanofactory(recipes, 1000000000000)
    while factory.make('FUEL'):
        pass
    return factory.store


with open('example3.txt') as f:
    data = dict()
    for line in f.read().splitlines():
        data.update(parse(line))

print(part_1(data))
