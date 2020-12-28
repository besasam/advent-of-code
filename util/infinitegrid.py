from collections.abc import MutableMapping


class Grid2D(MutableMapping):
    def __init__(self, init_value=None):
        self.store = dict()
        self.init_value = init_value

    def all_values(self):
        values = []
        for y in self.store:
            values += self.store[y].values()
        return values

    def prune(self):
        for y in list(self.store.keys()):
            for x in list(self.store[y].keys()):
                if self.store[y][x] == self.init_value:
                    self.store[y].pop(x)
            if not self.store[y]:
                self.store.pop(y)

    def __getitem__(self, key: tuple):
        x, y = key
        try:
            el = self.store[y][x]
        except KeyError:
            el = self.init_value
            if y not in self.store:
                self.store[y] = {x: el}
            else:
                self.store[y][x] = el
        return el

    def __setitem__(self, key: tuple, value):
        x, y = key
        try:
            self.store[y][x] = value
        except KeyError:
            self.store[y] = {x: value}

    def __delitem__(self, key: tuple):
        x, y = key
        try:
            del self.store[y][x]
        except KeyError:
            pass

    def __iter__(self):
        return iter(self.store)

    def __len__(self):
        return len(self.store)

    def __repr__(self):
        return self.store

    def __str__(self):
        return str(self.store)

