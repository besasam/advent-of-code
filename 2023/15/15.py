class Boxes:
    def __init__(self):
        self.boxes = {i: dict() for i in range(256)}

    def step(self, step):
        if step[-1] == '-':
            self.step_remove(step)
        else:
            self.step_add(step)

    def step_remove(self, step):
        label = step[:-1]
        box = get_hash(label)
        self.boxes[box].pop(label, None)

    def step_add(self, step):
        label, f_len = step.split('=')
        box = get_hash(label)
        self.boxes[box][label] = int(f_len)

    def get_focusing_power(self):
        res = 0
        for box in self.boxes:
            i = 1
            for f_len in self.boxes[box].values():
                res += (box+1) * i * f_len
                i += 1
        return res


def get_hash(string):
    val = 0
    for c in string:
        val = ((val + ord(c)) * 17) % 256
    return val


def part_1(data):
    return sum(get_hash(s) for s in data)


def part_2(data):
    boxes = Boxes()
    for s in data:
        boxes.step(s)
    return boxes.get_focusing_power()


with open('input.txt') as f:
    data = f.readline().split(',')

print(part_2(data))
