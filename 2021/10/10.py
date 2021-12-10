brackets = {'(': ')', '[': ']', '{': '}', '<': '>'}
rbrackets = {')': '(', ']': '[', '}': '{', '>': '<'}
error_scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
completion_scores = {')': 1, ']': 2, '}': 3, '>': 4}


def get_syntax_error_score(line: str):
    buffer = []
    for c in line:
        if c in rbrackets.values():
            buffer.append(c)
        elif buffer[-1] == rbrackets[c]:
            buffer.pop()
        else:
            return error_scores[c]
    return 0


def get_closing_sequence(line: str):
    buffer = []
    for c in line:
        if c in rbrackets.values():
            buffer.append(c)
        elif buffer[-1] == rbrackets[c]:
            buffer.pop()
    return ''.join(brackets[c] for c in reversed(buffer))


def get_completion_score(line: str):
    closing_sequence = get_closing_sequence(line)
    score = 0
    for c in closing_sequence:
        score = score*5 + completion_scores[c]
    return score


def part_1(lines):
    return sum(get_syntax_error_score(line) for line in lines)


def part_2(lines):
    scores = [get_completion_score(line) for line in lines if not get_syntax_error_score(line)]
    return list(sorted(scores))[len(scores)//2]


with open('input.txt') as f:
    data = f.read().splitlines()

print(part_2(data))
