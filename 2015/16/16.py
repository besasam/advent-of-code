import re


def part_1(sue: dict, aunts: dict):
    for i in aunts:
        if all(aunts[i][k] == sue[k] for k in aunts[i]):
            return i


def part_2(sue: dict, aunts: dict):
    for i in aunts:
        s = True
        for k in aunts[i]:
            if k == 'cats' or k == 'trees':
                if aunts[i][k] <= sue[k]:
                    s = False
                    break
            elif k == 'pomeranians' or k == 'goldfish':
                if aunts[i][k] >= sue[k]:
                    s = False
                    break
            elif aunts[i][k] != sue[k]:
                s = False
                break
        if s:
            return i



with open('input.txt') as f:
    aunts = {int(s[1]): {s[i]: int(s[i+1]) for i in [2, 4, 6]} for s in [re.split(' |: |, ', line) for line in f.read().splitlines()]}

with open('input2.txt') as f:
    sue = {s[0]: int(s[1]) for s in [line.split(': ') for line in f.read().splitlines()]}

print(part_2(sue, aunts))
