from dataclasses import dataclass
from itertools import combinations


@dataclass
class Item:
    name: str
    category: str
    cost: int = 0
    dmg: int = 0
    armor: int = 0


@dataclass
class Character:
    hp: int = 100
    dmg: int = 0
    armor: int = 0


def fight(player: Character, boss: Character):
    player_dmg = player.dmg - boss.armor
    if player_dmg < 1:
        player_dmg = 1
    boss_dmg = boss.dmg - player.armor
    if boss_dmg < 1:
        boss_dmg = 1
    while True:
        boss.hp -= player_dmg
        if boss.hp <= 0:
            return True
        player.hp -= boss_dmg
        if player.hp <= 0:
            return False


def get_item_combinations(items: dict):
    for weapon in items['Weapons']:
        yield [weapon]
        for armor in items['Armor']:
            yield [weapon, armor]
            for ring in items['Rings']:
                yield [weapon, armor, ring]
            for rings in combinations(items['Rings'], 2):
                yield [weapon, armor] + list(rings)
        for ring in items['Rings']:
            yield [weapon, ring]
        for rings in combinations(items['Rings'], 2):
            yield [weapon] + list(rings)


def make_player_character(equipment: list):
    dmg = sum(item.dmg for item in equipment)
    armor = sum(item.armor for item in equipment)
    return Character(100, dmg, armor)


def part_1(items: dict, boss: Character):
    wins = []
    boss_hp = boss.hp
    for combo in get_item_combinations(items):
        player = make_player_character(combo)
        if fight(player, boss):
            wins.append(sum(item.cost for item in combo))
        boss.hp = boss_hp
    return min(wins)


def part_2(items: dict, boss: Character):
    losses = []
    boss_hp = boss.hp
    for combo in get_item_combinations(items):
        player = make_player_character(combo)
        if not fight(player, boss):
            losses.append(sum(item.cost for item in combo))
        boss.hp = boss_hp
    return max(losses)


with open('shop.txt') as f:
    shopitems = [[entry.split() for entry in line] for line in [section.split('\n') for section in f.read().split('\n\n')]]
    shop = dict()
    for category in shopitems:
        cat = category[0][0][:-1]
        shop[cat] = []
        for item in category[1:]:
            shop[cat].append(Item(item[0], cat, int(item[1]), int(item[2]), int(item[3])))

with open('input.txt') as f:
    bossstats = [int(line.split()[-1]) for line in f.read().splitlines()]
    boss = Character(*bossstats)

print(part_2(shop, boss))
