class WrappingInteger:
    def __init__(self, val, ceil: int, floor: int = 0):
        self.ceil = ceil
        self.floor = floor
        m = int(val) % ceil
        if floor == 1 and m == 0:
            self.val = ceil
        else:
            self.val = m

    def __add__(self, other):
        return WrappingInteger(self.val + int(other), self.ceil, self.floor)

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        self.val = int(self.__add__(other))
        return self

    def __sub__(self, other):
        return WrappingInteger(self.val - int(other), self.ceil, self.floor)

    def __rsub__(self, other):
        return WrappingInteger(int(other) - self.val, self.ceil, self.floor)

    def __isub__(self, other):
        self.val = int(self.__sub__(other))
        return self

    def __lshift__(self, other):
        return WrappingInteger(self.val << int(other), self.ceil, self.floor)

    def __rlshift__(self, other):
        return WrappingInteger(int(other) << self.val, self.ceil, self.floor)

    def __rshift__(self, other):
        return WrappingInteger(self.val >> int(other), self.ceil, self.floor)

    def __rrshift__(self, other):
        return WrappingInteger(int(other) >> self.val, self.ceil, self.floor)

    def __and__(self, other):
        return WrappingInteger(self.val & int(other), self.ceil, self.floor)

    def __rand__(self, other):
        return WrappingInteger(int(other) & self.val, self.ceil, self.floor)

    def __or__(self, other):
        return WrappingInteger(self.val | int(other), self.ceil, self.floor)

    def __ror__(self, other):
        return WrappingInteger(int(other) | self.val, self.ceil, self.floor)

    def __xor__(self, other):
        return WrappingInteger(self.val ^ int(other), self.ceil, self.floor)

    def __rxor__(self, other):
        return WrappingInteger(int(other) ^ self.val, self.ceil, self.floor)

    def __invert__(self):
        return WrappingInteger(~self.val + 1, self.ceil, self.floor)

    def __eq__(self, other):
        return self.val == int(other)

    def __lt__(self, other):
        return self.val < int(other)

    def __le__(self, other):
        return self.val <= int(other)

    def __gt__(self, other):
        return self.val > int(other)

    def __ge__(self, other):
        return self.val >= int(other)

    def __ne__(self, other):
        return self.val != int(other)

    def __repr__(self):
        return str(self.val)

    def __str__(self):
        return str(self.val)

    def __int__(self):
        return self.val


class Int16Bit(WrappingInteger):
    def __init__(self, val):
        super().__init__(val, 65535, 0)
