class Maze:
    def __init__(self, maze, modified=False):
        self.m = maze[:]
        self.cur = 0
        self.mod = modified

    def jump_to_exit(self):
        c = 1
        while True:
            next = self.next()
            if self.cur + next >= len(self.m) or self.cur + next < 0:
                return c
            c += 1
            self.cur = self.cur + next

    def next(self):
        jump = self.m[self.cur]
        if self.mod and jump >= 3:
            self.m[self.cur] -= 1
        else:
            self.m[self.cur] += 1
        return jump


def part_1(maze):
    m = Maze(maze)
    return m.jump_to_exit()


def part_2(maze):
    m = Maze(maze, True)
    return m.jump_to_exit()


test = [0, 3, 0, 1, -3]
with open('input.txt') as f:
    data = [int(l) for l in f.read().splitlines()]
print(part_2(data))