import re


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


# def parse_parentheses(expression):
#     expression_in_parentheses = ''
#     count = 0
#     for c in expression:
#         if c == ')' and count == 0:
#             return expression_in_parentheses
#         if c == '(':
#             count += 1
#         elif c == ')':
#             count -= 1
#         expression += c
#
#
# def parenthesize(expression):
#     print()
#     print(expression.replace(' ', ''))
#     exp = list(expression.replace(' ', ''))
#     l = len(exp)
#     res = ''
#     sub = ''
#     parentheses = 0
#     op = '*'
#     i = 0
#     while i < l - 1:
#         print(f'Character: {exp[i]} - Expression: {res} - Subexpression: {sub} - Parentheses: {parentheses}')
#         if parentheses > 0:
#             if exp[i] == '(':
#                 parentheses += 1
#                 sub += '('
#             elif exp[i] == ')':
#                 if parentheses == 1:
#                     print()
#                     print(f'Subexpression: {sub}')
#                     res += parenthesize(sub) + ')'
#                     sub = ''
#                     op = '*'
#                     parentheses = 0
#                 else:
#                     parentheses -= 1
#                     sub += ')'
#             else:
#                 sub += exp[i]
#         elif exp[i] == '(':
#             parentheses += 1
#             res += '('
#         else:
#             if exp[i+1] == '+':
#                 if op == '*':
#                     res += '('
#                 op = '+'
#             elif exp[i+1] == '*':
#                 res += exp[i]
#                 if op == '+':
#                     res += ')'
#                 op = '*'
#                 i += 1
#                 continue
#             res += exp[i]
#         print(f'Character: {exp[i]} - Expression: {res} - Subexpression: {sub} - Parentheses: {parentheses}')
#         i += 1
#     if exp[-1] == ')':
#         res += parenthesize(sub)
#     res += exp[-1]
#     print(f'RESULT: {res}')
#     print()
#     return res


def parenthesize(expression):
    split_exp = split_expression(expression)
    e = expression.replace(' ', '')
    # print(f'Input: {e}')
    exp = ''
    addition = False
    while split_exp:
        c = split_exp.pop(0)
        if len(c) == 1:
            if c == '+' or c == '*':
                exp += c
            else:
                if not addition and '+' in split_exp and (
                        '*' not in split_exp or ('*' in split_exp and split_exp.index('+') < split_exp.index('*'))):
                    exp += '('
                    addition = True
                exp += c
                if addition and ('+' not in split_exp or (
                        '+' in split_exp and '*' in split_exp and split_exp.index('*') < split_exp.index('+'))):
                    exp += ')'
                    addition = False
        else:
            if not addition and '+' in split_exp and (
                    '*' not in split_exp or ('*' in split_exp and split_exp.index('+') < split_exp.index('*'))):
                exp += '('
                addition = True
            exp += '(' + parenthesize(c) + ')'
            if addition and ('+' not in split_exp or (
                    '+' in split_exp and '*' in split_exp and split_exp.index('*') < split_exp.index('+'))):
                exp += ')'
                addition = False
        # if parentheses > 0:
        #     if c == ')':
        #         if parentheses == 1:
        #             exp += '(' + parenthesize(subexp) + ')'
        #             subexp = ''
        #             parentheses = 0
        #             continue
        #         else:
        #             parentheses -= 1
        #     if c == '(':
        #         parentheses += 1
        #     subexp += c
        # if c == '(':
        #     parentheses += 1
        # elif c == '+' or c == '*':
        #     exp += c
        # elif c.isdigit():
        #     if not addition and '+' in expression and ('*' not in expression or ('*' in expression and expression.index('+') < expression.index('*'))):
        #         exp += '('
        #         addition = True
        #     exp += c
        #     if addition and ('+' not in expression or ('+' in expression and '*' in expression and expression.index('*') < expression.index('+'))):
        #         exp += ')'
        #         addition = False
    if addition:
        exp += ')'
    # print(f'Result: {exp}')
    return exp


def split_expression(expression):
    expression = list(expression.replace(' ', ''))
    res = []
    sub = ''
    parentheses = 0
    for c in expression:
        if parentheses > 0:
            if c == ')':
                if parentheses == 1:
                    res.append(sub)
                    sub = ''
                    parentheses = 0
                    continue
                else:
                    parentheses -= 1
            elif c == '(':
                parentheses += 1
            sub += c
        elif c == '(':
            parentheses += 1
        else:
            res.append(c)
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


with open('input.txt') as f:
    data = f.read().splitlines()

print(part_2(data))
