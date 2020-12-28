import re


def string_length(string: str):
    string = string[1:-1]
    string = re.sub(r'\\x[0-9a-f][0-9a-f]', '#', string)
    string = re.sub(r'\\"', '#', string)
    string = re.sub(r'\\\\', '#', string)
    return len(string)


def encoded_length(string: str):
    string = re.sub(r'"', '##', string)
    string = re.sub(r'\\', '##', string)
    return len(string) + 2


def part_1(data):
    return sum(len(s) - string_length(s) for s in data)


def part_2(data):
    return sum(encoded_length(s) - len(s) for s in data)


with open('input.txt') as f:
    data = f.read().splitlines()

print(part_2(data))
