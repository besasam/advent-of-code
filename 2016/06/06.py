import itertools
import operator


def find_most_common_character(string):
    most_common = ''
    count = 0
    for c in string:
        c_count = string.count(c)
        if c_count > count:
            most_common = c
            count = c_count
    return most_common


def find_least_common_character(string):
    least_common = ''
    count = len(string) + 1
    for c in string:
        c_count = string.count(c)
        if c_count < count:
            least_common = c
            count = c_count
    return least_common


def prepare_message(message):
    prepared_message = []
    for i in range(len(message[0])):
        column = []
        for m in message:
            column.append(m[i])
        prepared_message.append(''.join(column))
    return prepared_message


def correct_message(corrupted_message):
    message = []
    for m in prepare_message(corrupted_message):
        message.append(find_most_common_character(m))
    return ''.join(message)


def modified_correct_message(corrupted_message):
    message = []
    for m in prepare_message(corrupted_message):
        message.append(find_least_common_character(m))
    return ''.join(message)


def part_1(message):
    return correct_message(message)


def part_2(message):
    return modified_correct_message(message)


with open('input.txt') as f:
    data = f.read().splitlines()

print(part_2(data))