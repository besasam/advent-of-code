class Bot:
    def __init__(self, id):
        self.id = id
        self.chips = []
        self.cmd = {}

    def set_command(self, low, high):
        [self.cmd['low'], self.cmd['high']] = [low, high]

    def give(self, chip):
        self.chips.append(chip)

    def run(self):
        if not self.cmd or len(self.chips) < 2:
            return
        low = {'val': min(self.chips)}
        low.update(self.cmd['low'])
        high = {'val': max(self.chips)}
        high.update(self.cmd['high'])
        self.chips = []
        return {
            'bot': self.id,
            'low': low,
            'high': high
        }

    def __str__(self):
        s = 'Bot ' + str(self.id)
        if len(self.chips) > 0:
            s += ' [' + str(self.chips[0])
            if len(self.chips) > 1:
                s += ', ' + str(self.chips[1])
            s += ']'
        return s


class BotFactory:
    def __init__(self, instructions):
        self.i = [parse_instruction(i) for i in instructions]
        self.bots = {}
        self.output = {}

    def _execute(self, i):
        id = i['bot']
        bot = self._get(i['bot'])
        if 'val' in i:
            val = i['val']
            holds = bot.chips
            bot.give(i['val'])
            print(f'Giving value {val} to bot {id} {holds}')
        elif not bot.cmd:
            lto = i['low']['to']
            hto = i['high']['to']
            ltype = i['low']['type']
            htype = i['high']['type']
            print(f'Setting command for bot {id}')
            bot.set_command({'type': ltype, 'to': lto}, {'type': htype, 'to': hto})
        return bot.run()

    def _process(self, output):
        id = output['bot']
        l = output['low']['val']
        h = output['high']['val']
        print(f'Got values {l} and {h} from bot {id}')
        for o in ['low', 'high']:
            type = output[o]['type']
            to = output[o]['to']
            val = output[o]['val']
            if type == 0:
                print(f'Putting value {val} in output {to}')
                self.output[to] = val
            else:
                e = self._execute({'bot': to, 'val': val})
                if e:
                    self._process(e)

    def _get(self, id):
        if id not in self.bots:
            self.bots[id] = Bot(id)
        return self.bots[id]

    def find_numbers(self, l, h):
        k = 0
        while True:
            e = self._execute(self.i[k])
            if e:
                if e['low']['val'] == l and e['high']['val'] == h:
                    return e['bot']
                self._process(e)
            if k < len(self.i) - 1:
                k += 1
            else:
                k = 0


def parse_instruction(instruction):
    l = instruction.split(' ')
    if instruction[0] == 'v':
        return {'bot': int(l[-1]), 'val': int(l[1])}
    low = {'type': 1 if l[5] == 'bot' else 0, 'to': int(l[6])}
    high = {'type': 1 if l[-2] == 'bot' else 0, 'to': int(l[-1])}
    return {'bot': int(l[1]), 'low': low, 'high': high}


def trace_bot(id, instructions):
    trace = set()
    for i in instructions:
        if 'val' not in i:
            for o in ['low', 'high']:
                if i[o]['type'] == 1:
                    trace.add(i[o]['to'])


def trace_chip(val, instructions):
    holder = None
    trace = []
    for i in instructions:
        id = i['bot']
        if 'val' in i and i['val'] == val:
            holder = id
            trace.append(id)
        else:
            for o in ['low', 'high']:
                if i[o]['type'] == 1:
                    trace.append(i[o]['to'])
    return


def trace_chips(vals, instructions):
    [val1_holders, val1_candidates] = trace_chip(vals[0], instructions)
    [val2_holders, val2_candidates] = trace_chip(vals[1], instructions)
    return [val1_holders, val1_candidates, val2_holders, val2_candidates]


def part_1(data, low, high):
    b = BotFactory(data)
    return b.find_numbers(low, high)


with open('input.txt') as f:
    data = f.read().splitlines()

with open('example.txt') as f:
    example = f.read().splitlines()

instructions = [parse_instruction(e) for e in example]
for i in instructions:
    print(i)

print()

test = set()
print(test)
test.add(0)
print(test)
test.add(1)
print(test)
test.add(1)
print(test)