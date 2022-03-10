from building import Building
import globals as macros

class Hut(Building):

    def __init__(self, x, y, size=(1, 1), health=100):
        super().__init__(x, y, size, health)
        self.points = 1
        self.type = "HUT"
        self.texture = macros.HUT
        self.tile = macros.HUT_TILE
    
