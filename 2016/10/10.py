class BotFactory:
    def __init__(self, instructions: list[dict]):
        self.bots = {}
        self.instructions = {}
        self.output = {}
        for i in instructions:
            if 'value' in i.keys():
                self.give_to_bot(i['bot'], i['value'])
            else:
                self.instructions[i['bot']] = i['ins']

    def give_to_bot(self, id: int, value: int):
        if id not in self.bots:
            self.bots[id] = []
        self.bots[id].append(value)

    def step(self):
        state = {bot: self.bots[bot][:] for bot in self.bots.keys()}
        for bot in state:
            if len(state[bot]) < 2:
                continue
            low, high = min(state[bot]), max(state[bot])
            ins = self.instructions[bot]
            low_target, high_target = ins['low'], ins['high']
            if low_target[0] == 'bot':
                self.give_to_bot(low_target[1], low)
            else:
                self.output[low_target[1]] = low
            if high_target[0] == 'bot':
                self.give_to_bot(high_target[1], high)
            else:
                self.output[high_target[1]] = high
            self.bots[bot] = []

    def search(self, val1: int, val2: int):
        while True:
            for bot in self.bots:
                if val1 in self.bots[bot] and val2 in self.bots[bot]:
                    return bot
            self.step()

    def get_output(self, id: int):
        if id not in self.output.keys():
            return None
        return self.output[id]


def parse_instruction(instruction: str):
    ins = instruction.split(' ')
    if ins[0] == 'value':
        return {'value': int(ins[1]), 'bot': int(ins[-1])}
    bot, low_target, low, high_target, high = int(ins[1]), ins[5], int(ins[6]), ins[-2], int(ins[-1])
    return {'bot': bot, 'ins': {'low': (low_target, low), 'high': (high_target, high)}}


def part_1(data):
    bf = BotFactory(data)
    return bf.search(61, 17)


def part_2(data):
    bf = BotFactory(data)
    while True:
        o1, o2, o3 = bf.get_output(0), bf.get_output(1), bf.get_output(2)
        if o1 is None or o2 is None or o3 is None:
            bf.step()
        else:
            return o1*o2*o3


with open('input.txt') as f:
    data = [parse_instruction(line) for line in f.read().splitlines()]

print(part_2(data))
