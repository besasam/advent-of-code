def clean(stream):
    buffer = ''
    garbage = False
    escape = False
    for c in stream:
        if not garbage:
            if c == '{' or c == '}':
                buffer += c
            elif c == '<':
                garbage = True
        elif not escape:
            if c == '!':
                escape = True
            elif c == '>':
                garbage = False
        else:
            escape = False
    return buffer


def get_score(stream):
    score = 0
    open = 0
    for s in stream:
        if s == '{':
            open += 1
            score += open
        if s == '}':
            open -= 1
    return score


def extract_garbage(stream):
    count = 0
    garbage = False
    escape = False
    for c in stream:
        if garbage:
            if not escape:
                if c == '!':
                    escape = True
                elif c == '>':
                    garbage = False
                else:
                    count += 1
            else:
                escape = False
        elif c == '<':
            garbage = True
    return count


test_streams = [clean(s) for s in ['{}', '{{{}}}', '{{},{}}', '{{{},{},{{}}}}', '{<a>,<a>,<a>,<a>}', '{{<ab>},{<ab>},{<ab>},{<ab>}}', '{{<!!>},{<!!>},{<!!>},{<!!>}}', '{{<a!>},{<a!>},{<a!>},{<ab>}}']]
with open('input.txt') as f:
    data = f.readline()

print(extract_garbage(data))