import re


def contains_three_vowels(string: str):
    return len(re.findall('[aeiou]', string)) >= 3


def contains_double_letter(string: str):
    prev = ''
    for c in string:
        if c == prev:
            return True
        prev = c
    return False


def contains_forbidden_strings(string: str):
    return len(re.findall('ab|cd|pq|xy', string)) != 0


def contains_two_pairs(string: str):
    while string:
        pair, rest = string[:2], string[2:]
        if pair in rest:
            return True
        string = string[1:]
    return False


def contains_double_letter_with_between(string: str):
    for i in range(len(string)-2):
        if string[i] == string[i+2] and string[i+1] != string[i]:
            return True
    return False


def part_1(data):
    return sum(contains_three_vowels(s) and contains_double_letter(s) and not contains_forbidden_strings(s) for s in data)


def part_2(data):
    return sum(contains_two_pairs(s) and contains_double_letter_with_between(s) for s in data)


with open('input.txt') as f:
    data = f.read().splitlines()

print(part_2(data))
