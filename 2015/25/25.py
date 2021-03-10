class WeatherMachine:
    def __init__(self, n: int, mul: int, mod: int):
        self.n = n
        self.mul = mul
        self.mod = mod

    def get_code_by_position(self, row: int, col: int):
        i = 1
        while row > 1 or col > 1:
            i += 1
            if col == 1:
                col = row - 1
                row = 1
            else:
                row += 1
                col -= 1
        return i

    def nth_code(self, n: int):
        res = self.n
        while n > 1:
            res = (res * self.mul) % self.mod
            n -= 1
        return res


def part_1():
    wm = WeatherMachine(20151125, 252533, 33554393)
    return wm.nth_code(wm.get_code_by_position(2978, 3083))


print(part_1())
