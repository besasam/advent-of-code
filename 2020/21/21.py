class Ingredients:
    def __init__(self, data):
        self.data = data
        self.allergens = dict()
        self.distinct_allergens = []
        self.distinct_ingredients = []
        self.extract_allergens()
        self.reduce_allergens()

    def extract_allergens(self):
        for d in self.data:
            for a in d[1]:
                if a not in self.allergens:
                    self.allergens[a] = d[0]
                else:
                    self.allergens[a] = [x for x in self.allergens[a] if x in d[0]]

    def reduce_allergens(self):
        while len(self.distinct_allergens) != len(self.allergens):
            for a in self.allergens:
                if len(self.allergens[a]) == 1:
                    if a not in self.distinct_allergens:
                        self.distinct_allergens.append(a)
                        self.distinct_ingredients.append(self.allergens[a][0])
                    continue
                for d in self.distinct_ingredients:
                    if d in self.allergens[a]:
                        self.allergens[a].remove(d)

    def get_number_of_safe_ingredients(self):
        c = 0
        for d in self.data:
            for i in d[0]:
                if i not in self.distinct_ingredients:
                    c += 1
        return c

    def get_canonical_ingredient_list(self):
        self.distinct_allergens.sort()
        res = ''
        for a in self.distinct_allergens:
            res += self.allergens[a][0] + ','
        return res[:-1]

    def __str__(self):
        res = ''
        for a in self.allergens:
            res += a + ': ' + str(self.allergens[a]) + '\n'
        return res


def part_1(data):
    ingredients = Ingredients(data)
    return ingredients.get_number_of_safe_ingredients()


def part_2(data):
    ingredients = Ingredients(data)
    return ingredients.get_canonical_ingredient_list()


with open('input.txt') as f:
    data = [[x[0].split(' '), x[1][:-1].split(', ')] for x in [l.split(' (contains ') for l in f.read().splitlines()]]

print(part_2(data))
