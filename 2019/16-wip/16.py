class FFT:
    def __init__(self, signal: str):
        self.signal = [int(x) for x in signal]
        self.offset = int(signal[:8])
        self.len = len(self.signal)
        self.pattern = [0, 1, 0, -1]
        self.pattern_cache = dict()

    def phase(self):
        next_signal = []
        for i in range(self.len):
            next_signal.append(self.calculate(i))
        self.signal = next_signal
        return next_signal

    def calculate(self, pos: int):
        pattern = self.get_pattern(pos)
        result = sum([pattern[i]*self.signal[i] for i in range(self.len)])
        return abs(result) % 10

    def get_pattern(self, pos: int):
        if pos in self.pattern_cache:
            return self.pattern_cache[pos]
        base_pattern = [p for p in self.pattern for _ in range(pos+1)]
        pattern = base_pattern[:]
        while len(pattern) <= self.len:
            pattern.extend(base_pattern)
        self.pattern_cache[pos] = pattern[1:self.len+1]
        return self.pattern_cache[pos]


def part_1(data):
    fft = FFT(data)
    for _ in range(100):
        fft.phase()
    return ''.join([str(x) for x in fft.signal[:8]])


def part_2(data):
    fft = FFT(data*10000)
    for i in range(100):
        print(i)
        fft.phase()
    return ''.join([str(x) for x in fft.signal[fft.offset:fft.offset+8]])


with open('input.txt') as f:
    data = f.readline()

test = '03036732577212944063491565474664'
print(part_2(test))
