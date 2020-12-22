# don't judge, it's a process

def resolve_rules(rules):
    words = dict()
    while len(words) < len(rules):
        # print()
        # print(f'Words: {words}')
        # print(f'Rules: {rules}')
        for rule in rules:
            # print()
            # print(f'Resolving rule {rule} ({rules[rule]})')
            if rule in words:
                # print('Already resolved')
                continue
            if all([type(word) is str for word in rules[rule]]):
                # print('Already a string, adding to words')
                words[rule] = rules[rule]
                continue
            for word in rules[rule]:
                # print(f'Resolving subrule {word}')
                if type(word) is list and all([type(var) is str for var in word]):
                    # print('All variables resolved, making string')
                    string = ''.join(word)
                    if string not in rules[rule]:
                        rules[rule].append(''.join(word))
                    rules[rule].remove(word)
                    continue
                else:
                    for i, w in enumerate(word):
                        if type(w) is int and w in words:
                            # print(f'Resolving variable {w}')
                            if len(words[w]) == 1:
                                # print('Directly resolved with one possibility')
                                word[i] = words[w][0]
                            else:
                                # print('Resolving possibilities')
                                # print(f'To remove: {word}')
                                # print(f'Current rule: {rules[rule]}')
                                for c in words[w]:
                                    tmp = word[:]
                                    tmp[i] = c
                                    # print(f'One possibility: {tmp}')
                                    rules[rule].append(tmp)
                                # print(f'To remove: {word}')
                                # print(f'Current rule: {rules[rule]}')
                                if word in rules[rule]:
                                    rules[rule].remove(word)
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


with open('input.txt') as f:
    data = f.read().splitlines()
    delim = data.index('')
    rules = parse_rules(data[:delim])
    messages = data[delim+1:]

print(part_1(rules, messages))
