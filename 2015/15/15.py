from dataclasses import dataclass
import itertools


@dataclass
class Ingredient:
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int


def cookie_score(ingredients: dict, recipe: dict):
    capacity = x if (x := sum(recipe[i] * ingredients[i].capacity for i in ingredients)) > 0 else 0
    durability = x if (x := sum(recipe[i] * ingredients[i].durability for i in ingredients)) > 0 else 0
    flavor = x if (x := sum(recipe[i] * ingredients[i].flavor for i in ingredients)) > 0 else 0
    texture = x if (x := sum(recipe[i] * ingredients[i].texture for i in ingredients)) > 0 else 0
    return capacity * durability * flavor * texture


def cookie_cals(ingredients: dict, recipe: dict):
    return sum(recipe[i] * ingredients[i].calories for i in ingredients)


def part_1(ingredients: dict):
    max_score = 0
    ingredient_order = list(itertools.permutations(ingredients.keys()))
    for recipe_q in itertools.combinations([i for i in range(101)], len(ingredients)):
        if sum(recipe_q) > 100:
            continue
        for recipe_i in ingredient_order:
            recipe = {recipe_i[i]: recipe_q[i] for i in range(len(ingredients))}
            score = cookie_score(ingredients, recipe)
            if score > max_score:
                max_score = score
    return max_score


def part_2(ingredients: dict):
    max_score = 0
    ingredient_order = list(itertools.permutations(ingredients.keys()))
    for recipe_q in itertools.combinations([i for i in range(101)], len(ingredients)):
        if sum(recipe_q) != 100:
            continue
        for recipe_i in ingredient_order:
            recipe = {recipe_i[i]: recipe_q[i] for i in range(len(ingredients))}
            if cookie_cals(ingredients, recipe) != 500:
                continue
            if (score := cookie_score(ingredients, recipe)) > max_score:
                max_score = score
    return max_score


with open('input.txt') as f:
    ingredients = {s[0][:-1]: Ingredient(int(s[2][:-1]), int(s[4][:-1]), int(s[6][:-1]), int(s[8][:-1]), int(s[10])) for s in [line.split() for line in list(sorted(f.read().splitlines()))]}

print(part_2(ingredients))
