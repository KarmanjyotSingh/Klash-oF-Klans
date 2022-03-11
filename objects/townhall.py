# define the town hall class here

from objects.building import Building
import objects.globals as macros


class TownHall(Building):

    def __init__(self, x, y, size=(1, 1), health=10):
        super().__init__(x, y, size,macros.TOWN_HALL_HEALTH)
        self.points = 100
        self.type = "TOWN_HALL"
        self.drawing = ["           x",
                        ".-. _______|",
                        "|=|/     /  \\",
                        "| |_____|_\"\"_|",
                        "|_|_[X]_|____|"]
