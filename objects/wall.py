from building import Building


class Wall(Building):
    def __init__(self, x, y, size=(1, 1), health=10, level=1):
        super().__init__(x, y, size, health)
        self.points = 1
        self.type = "WALL"
        self.drawing = "#"
        self.level = level
        
