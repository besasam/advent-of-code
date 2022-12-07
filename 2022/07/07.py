class File:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def get_size(self) -> int:
        return self.size


class Directory:
    def __init__(self, name: str, parent=None):
        self.name = name
        self.parent = parent
        self.files = dict()

    def touch(self, file):
        if file.name in self.files:
            return
        self.files[file.name] = file

    def get_size(self) -> int:
        if not self.files:
            return 0
        return sum(self.files[i].get_size() for i in self.files)


def make(terminal_output: list) -> Directory:
    root = Directory('/')
    cur = root
    for i in terminal_output:
        if i[0] == '$':
            if i[1] == 'cd':
                cur = root if i[2] == '/' else cur.parent if i[2] == '..' else cur.files[i[2]]
        elif i[0] == 'dir':
            cur.files[i[1]] = Directory(i[1], cur)
        else:
            cur.files[i[1]] = File(i[1], int(i[0]))
    return root


def traverse(directory):
    yield directory
    for d in directory.files:
        if type(directory.files[d]) == Directory:
            yield from traverse(directory.files[d])


def part_1(data: list) -> int:
    return sum(s for d in traverse(make(data)) if (s := d.get_size()) <= 100000)


def part_2(data: list) -> int:
    root = make(data)
    lim = 30000000 - (70000000 - root.get_size())
    return min(s for d in traverse(root) if (s := d.get_size()) >= lim)


with open('input.txt') as f:
    data = [line.split() for line in f.read().splitlines()]

print(part_2(data))
