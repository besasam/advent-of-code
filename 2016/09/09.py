import re
import math


class Decompressor:
    def decompress(self, string):
        self._initialize(string)
        while len(self.buffer) > 0:
            self._write()
        return ''.join(self.result)

    def _initialize(self, string):
        self.result = []
        self.buffer = string
        self.marker = None
        self.span = 0
        self.times = 0

    def _write(self):
        if self.marker:
            self._parse_marker()
            s = self.buffer[:self.span]
            while self.times > 0:
                self.result.append(s)
                self.times -= 1
            self.buffer = self.buffer[self.span:]
            self.marker = None
        p = self.buffer.find('(')
        if p == -1:
            self.result.append(self.buffer)
            self.buffer = ''
            return
        self.result.append(self.buffer[:p])
        self.buffer = self.buffer[p:]
        m = self._is_marker()
        if m:
            self.marker = m
        else:
            self.result.append(self.buffer[0])
            self.buffer = self.buffer[1:]

    def _is_marker(self):
        return re.search(r'\(\d+[x]\d+\)', self.buffer)

    def _parse_marker(self):
        end = self.marker.span()[1]
        b = self.buffer[1:end-1].split('x')
        self.span = int(b[0])
        self.times = int(b[1])
        self.buffer = self.buffer[end:]


class MetaDecompressor:
    # def decompress(self, string):
    #     self._initialize(string)
    #     if self.start:
    #         self.length += self.content.pop(0)
    #     while self.content:
    #         print(self.markers)
    #         print(self.content)
    #         print(self.length)
    #         print()
    #         if self.markers:
    #             break
    #         else:
    #             self.length += self.content.pop()
    #     # while self.content:
    #     #     print(self.markers)
    #     #     print(self.content)
    #     #     print(self.length)
    #     #     print()
    #     #     if self.markers:
    #     #         [span, times] = self.markers.pop()
    #     #         self.length += (span * times) + (self.content.pop() - span)
    #     #     else:
    #     #         self.length += self.content.pop()
    #     return self.length
    #
    # def _initialize(self, string):
    #     self.length = 0
    #     self.markers = [list(map(int, m[1:-1].split('x'))) for m in re.findall(r'\(\d+[x]\d+\)', string)]
    #     self.content = [len(c) for c in re.split(r'\(\d+[x]\d+\)', string)]
    #     self.start = string[0] != '('
    #
    # def _unpack(self):
    #     return
    #
    # def _marker_length(self, i):
    #     return sum([int(math.log10(m)) for m in self.markers[i]]) + 3
    #
    # def _markers_in_span(self):
    #     count = 0
    #     if len(self.markers) < 2:
    #         return count
    #     span = self.markers[0][0]
    #     l = 0
    #     for i in range(len(self.markers) - 1):
    #         l += self.content[i] + self._marker_length(i+1)
    #         if span < l:
    #             return count
    #         count += 1
    #     return count
    class Marker:
        def __init__(self, m):
            self.len = len(m)
            [self.span, self.times] = list(map(int, m[1:-1].split('x')))

    def decompress(self, string):
        self._initialize(string)
        return self._write()

    def _initialize(self, string):
        self.file = []
        self.buffer = string

    def _write(self):
        m = re.search(r'\(\d+[x]\d+\)', self.buffer)
        self.file.append(m.span()[0])
        print(m.group())
        return self.file


def part_1(data):
    d = Decompressor()
    return len(d.decompress(data))


# with open('input.txt') as f:
#    data = f.read()

test = 'X(8x2)(3x3)ABCY'
print(test)
print()
md = MetaDecompressor()
print(md.decompress(test))