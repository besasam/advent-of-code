import re


class Bags:
    def __init__(self, data):
        self.bags = dict()
        for d in data:
            self.bags.update({d[0]: None})
            if len(d) > 1:
                self.bags[d[0]] = dict()
                for c in d[1]:
                    self.bags[d[0]].update({c[1]: c[0]})

    def find(self, color):
        found = set()
        for b in self.bags:
            if self.bags[b] is not None and color in self.bags[b]:
                found.add(b)
        next = found.copy()
        for n in next:
            found.update(self.find(n))
        return found

    def count(self, color):
        if self.bags[color] is None:
            return 0
        c = 0
        for b in self.bags[color]:
            c += self.bags[color][b] * (self.count(b) + 1)
        return c

    def __str__(self):
        string = ''
        for b in self.bags:
            string += f'{b}: {self.bags[b]}\n'
        return string


def part_1(data):
    bags = Bags(data)
    return len(bags.find('shiny gold'))


def part_2(data):
    bags = Bags(data)
    return bags.count('shiny gold')


with open('input.txt') as f:
    data = [[r[0], [[k if not k.isdigit() else int(k) for k in i.split(maxsplit=1)] for i in r[1:]]] if r[1][0].isdigit() else [r[0]] for r in [re.split(' bags contain | bags, | bag, | bags.| bag.', t)[:-1] for t in f.read().splitlines()]]

print(part_2(data))