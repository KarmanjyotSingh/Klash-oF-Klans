from building import Building


class Hut(Building):

    def __init__(self, x, y, size=(1, 1), health=10):
        super().__init__(x, y, size, health)
        self.points = 1
        self.type = "HUT"
        
