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


def part_1(rules, messages):
    rule_0 = resolve_rules(rules)[0]
    return sum([m in rule_0 for m in messages])


with open('input2.txt') as f:
    data = f.read().splitlines()
    delim = data.index('')
    rules = parse_rules(data[:delim])
    messages = data[delim+1:]

print(part_1(rules, messages))
