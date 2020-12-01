from bfs import BFS


# God bless StackOverflow
def powerset(s):
    def ps(s):
        x = len(s)
        masks = [1 << i for i in range(x)]
        for i in range(1 << x):
            yield [ss for mask, ss in zip(masks, s) if i & mask]
    return list(ps(s))


def copy_state(state):
    return list_to_state(state_to_list(state))


def copy_list(state):
    return [s[:] for s in state]


def state_to_list(state):
    return [list(s) for s in state]


def list_to_state(state):
    return tuple(tuple(set(s)) for s in state)


class RTF:
    def __init__(self, elements, floors):
        self.pos = elements
        self.neg = [-x for x in self.pos]
        self.vars = self.pos + self.neg + [0]
        self.domain = list(range(floors))

    # Takes a single floor in a state as an argument
    # and checks if constraints are satisfied
    def conflict(self, s):
        pos = [x for x in s if x > 0]
        neg = [x for x in s if x < 0]
        if not neg:
            return False
        for p in pos:
            if -p not in neg:
                return True
        return False

    # Checks constraints for all floors in state
    def valid_state(self, state):
        for s in state:
            if self.conflict(s):
                return False
        return True

    def next_states(self, state):
        next_states = []
        pos = -1
        for i, s in enumerate(state):
            if 0 in s:
                pos = i
        if pos != -1:
            to = []
            if pos > 0:
                to.append(pos - 1)
            if pos < len(state) - 1:
                to.append(pos + 1)
            if len(state[pos]) > 2:
                state_copy = state_to_list(state)
                state_copy[pos].remove(0)
                payload = [0]
                for x in state_copy[pos]:
                    state_copy_x = copy_list(state_copy)
                    state_copy_x[pos].remove(x)
                    payload_x = payload[:]
                    payload_x.append(x)
                    for t in to:
                        next_x = copy_list(state_copy_x)
                        next_x[t] += payload_x
                        next_state_x = list_to_state(next_x)
                        if self.valid_state(next_state_x):
                            next_states.append(copy_state(next_state_x))
                    for y in state_copy_x[pos]:
                        state_copy_y = copy_list(state_copy_x)
                        state_copy_y[pos].remove(y)
                        payload_y = payload_x[:]
                        payload_y.append(y)
                        for t in to:
                            next_y = copy_list(state_copy_y)
                            next_y[t] += payload_y
                            next_state_y = list_to_state(next_y)
                            if self.valid_state(next_state_y):
                                next_states.append(copy_state(next_state_y))
        return next_states

    def get_solutions(self, start, goal):
        bfs = BFS()
        solutions = bfs.search(start, goal, self.next_states)
        return bfs.paths


def part_1():
    #elements = [H, Li] = [i + 1 for i in range(2)]
    elements = [Sr, Pu, Tm, Ru, Cm] = [i + 1 for i in range(5)]
    floors = 4
    rtf = RTF(elements, floors)
    vars = rtf.vars
    start = (tuple({0, -Sr, Sr, -Pu, Pu}), tuple({-Tm, -Ru, Ru, -Cm, Cm}), tuple({Tm}), tuple(set()))
    goal = (tuple(set()), tuple(set()), tuple(set()), tuple(set(vars)))
    solutions = rtf.get_solutions(start, goal)
    return min(solutions)


print(part_1())
