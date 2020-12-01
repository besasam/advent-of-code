class Keypad:
    keypad = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    row = 1
    col = 1

    def step(self, instruction):
        if instruction == 'U' and self.row != 0:
            self.row -= 1
        elif instruction == 'D' and self.row != 2:
            self.row += 1
        elif instruction == 'L' and self.col != 0:
            self.col -= 1
        elif instruction == 'R' and self.col != 2:
            self.col += 1

    def get_next_button(self, instructions):
        for instruction in instructions:
            self.step(instruction)
        return self.keypad[self.row][self.col]

    def get_code(self, all_instructions):
        code = ''
        for instructions in all_instructions:
            code += str(self.get_next_button(instructions))
        return code


class FunkyKeypad(Keypad):
    keypad = [
        ['', '', 1, '', ''],
        ['', 2, 3, 4, ''],
        [5, 6, 7, 8, 9],
        ['', 'A', 'B', 'C', ''],
        ['', '', 'D', '', '']
    ]
    row = 2
    col = 0

    def step(self, instruction):
        if instruction == 'U' and self.row != 0 and self.keypad[self.row-1][self.col] != '':
            self.row -= 1
        elif instruction == 'D' and self.row != 4 and self.keypad[self.row+1][self.col] != '':
            self.row += 1
        elif instruction == 'L' and self.col != 0 and self.keypad[self.row][self.col-1] != '':
            self.col -= 1
        elif instruction == 'R' and self.col != 4 and self.keypad[self.row][self.col+1] != '':
            self.col += 1


def part_1(data):
    keypad = Keypad()
    return keypad.get_code(data)


def part_2(data):
    keypad = FunkyKeypad()
    return keypad.get_code(data)


with open('input.txt') as f:
    data = f.read().splitlines()

print(part_2(data))