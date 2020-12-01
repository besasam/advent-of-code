def part_1(string):
    captcha = [int(x) for x in string]
    sum = 0
    for i in range(len(captcha) - 1):
        if captcha[i] == captcha[i+1]:
            sum += captcha[i]
    if captcha[-1] == captcha[0]:
        sum += captcha[-1]
    return sum


def part_2(string):
    captcha = [int(x) for x in string]
    sum = 0
    length = len(captcha)
    step = int(length / 2)
    for i in range(length):
        nex = (i + step) % length
        if captcha[i] == captcha[nex]:
            sum += captcha[i]
    return sum


tests = ['1122', '1111', '1234', '91212129']
with open('input.txt') as f:
    data = f.readline()
print(part_2(data))