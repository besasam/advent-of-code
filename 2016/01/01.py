class GridWalk:
    position = [0, 0]
    orientation = 0
    horizontal = []
    vertical = []
    last_path = {}

    def __init__(self, path):
        self.path = path

    def turn(self, direction):
        orientation = self.orientation
        if direction == 'R':
            orientation += 1
        else:
            orientation -= 1
        self.orientation = orientation % 4

    def step(self, instruction):
        direction = instruction[0]
        distance = int(instruction[1:])
        self.turn(direction)
        if self.orientation == 0:
            self.position[1] += distance
        elif self.orientation == 1:
            self.position[0] += distance
        elif self.orientation == 2:
            self.position[1] -= distance
        else:
            self.position[0] -= distance

    def follow_path(self):
        for instruction in self.path:
            self.step(instruction)

    def get_distance(self, position):
        return sum([abs(p) for p in position])

    def visit(self, instruction):
        [cur_x, cur_y] = self.position
        self.step(instruction)
        [new_x, new_y] = self.position
        if self.orientation in [0, 2]:
            self.last_path = {
                'x': cur_x,
                'start': min([cur_y, new_y]),
                'end': max([cur_y, new_y])
            }
        else:
            self.last_path = {
                'y': cur_y,
                'start': min([cur_x, new_x]),
                'end': max([cur_x, new_x])
            }

    def check_for_intersection(self, horizontal, vertical):
        if vertical['x'] not in range(horizontal['start'], horizontal['end'] + 1) or horizontal['y'] not in range(vertical['start'], vertical['end'] + 1):
            return
        return [vertical['x'], horizontal['y']]

    def find_first_intersection(self):
        for instruction in self.path:
            previous_path = self.last_path
            self.visit(instruction)
            if 'x' in self.last_path:
                for path in self.horizontal:
                    if path != previous_path:
                        check = self.check_for_intersection(path, self.last_path)
                        if check:
                            return check
                self.vertical.append(self.last_path)
            else:
                for path in self.vertical:
                    if path != previous_path:
                        check = self.check_for_intersection(self.last_path, path)
                        if check:
                            return check
                self.horizontal.append(self.last_path)

    def part_1(self):
        self.follow_path()
        return self.get_distance(self.position)

    def part_2(self):
        intersection = self.find_first_intersection()
        return self.get_distance(intersection)


with open('input.txt') as f:
   data = f.read()
path = data.split(', ')
grid_walk = GridWalk(path)
print(grid_walk.part2())