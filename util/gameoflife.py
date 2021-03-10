from collections.abc import MutableMapping
from dataclasses import dataclass, field


@dataclass
class Cell:
    grid_size: tuple[int]
    pos: tuple[int]
    active: bool = False
    neighbors: list = field(default_factory=list)

    def get_neighbors(self):
        if self.neighbors:
            return self.neighbors



@dataclass
class Grid:
    map: dict or MutableMapping
