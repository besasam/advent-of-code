def parse(expression):
    exp = list(expression.replace(' ', ''))
    parsed_exp = []
    sub_exp = ''
    count = 0
    while exp:
        c = exp[0]
        if count > 0:
            if c == ')' and count == 1:
                parsed_exp.append(parse(sub_exp))
                sub_exp = ''
                count = 0
            else:
                sub_exp += c
                if c == '(':
                    count += 1
                elif c == ')':
                    count -= 1
        elif c == '(':
            count += 1
        else:
            parsed_exp.append(c)
        exp.pop(0)
    return parsed_exp


def parse_parentheses(expression):
    expression_in_parentheses = ''
    count = 0
    for c in expression:
        if c == ')' and count == 0:
            return expression_in_parentheses
        if c == '(':
            count += 1
        elif c == ')':
            count -= 1
        expression += c


# def parenthesize(expression):
#     exp = list(expression.replace(' ', ''))
#     res = ''
#     l = len(exp)
#     op = '*'
#     parentheses = 0
#     i = 0
#     while i < l - 1:
#         if exp[i] in ['(', ')']:
#             res += exp[i]
#             op = '*'
#             i += 1
#             continue
#         if exp[i+1] == '+' and op == '*':
#             res += '('
#             parentheses += 1
#             op = '+'
#         elif exp[i] == '*' and op == '+':
#             res += ')'
#             parentheses -= 1
#             op = '*'
#         res += exp[i]
#         i += 1
#     res += exp[-1]
#     if parentheses > 0:
#         res += ''.join([')' for _ in range(parentheses)])
#     return res


def parenthesize(expression):
    print()
    print(expression.replace(' ', ''))
    exp = list(expression.replace(' ', ''))
    l = len(exp)
    res = ''
    sub = ''
    parentheses = 0
    op = '*'
    i = 0
    while i < l - 1:
        print(f'Character: {exp[i]} - Expression: {res} - Subexpression: {sub} - Parentheses: {parentheses}')
        if parentheses > 0:
            if exp[i] == '(':
                parentheses += 1
                sub += '('
            elif exp[i] == ')':
                if parentheses == 1:
                    print()
                    print(f'Subexpression: {sub}')
                    res += parenthesize(sub) + ')'
                    sub = ''
                    op = '*'
                    parentheses = 0
                else:
                    parentheses -= 1
                    sub += ')'
            else:
                sub += exp[i]
        elif exp[i] == '(':
            parentheses += 1
            res += '('
        else:
            if exp[i+1] == '+':
                if op == '*':
                    res += '('
                op = '+'
            elif exp[i+1] == '*':
                res += exp[i]
                if op == '+':
                    res += ')'
                op = '*'
                i += 1
                continue
            res += exp[i]
        print(f'Character: {exp[i]} - Expression: {res} - Subexpression: {sub} - Parentheses: {parentheses}')
        i += 1
    if exp[-1] == ')':
        res += parenthesize(sub)
    res += exp[-1]
    print(f'RESULT: {res}')
    print()
    return res


def evaluate(expression):
    res = 0
    op = '+'
    for c in expression:
        if type(c) == str:
            if c in ['+', '*']:
                op = c
            else:
                if op == '+':
                    res += int(c)
                elif op == '*':
                    res *= int(c)
        else:
            if op == '+':
                res += evaluate(c)
            elif op == '*':
                res *= evaluate(c)
    return res


def part_1(data):
    return sum([evaluate(parse(d)) for d in data])


def part_2(data):
    return sum([evaluate(parse(parenthesize(d))) for d in data])


with open('example.txt') as f:
    data = f.read().splitlines()

#print(part_2(data))

# for d in data:
#     print(d.replace(' ', ''))
#     print(parenthesize(d))
#     print()

print(parenthesize(data[3]))

#print(evaluate(parse(parenthesize(data[3]))))