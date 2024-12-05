def is_correct_order(rules: dict, update: list) -> bool:
    for i, page in enumerate(update):
        if page in rules and not all(p in update[:i] for p in rules[page] if p in update):
            return False
    return True


def fix_order(all_rules: dict, update: list) -> list:
    rules = {page: set(needs for needs in all_rules[page] if needs in update) for page in all_rules if page in update}
    for page in update:
        if page not in rules:
            rules[page] = set()
    order = {len(rules[page]): page for page in rules}
    return [order[i] for i in range(len(update))]


def part_1(rules: dict, updates: list) -> int:
    return sum(update[len(update)//2] for update in updates if is_correct_order(rules, update))


def part_2(rules: dict, updates: list) -> int:
    return sum(fix_order(rules, update)[len(update)//2] for update in updates if not is_correct_order(rules, update))


with open('input.txt') as f:
    data = [part.splitlines() for part in f.read().split('\n\n')]

rules = dict()
for rule in data[0]:
    [needs, num] = [int(x) for x in rule.split('|')]
    if num not in rules:
        rules[num] = set()
    rules[num].add(needs)

updates = [[int(x) for x in line.split(',')] for line in data[1]]

print(part_2(rules, updates))
