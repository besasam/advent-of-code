import re


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
        b = self.buffer[1:end - 1].split('x')
        self.span = int(b[0])
        self.times = int(b[1])
        self.buffer = self.buffer[end:]


class MetaDecompressor:
    marker_regexp = r'\(\d+x\d+\)'

    def get_decompressed_length(self, string: str):
        if string == '':
            return 0
        marker_match = re.search(self.marker_regexp, string)
        if marker_match is None:
            return len(string)
        head, tail, marker = string[:marker_match.start()], string[marker_match.end():], marker_match.group()
        span, times = [int(c) for c in marker[1:-1].split('x')]
        cur, nex = tail[:span], tail[span:]
        return len(head) + times * self.get_decompressed_length(cur) + self.get_decompressed_length(nex)


def part_1(data):
    d = Decompressor()
    return len(d.decompress(data))


def part_2(data):
    md = MetaDecompressor()
    return md.get_decompressed_length(data)


with open('input.txt') as f:
   data = f.read()

print(part_2(data))