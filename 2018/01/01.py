class ElvishDevice:
    def __init__(self):
        self.frequency = 0

    def calibrate(self, data):
        self.frequency = 0
        for frequency in data:
            self.frequency += frequency
        return self.frequency

    def calibrate_yield(self, data):
        for frequency in data:
            self.frequency += frequency
            yield self.frequency

    def check_for_repeat_value(self, data):
        self.frequency = 0
        vals = set()
        while True:
            for frequency in self.calibrate_yield(data):
                if frequency in vals:
                    return frequency
                vals.add(frequency)


def part_1(data):
    device = ElvishDevice()
    return device.calibrate(data)


def part_2(data):
    device = ElvishDevice()
    return device.check_for_repeat_value(data)


with open('input.txt') as f:
    data = [int(line) for line in f.read().splitlines()]

print(part_2(data))
