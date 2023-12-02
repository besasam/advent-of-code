numbers = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}


def calibration_value(s):
    digits = [c for c in s if c.isdigit()]
    return int(digits[0] + digits[-1])


def get_first_digit(s):
    if s[0].isdigit():
        return s[0]
    for num in numbers.keys():
        if s.startswith(num):
            return numbers[num]
    return get_first_digit(s[1:])


def get_last_digit(s):
    if s[-1].isdigit():
        return s[-1]
    for num in numbers.keys():
        if s.endswith(num):
            return numbers[num]
    return get_last_digit(s[:-1])


def part_1(data):
    return sum(calibration_value(l) for l in data)


def part_2(data):
    return sum(int(get_first_digit(l) + get_last_digit(l)) for l in data)


with open('input.txt') as f:
    data = f.read().splitlines()

print(part_2(data))
