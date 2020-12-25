def resolve_rules(rules_dict):
    words = dict()
    rules = dict()
    for rule in rules_dict:
        rules[rule] = set(tuple(r) if type(r[0]) is not str else str(r[0]) for r in rules_dict[rule])
    while rules:
        for rule in list(rules.keys()):
            if all(type(r) is str for r in rules[rule]):
                words[rule] = rules[rule]
                rules.pop(rule)
                continue
            rule_copy = rules[rule].copy()
            for subrule in rule_copy:
                if type(subrule) is tuple:
                    replaced = False
                    if all(type(r) is str for r in subrule):
                        rules[rule].add(joined := ''.join(subrule))
                        rules[rule].remove(subrule)
                        continue
                    for i, var in enumerate(subrule):
                        if var in words:
                            replaced = True
                            for res in words[var]:
                                tmp = tuple(s if k != i else res for k, s in enumerate(subrule))
                                rules[rule].add(tmp)
                    if replaced:
                        rules[rule].remove(subrule)
    return words


def parse_rule(rule_string):
    rule_split = rule_string.split(': ')
    rule = int(rule_split[0])
    content_split = rule_split[1].split(' | ')
    content = []
    for c in content_split:
        if c[0] == '"':
            content.append(c[1:-1])
        else:
            content.append([int(x) for x in c.split(' ')])
    return {rule: content}


def parse_rules(rule_strings):
    rules = dict()
    for r in rule_strings:
        rules.update(parse_rule(r))
    return rules


def validate(message: str, rules, c42: int = 0, c31: int = 0):
    if message == '':
        return c42 > c31 > 0
    if c31 > 0 or not any([message.startswith(r42) for r42 in rules[42]]):
        if c42 == 0:
            return False
        for r31 in rules[31]:
            if message.startswith(r31):
                nex = message.removeprefix(r31)
                if validate(nex, rules, c42, c31+1):
                    return True
    if c31 == 0:
        for r42 in rules[42]:
            if message.startswith(r42):
                nex = message.removeprefix(r42)
                if validate(nex, rules, c42+1, c31):
                    return True
    return False


def part_1(rules, messages):
    rule_0 = resolve_rules(rules)[0]
    return sum([m in rule_0 for m in messages])


def part_2(rules, messages):
    resolved_rules = resolve_rules(rules)
    return sum([validate(m, resolved_rules) for m in messages])


with open('input.txt') as f:
    data = f.read().splitlines()
    delim = data.index('')
    rules = parse_rules(data[:delim])
    messages = data[delim+1:]

print(part_2(rules, messages))
